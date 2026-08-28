# Security & Legal

## For security teams

- **No telemetry, no phone-home.** Nothing in this repo reports usage,
  errors, or content anywhere. The only network calls the harness makes
  are to the search/LLM providers you configure yourself.
- **Nothing is trusted by default.** The harness's core mechanism exists
  because "the model says it searched" is not evidence — every cited
  source is cross-checked against what a real tool call actually
  returned, in code, not by asking the model to self-report.
- **API keys stay local.** `OPENROUTER_API_KEY` / `TAVILY_API_KEY` /
  `MISTRAL_API_KEY` are read from your own environment; nothing in this
  repo transmits them anywhere but the provider they're for.
- **Adversarially tested, with the design frozen before results
  existed.** [`redteam/PROTOCOL.md`](https://github.com/iamstefanp/superbasic-research/blob/main/tests/redteam/PROTOCOL.md)'s
  git history proves the test hypotheses predate the outcomes — not
  fitted to what happened after the fact. Full writeup:
  [Red-Team Evaluation](/testing/red-team).
- **Zero disk writes required to run the method itself** — `sbr.py`
  returns documents in memory; where they're written (Drive, local
  disk, nowhere) is entirely up to the `writer` callback you supply.

## For legal & procurement

- **CC BY-SA 4.0** — use it, adapt it, build on it. Share adaptations
  under the same terms. Full text:
  [LICENSE](https://github.com/iamstefanp/superbasic-research/blob/main/LICENSE).
- **No CLA.** Nothing to sign to use, fork, or modify this.
- **SuperBasic™ is a trademark; the method is not.** The process itself
  is open under the license above — the name has separate, narrower
  terms. See
  [TRADEMARK.md](https://github.com/iamstefanp/superbasic-research/blob/main/TRADEMARK.md).
- **Not source-available, not open-core.** There is no paid tier, no
  feature gated behind a license key, and no separate "enterprise"
  version of this repo.
