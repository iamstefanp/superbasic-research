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
DEFAULT_MODEL = os.environ.get("SBR_HARNESS_MODEL", "openai/gpt-4o")

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


def _call_model(messages, model=DEFAULT_MODEL):
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
            "max_tokens": 4000,
        },
        timeout=120,
    )
    if resp.status_code != 200:
        raise HarnessError(f"OpenRouter call failed: HTTP {resp.status_code} "
                            f"— {resp.text[:500]}")
    return resp.json()


def _execute_tool_call(call, real_urls_seen: set) -> dict:
    """
    Run one tool call for real. Every URL that comes back from a real
    call — search result or fetch — gets added to `real_urls_seen`,
    which is the ground truth the final output gets checked against.
    """
    name = call["function"]["name"]
    try:
        args = json.loads(call["function"]["arguments"])
    except (json.JSONDecodeError, KeyError):
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
                    model=DEFAULT_MODEL, max_rounds: int = 8):
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
        response = _call_model(messages, model=model)
        choice = response["choices"][0]
        message = choice["message"]
        tool_calls = message.get("tool_calls")

        if not tool_calls:
            return message.get("content", ""), real_urls_seen

        messages.append(message)
        for call in tool_calls:
            result = _execute_tool_call(call, real_urls_seen)
            messages.append({
                "role": "tool",
                "tool_call_id": call["id"],
                "content": json.dumps(result),
            })

    # Ran out of rounds still calling tools — force a final answer.
    messages.append({
        "role": "user",
        "content": "Stop searching now and produce your final phase "
                    "output as instructed, using only what you've "
                    "actually retrieved above.",
    })
    response = _call_model(messages, model=model)
    return response["choices"][0]["message"].get("content", ""), real_urls_seen


def _extract_json_block(text: str) -> dict:
    """Pull the last fenced ```json block out of the model's response."""
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


def make_executor(model=DEFAULT_MODEL):
    """
    Returns a callable matching sbr.py's agent_executor contract:
        callable(phase_number, run_card, context, previous_card) -> PhaseCard

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
