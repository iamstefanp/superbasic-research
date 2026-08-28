# Cross-Model Log

::: tip Full raw log
This page summarizes
[`tests/CROSS-MODEL.md`](https://github.com/iamstefanp/superbasic-research/blob/main/tests/CROSS-MODEL.md)
on GitHub — the chronological narrative log, every round in full detail,
kept as the single source of truth. This page is the story arc; that
file is the record.
:::

## The discovery

Cross-model testing found that pasting `SKILL.md` as a bare system prompt
— no real search tool wired into the request — makes some models
fabricate entire source tables and stamp them CONFIRMED using the
method's own scoring apparatus, which reads as *more* credible than a
plain hallucination, not less.

**Round 1**, before any fix existed: **Kimi K2, DeepSeek, and Llama 3.3
70B all fabricated**, independently inventing numbers for the same fact
that didn't even agree with each other. GPT-5 and Gemini 2.5 Pro instead
ran out of their token budget being honest about the constraint — a
different, better failure mode, but still not a pass.

## The fix, applied in stages

1. **Stage 0/1** — disclosure and falsifiable-URL requirements shipped
   the same day.
2. **A prompt-level tool-access gate** was added — and then confirmed
   insufficient: **Llama 3.3 70B fabricated anyway**, simply skipping the
   declaration. A prompt instruction only works on a model willing to
   obey it.
3. **Stage 2 — the real tool-calling harness** (`harness/executor.py`):
   the model gets a real `web_search`/`fetch_url` tool; the runtime
   executes it for real and cross-checks every cited source against what
   actually came back. This is the only stage that structurally prevents
   fabrication rather than disclosing, detecting, or discouraging it.

## Verification: 6 of 6 required models, clean

Every model on the required support list came back with 100% of cited
sources genuinely retrieved under the Stage 2 harness — including one
**live-caught fabrication attempt**.

| Model | Result |
|---|---|
| Claude | Clean — also verified separately under the harness itself, not just the method battery |
| Gemini | Clean |
| ChatGPT (GPT-5) | Clean — after fixing a real bug: the harness's 4,000-token default was too tight for GPT-5's reasoning pattern, silently producing 0 sources |
| **Mistral** | **Caught fabricating live** — 5 of 7 sources invented, all correctly overridden by the harness. The strongest proof yet that enforcement works against a model that actually tries, not just one that happens to behave. |
| DeepSeek | Clean |
| Llama (3.3 70B, cloud) | Clean — the exact model the prompt-level gate alone could not stop |
| Llama (local, via Ollama) | Not clean — two distinct failure shapes at 3B and 8B, unresolved, disclosed as open findings |
| Qwen (extra, beyond the required list) | Clean |

## Real bugs, found and fixed in the open

- **Enforcement's key-matching bug**: the first live test (Kimi K2)
  looked for sources under specific key names and a lowercase `url`
  field; Kimi's real output used different casing, so enforcement
  silently never ran. Fixed by matching source lists by *shape*, not
  exact name.
- **Mistral's OpenRouter routing**: a verified-working BYOK key,
  confirmed active on both Mistral's own API and OpenRouter's own
  key-test, still never got attempted by OpenRouter — every call fell
  through to a rate-limited shared pool. Fixed by adding a direct
  `backend="mistral"` that bypasses OpenRouter entirely.
- **`max_tokens` needs per-model tuning**: GPT-5 and Claude both silently
  returned 0 sources at the harness's default, because they spend more
  of their budget reasoning before answering. Made configurable, with
  the actual numbers that worked documented in the full log.

## Where things stand

All required models covered. The Ollama local-model failures and the
Mistral outage pattern are open, disclosed items — see
[Red-Team Evaluation](/testing/red-team)'s Known Limitations for the
current, most precise statement of what's still unresolved.

For the complete, dated, round-by-round account —
[read the full log on GitHub](https://github.com/iamstefanp/superbasic-research/blob/main/tests/CROSS-MODEL.md).
