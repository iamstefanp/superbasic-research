"""
executor.py — a reference `agent_executor` for sbr.py, backed by real tools.

sbr.py's run_sbr() takes any `agent_executor` matching:
    callable(phase_number, run_card, context, previous_card) -> PhaseCard

Nothing about that contract requires real tool access — which is
exactly the gap tests/CROSS-MODEL.md found. This file is a conforming
implementation that closes it: the model gets an actual `web_search` and
`fetch_url` tool via the LLM API's real function-calling, this file
executes the tool call for real (search_provider.py), and inserts the
genuine result back into the conversation. The model never gets to type
a URL and have it trusted — every source in the final output is
cross-checked against what the real tool calls actually returned in
THIS run, and anything that doesn't match is overridden, not reported.

This is Stage 2 of the fix in tests/CROSS-MODEL.md. It only helps the
governed-mode use case: running sbr.py as real code with this as the
executor. It does nothing for someone pasting SKILL.md into a bare chat
— that gap is Stage 0/1/3/4's job, not this file's.
"""

import json
import os
import re

import requests

import search_provider

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
MISTRAL_URL = "https://api.mistral.ai/v1/chat/completions"
OLLAMA_URL = os.environ.get("SBR_OLLAMA_URL", "http://localhost:11434/api/chat")
DEFAULT_MODEL = os.environ.get("SBR_HARNESS_MODEL", "openai/gpt-4o")
DEFAULT_BACKEND = os.environ.get("SBR_HARNESS_BACKEND", "openrouter")
# 4000 was too tight for a heavy-reasoning model doing real multi-round
# tool calls — found via testing (GPT-5, 2026-08-28): it spent its
# budget on internal reasoning about the tool-access constraint and
# never reached a final answer, producing 0 sources not because it
# fabricated or refused, but because it ran out of room. Configurable
# rather than a second hardcoded guess.
DEFAULT_MAX_TOKENS = int(os.environ.get("SBR_HARNESS_MAX_TOKENS", "4000"))

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "web_search",
            "description": (
                "Search the live web. Returns real results — title, URL, "
                "a content snippet, and a publish date where available. "
                "Use this before citing anything; a search result alone "
                "is not a source (open it with fetch_url first)."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string",
                               "description": "The exact search query."},
                },
                "required": ["query"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "fetch_url",
            "description": (
                "Open a specific URL and return its real, extracted "
                "text content. Use this to actually read a source before "
                "citing it — a search snippet is not enough."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "url": {"type": "string",
                             "description": "The exact URL to open."},
                },
                "required": ["url"],
            },
        },
    },
]


class HarnessError(Exception):
    """Raised when the harness itself fails — not a research-content
    failure, which sbr.py's own gates handle."""


def _call_model(messages, model=DEFAULT_MODEL, backend=DEFAULT_BACKEND,
                 max_tokens=DEFAULT_MAX_TOKENS):
    """
    Returns a normalized dict: {"message": {"content": str|None,
    "tool_calls": [{"id": str, "function": {"name": str,
    "arguments": dict|str}}]}}.

    Three backends, because they're genuinely different APIs, not just
    different model names:
    - openrouter: cloud, any tool-calling-capable model on OpenRouter.
    - mistral: cloud, Mistral's own API direct — added specifically
      because OpenRouter's BYOK routing for Mistral was confirmed broken
      (2026-08-28: a verified-working key, confirmed active on both
      Mistral's own API and OpenRouter's own key-test, still never got
      attempted by OpenRouter — every call fell through to the
      rate-limited shared pool regardless). Going direct sidesteps that
      routing gap entirely rather than waiting on OpenRouter to fix it.
    - ollama: local, zero cloud dependency, which is exactly the
      environment where "does this model even get real tools" matters
      most — most bare-paste users running a local model have no tool
      access by default, so this is what actually closes that gap for
      them rather than just testing the cloud case again.
    """
    if backend == "ollama":
        resp = requests.post(
            OLLAMA_URL,
            json={"model": model, "messages": messages, "tools": TOOLS,
                  "stream": False},
            timeout=180,  # local inference on modest hardware is slow
        )
        if resp.status_code != 200:
            raise HarnessError(f"Ollama call failed: HTTP {resp.status_code} "
                                f"— {resp.text[:500]}")
        return resp.json()  # already {"message": {...}} shaped

    if backend == "mistral":
        key = os.environ.get("MISTRAL_API_KEY")
        if not key:
            raise HarnessError("MISTRAL_API_KEY is not set.")
        resp = requests.post(
            MISTRAL_URL,
            headers={"Authorization": f"Bearer {key}",
                     "Content-Type": "application/json"},
            json={
                "model": model,
                "messages": messages,
                "tools": TOOLS,
                "max_tokens": max_tokens,
            },
            timeout=180,
        )
        if resp.status_code != 200:
            raise HarnessError(f"Mistral call failed: HTTP {resp.status_code} "
                                f"— {resp.text[:500]}")
        data = resp.json()
        return {"message": data["choices"][0]["message"]}  # OpenAI-compatible shape

    if backend != "openrouter":
        raise HarnessError(f"Unknown backend: {backend!r} "
                            f"(expected 'openrouter', 'mistral', or 'ollama')")

    key = os.environ.get("OPENROUTER_API_KEY")
    if not key:
        raise HarnessError("OPENROUTER_API_KEY is not set.")
    resp = requests.post(
        OPENROUTER_URL,
        headers={"Authorization": f"Bearer {key}",
                 "Content-Type": "application/json"},
        json={
            "model": model,
            "messages": messages,
            "tools": TOOLS,
            "max_tokens": max_tokens,
        },
        timeout=180,
    )
    if resp.status_code != 200:
        raise HarnessError(f"OpenRouter call failed: HTTP {resp.status_code} "
                            f"— {resp.text[:500]}")
    data = resp.json()
    return {"message": data["choices"][0]["message"]}


def _execute_tool_call(call, real_urls_seen: set) -> dict:
    """
    Run one tool call for real. Every URL that comes back from a real
    call — search result or fetch — gets added to `real_urls_seen`,
    which is the ground truth the final output gets checked against.
    """
    name = call["function"]["name"]
    raw_args = call["function"]["arguments"]
    # OpenRouter/OpenAI send arguments as a JSON string; Ollama sends
    # them as an already-parsed dict (confirmed by direct probe against
    # a local model, 2026-08-28) — accept either rather than assuming
    # one API's convention is universal.
    if isinstance(raw_args, dict):
        args = raw_args
    else:
        try:
            args = json.loads(raw_args)
        except (json.JSONDecodeError, TypeError):
            args = {}

    if name == "web_search":
        query = args.get("query", "")
        try:
            results = search_provider.search(query)
        except search_provider.SearchProviderError as e:
            return {"error": str(e)}
        for r in results:
            if r.get("url"):
                real_urls_seen.add(r["url"])
        return {"query": query, "results": results}

    if name == "fetch_url":
        url = args.get("url", "")
        result = search_provider.fetch_url(url)
        if result.get("status") == 200:
            real_urls_seen.add(url)
        return result

    return {"error": f"unknown tool: {name}"}


def _run_tool_loop(system_prompt: str, user_prompt: str,
                    model=DEFAULT_MODEL, backend=DEFAULT_BACKEND,
                    max_tokens=DEFAULT_MAX_TOKENS, max_rounds: int = 8):
    """
    Drives the model through as many real tool calls as it wants, up to
    max_rounds, then returns (final_text, real_urls_seen). The loop ends
    when the model responds with no tool_calls — meaning it's done
    gathering and is producing its phase output.
    """
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]
    real_urls_seen = set()

    for _ in range(max_rounds):
        response = _call_model(messages, model=model, backend=backend, max_tokens=max_tokens)
        message = response["message"]
        tool_calls = message.get("tool_calls")

        if not tool_calls:
            return message.get("content") or "", real_urls_seen

        messages.append(message)
        for call in tool_calls:
            result = _execute_tool_call(call, real_urls_seen)
            # Ollama's tool_calls don't always carry a stable "id" the
            # same way OpenAI's do; call.get() rather than call[...] so
            # a missing id doesn't crash the loop on that backend.
            messages.append({
                "role": "tool",
                "tool_call_id": call.get("id", ""),
                "content": json.dumps(result),
            })

    # Ran out of rounds still calling tools — force a final answer.
    messages.append({
        "role": "user",
        "content": "Stop searching now and produce your final phase "
                    "output as instructed, using only what you've "
                    "actually retrieved above.",
    })
    response = _call_model(messages, model=model, backend=backend, max_tokens=max_tokens)
    return response["message"].get("content") or "", real_urls_seen


def _extract_json_block(text: str) -> dict:
    """
    Pull the last fenced ```json block out of the model's response.
    Defensively tolerant of a non-string `text` — found via testing
    (Llama 3.3 70B, 2026-08-28) that some providers return an explicit
    `content: null` rather than omitting the key, which broke the naive
    `.get("content", "")` default at the call sites; this is the
    second line of defense in case a None reaches here some other way.
    """
    if not isinstance(text, str):
        return {}
    matches = re.findall(r"```json\s*(\{.*?\})\s*```", text, re.DOTALL)
    if not matches:
        matches = re.findall(r"(\{.*\})", text, re.DOTALL)
    if not matches:
        return {}
    try:
        return json.loads(matches[-1])
    except json.JSONDecodeError:
        return {}


def _find_source_list(outputs: dict) -> list:
    """
    Locate the sources list without trusting the model to name its own
    key consistently. Found the hard way: a real run (Kimi K2, logged
    2026-08-28) named its key "Intel_Items" — matching neither "sources"
    nor "Intel Items" — and the enforcement below silently never ran,
    because a dict.get() on the wrong key returns None and the whole
    check just no-ops. That is exactly the kind of gap this file exists
    to close, so this now searches by SHAPE (a list of dicts, at least
    one of which has some case of a "url" key) rather than by name.
    """
    for value in outputs.values():
        if not isinstance(value, list) or not value:
            continue
        if any(isinstance(item, dict) and
               any(k.lower() in ("url", "urls") for k in item)
               for item in value):
            return value
    return []


def _url_key(source: dict):
    """The actual key this source dict used for its URL, whatever case
    or spelling the model chose — 'url' and 'URL' have both been
    observed in real runs. Returns None if there isn't one."""
    for k in source:
        if k.lower() == "url":
            return k
    return None


def _enforce_real_urls(outputs: dict, real_urls_seen: set) -> dict:
    """
    The core guarantee this harness exists to provide: any source in the
    output whose URL was never actually returned by a real tool call in
    this run gets overridden — retrieved forced to False, the fabricated
    URL discarded — rather than trusted because the model typed it. This
    runs regardless of what the model claims about itself.
    """
    sources = _find_source_list(outputs)
    if not sources:
        return outputs

    for s in sources:
        if not isinstance(s, dict):
            continue
        key = _url_key(s)
        url = s.get(key) if key else None
        if url not in real_urls_seen:
            s["retrieved"] = False
            s["_harness_note"] = (
                "URL not found in this run's real tool-call results — "
                "overridden by the harness, not trusted from model output."
            )
        else:
            s["retrieved"] = True
    return outputs


def make_executor(model=DEFAULT_MODEL, backend=DEFAULT_BACKEND,
                   max_tokens=DEFAULT_MAX_TOKENS):
    """
    Returns a callable matching sbr.py's agent_executor contract:
        callable(phase_number, run_card, context, previous_card) -> PhaseCard

    `backend="ollama"` runs entirely locally against an Ollama server —
    zero cloud dependency for the LLM call itself (search still needs
    Tavily, since local-only search isn't a thing this harness provides).
    This matters beyond "one more model to test": it's the actual
    environment a lot of bare-paste users are in by default, where the
    honest answer to "do I have a search tool" is usually no unless
    something like this harness gives them one deliberately.

    Import sbr.py's PhaseCard lazily to avoid a hard dependency at
    import time for callers who only want search_provider.py.
    """
    import sys
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
    import sbr

    def executor(phase_number, run_card, context, previous_card=None):
        system_prompt = sbr.build_phase_prompt(
            phase_number, run_card, context, previous_card)
        system_prompt += (
            "\n\nEnd your response with a single fenced ```json block "
            "containing your phase output as a JSON object matching the "
            "schema above. Use real tool calls — web_search then "
            "fetch_url — before citing anything; do not narrate a "
            "search you did not perform."
        )

        text, real_urls_seen = _run_tool_loop(
            system_prompt,
            f"Execute Phase {phase_number} now.",
            model=model,
            backend=backend,
            max_tokens=max_tokens,
        )

        outputs = _extract_json_block(text)
        if phase_number == 4:  # INTEL — where sources originate
            outputs = _enforce_real_urls(outputs, real_urls_seen)

        confidence = outputs.get("confidence", "MEDIUM")
        go = outputs.get("go", True)
        tool_access = bool(real_urls_seen) or phase_number != 1
        if phase_number == 1:
            outputs["tool_access"] = True  # this harness always has tools

        return sbr.PhaseCard(
            phase=phase_number,
            name=sbr.PHASE_AGENTS[phase_number]["name"],
            outputs=outputs,
            confidence=confidence,
            go=go,
        )

    return executor
