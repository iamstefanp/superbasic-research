# Reference harness — the governed-mode executor

This is Stage 2 of the fix documented in
[`../tests/CROSS-MODEL.md`](../tests/CROSS-MODEL.md). It's the only
stage in that plan that actually **prevents** source fabrication rather
than disclosing it, catching it after the fact, or making it cheaper to
spot. Everything else in this repo — the tool-access gate, the
falsifiable-URL requirement — is a mitigation for the case where this
harness *isn't* what's running. This is what should be running.

## What it does, in one sentence

The model gets a real `web_search` and `fetch_url` tool. When it calls
one, this code executes the call for real and inserts the genuine
result back into the conversation — so the model has nothing to narrate,
because the real result already exists before it writes anything. After
the model produces its final phase output, every cited source's URL is
cross-checked against the set of URLs that actually came back from real
tool calls **in this run**. Anything that doesn't match gets
`retrieved` forced to `False` by the harness — not reported by the
model, decided by code that already knows the truth.

That's the specific gap named in `tests/CROSS-MODEL.md`: Llama 3.3 70B
fabricated a full report even *after* a prompt-level tool-access gate
existed, because a prompt instruction only works on a model willing to
obey it. This harness doesn't ask the model to be honest about whether
it searched. It makes "the model decides what's real" structurally
impossible for the one thing that matters most — the URL.

## Setup

```bash
pip install -r requirements.txt

export OPENROUTER_API_KEY="..."   # already required elsewhere in this repo
export TAVILY_API_KEY="..."       # get a free key at https://tavily.com
                                   # (1,000 searches/month free tier —
                                   # enough to build and test against)
```

## Use it

```python
import sys
sys.path.insert(0, "harness")
import executor
import sbr

card = sbr.RunCard({"question": "your real research question", "mode": "LIGHT"})
ctx  = sbr.RunContext({"destination": None})

result = sbr.run_sbr(
    card, ctx,
    agent_executor=executor.make_executor(),   # this file, not a bare LLM call
    writer=lambda dest, name, content: {"id": name, "url": None},
)

print(result.status)     # COMPLETE | PARTIAL | STOPPED
print(result.documents)
```

Swap `executor.make_executor(model="anthropic/claude-3.5-sonnet")` or
any other tool-calling-capable model on OpenRouter — the harness code
doesn't change, only which model is doing the reasoning around the real
tool results.

## What this does NOT fix

- **A model can still misread or selectively quote a genuinely-fetched
  page.** The URL is real; the *interpretation* of what's on it is still
  the model's judgment call. That's a different, harder problem — this
  harness makes the evidence real, not the reasoning about it infallible.
- **It does nothing for bare-paste `SKILL.md` usage.** If someone pastes
  the method into a chat UI with no tools wired in, this file isn't in
  the loop at all. That gap is what Stage 0/1/3/4 in
  `tests/CROSS-MODEL.md` are for.
- **Paywalled, JS-rendered, or bot-blocked pages** will still return a
  low-quality or failed fetch. `search_provider.fetch_url()` reports the
  failure explicitly (`error` field) rather than silently returning
  nothing — sbr.py's INTEL phase instructions already require logging
  that as a Failed Retrieval, not substituting something else.

## Status

**Code complete, unit-tested on the pure logic (JSON extraction, URL
enforcement) with mock data. Not yet live-tested end-to-end against a
real model + real Tavily key** — that's the next step once a
`TAVILY_API_KEY` is available. The honest test, per the staged plan: run
the exact Round 1/1.5 prompts (Kimi, DeepSeek, Llama 3.3 70B — the three
models that fabricated) through this harness and confirm every source
in the resulting Report has a URL that traces to a real, logged tool
call. Log the result as Round 3 in `../tests/CROSS-MODEL.md`.
