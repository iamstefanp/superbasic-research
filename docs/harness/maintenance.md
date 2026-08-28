# Maintenance

This repo's central claim — the Stage 2 harness prevents source
fabrication — is only as current as the last time it was actually
re-verified. A model support table with no date on it is a claim with no
expiry, which is a quiet way of overstating confidence. This page is how
re-verification stays a routine, not something that only happens when
someone notices a problem.

## The trigger taxonomy

Not every reason to re-test is the same kind of event. Some are code
changes (automatic), some are external signals nobody inside this repo
can see coming, and one is a calendar fact — nothing "announces" model
drift.

| Trigger | Why it matters | How it fires |
|---|---|---|
| **New model release / major version bump** | A tracked model family shipped a new version — needs verification before the support table can trust it | External `repository_dispatch` event |
| **Community/internal failure report** | Someone reports the method producing bad output | External `repository_dispatch` event |
| **Provider silently repoints a model alias** | e.g. `anthropic/claude-sonnet-5` on OpenRouter starts resolving to a materially different model, with no version bump to notice | Only the monthly schedule catches this |
| **Provider API contract change** | e.g. a tool-call argument format changes — already happened once (Ollama sends a parsed dict, OpenAI/OpenRouter send a JSON string) | Monthly schedule, or manual run if suspected |
| **Code change to enforcement logic** | The one thing that should never ship without re-verification | Automatic — runs H3 on every touching PR |
| **New attack shape reported** | Someone finds a bypass technique not in the current battery | Becomes a code change → covered by the PR trigger |
| **Search or model provider swapped** | e.g. Tavily → Brave/Serper, or a new backend added | Manual run before the swap ships |
| **Pre-release checklist** | Don't tag a release under an unverified regression | Manual run, part of the release checklist |

## How re-testing actually runs

[`.github/workflows/redteam.yml`](https://github.com/iamstefanp/superbasic-research/blob/main/.github/workflows/redteam.yml)
— two jobs:

- **`fast-checks`** — H3 (enforcement precision) only. No API keys
  needed, runs in seconds. Fires on every pull request touching
  `sbr.py`, `harness/**`, or `tests/redteam/**`.
- **`full-redteam`** — all 5 hypotheses, live model calls, real API
  spend. Fires on a monthly schedule, manual dispatch, or an external
  `repository_dispatch` webhook — meant to be fired by a monitoring
  process without that process needing to know anything about this repo
  beyond its name and two event names (`new-model-released`,
  `failure-reported`).

Every hypothesis step captures its actual exit code (0 = PASS, 1 = FAIL,
2 = INCONCLUSIVE), not just success/failure, because GitHub Actions' own
step outcome can't tell a real regression apart from an external outage.
**Only a genuine FAIL fails the workflow** — an INCONCLUSIVE (a provider
having a bad day) is surfaced in the job summary and the committed
evidence, not treated as a build break. Evidence from every full run is
committed back to `tests/redteam/evidence/` automatically.

## Adding a new model to the support table

1. Add it to the relevant target list in the `tests/redteam/test_*.py`
   files you want to cover it.
2. Run locally, or fire a manual workflow run in CI.
3. Update the model-support table on the [Cross-Model Log](/testing/cross-model)
   page with the result and link the evidence.

## Known gap in this process, stated plainly

Provider changelogs aren't monitored by anything in this repo — the
`repository_dispatch` hooks exist so an external process *can* do that
and notify this repo, but building that watcher is not part of this
repo's own scope. Until something feeds `new-model-released` events in,
the monthly schedule is the only thing standing between a silent model
change and this repo's claims going stale without anyone noticing.

Full detail:
[`MAINTENANCE.md`](https://github.com/iamstefanp/superbasic-research/blob/main/MAINTENANCE.md)
on GitHub.
