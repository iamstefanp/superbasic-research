# Setup & Backends

This is Stage 2 of the fabrication fix documented in the
[Cross-Model Log](/testing/cross-model). It's the only stage that
actually **prevents** source fabrication rather than disclosing it,
catching it after the fact, or making it cheaper to spot.

## What it does, in one sentence

The model gets a real `web_search` and `fetch_url` tool. When it calls
one, this code executes the call for real and inserts the genuine result
back into the conversation — so the model has nothing to narrate, because
the real result already exists before it writes anything. After the
model produces its final phase output, every cited source's URL is
cross-checked against the set of URLs that actually came back from real
tool calls **in this run**. Anything that doesn't match gets `retrieved`
forced to `False` by the harness — not reported by the model, decided by
code that already knows the truth.

That's the specific gap named in the Cross-Model Log: Llama 3.3 70B
fabricated a full report even *after* a prompt-level tool-access gate
existed, because a prompt instruction only works on a model willing to
obey it. This harness doesn't ask the model to be honest about whether
it searched. It makes "the model decides what's real" structurally
impossible for the one thing that matters most — the URL.

## Setup

```bash
pip install -r requirements.txt

export TAVILY_API_KEY="..."       # get a free key at https://tavily.com
                                   # (1,000 searches/month free tier —
                                   # enough to build and test against)

# Pick a backend — see "Three backends" below:
export OPENROUTER_API_KEY="..."   # for backend="openrouter" (default)
export MISTRAL_API_KEY="..."      # for backend="mistral" (direct)
                                   # Ollama needs no key — see below
```

## Three backends

`make_executor(model=..., backend=...)` supports three, because they're
genuinely different APIs, not just different model names:

- **`backend="openrouter"`** (default) — any tool-calling-capable model
  on OpenRouter, e.g. `anthropic/claude-sonnet-5`, `openai/gpt-5`,
  `google/gemini-2.5-pro`, `deepseek/deepseek-chat`,
  `moonshotai/kimi-k2`, `qwen/qwen-2.5-72b-instruct`.
- **`backend="mistral"`** — calls `api.mistral.ai` directly. Added
  because OpenRouter's BYOK routing for Mistral was found to be broken
  (a verified-working key, confirmed active on both Mistral's own API
  and OpenRouter's own key-test, still never got attempted by
  OpenRouter — every call fell through to the rate-limited shared pool).
  Going direct sidesteps that entirely. Model: e.g.
  `mistral-large-latest`.
- **`backend="ollama"`** — local, zero cloud dependency, pointed at
  `http://localhost:11434` by default (override with `SBR_OLLAMA_URL`).
  This is the environment where "does this model even get real tools"
  matters most — most bare-paste users running a local model have no
  tool access by default. Model: whatever's pulled locally, e.g.
  `llama3.1:8b`.

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
    agent_executor=executor.make_executor(
        model="anthropic/claude-sonnet-5", backend="openrouter",
        max_tokens=12000,   # see "max_tokens matters" below — the
                            # 4,000 default is too tight for several
                            # tested models
    ),
    writer=lambda dest, name, content: {"id": name, "url": None},
)

print(result.status)     # COMPLETE | PARTIAL | STOPPED
print(result.documents)
```

### `max_tokens` matters — the default will silently fail on some models

The harness's default (`SBR_HARNESS_MAX_TOKENS`, 4,000) is tuned for
lighter models. Heavy-reasoning models (GPT-5, Claude) were found to
spend most or all of that budget on internal reasoning before producing
a final answer — the result is **0 sources, which looks like the model
refused or the harness is broken, when the real cause is running out of
room.** Confirmed and fixed by raising the budget (GPT-5 needed ~12k,
Claude needed ~20k for a full Phase 1→4 chain) — see the
[Cross-Model Log](/testing/cross-model) for the exact diagnosis. If you
get 0 sources from a capable model, raise `max_tokens` before assuming
anything else is wrong.

## What this does NOT fix

- **A model can still misread or selectively quote a genuinely-fetched
  page.** The URL is real; the *interpretation* of what's on it is still
  the model's judgment call. That's a different, harder problem — this
  harness makes the evidence real, not the reasoning about it infallible.
- **It does nothing for bare-paste `SKILL.md` usage.** If someone pastes
  the method into a chat UI with no tools wired in, this file isn't in
  the loop at all.
- **Paywalled, JS-rendered, or bot-blocked pages** will still return a
  low-quality or failed fetch. `search_provider.fetch_url()` reports the
  failure explicitly (`error` field) rather than silently returning
  nothing.

## Status

**Live-verified and formally red-teamed, not just unit-tested.** Every
one of the six required model families (Claude, Gemini, Mistral,
ChatGPT/GPT-5, DeepSeek, Llama) has run through this harness for real and
come back with 100% of cited sources genuinely retrieved — including one
live-caught fabrication attempt. Full results:
[Cross-Model Log](/testing/cross-model) and
[Red-Team Evaluation](/testing/red-team).
