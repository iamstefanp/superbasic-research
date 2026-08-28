# Maintenance

This repo's central claim — the Stage 2 harness prevents source
fabrication — is only as current as the last time it was actually
re-verified. A model support table with no date on it is a claim with
no expiry, which is a quiet way of overstating confidence. This file
is how re-verification stays a routine, not something that only
happens when someone notices a problem.

## The trigger taxonomy

Not every reason to re-test is the same kind of event. Some are code
changes (automatic), some are external signals nobody inside this repo
can see coming (need a human or a monitoring process to notice), and
one is a calendar fact (nothing "announces" model drift).

| Trigger | Why it matters | How it fires |
|---|---|---|
| **New model release / major version bump** | A tracked model family shipped a new version — needs verification before the support table can trust it | `repository_dispatch: new-model-released` — see below |
| **Community/internal failure report** | Someone reports the method producing bad output | `repository_dispatch: failure-reported` |
| **Provider silently repoints a model alias** | e.g. `anthropic/claude-sonnet-5` on OpenRouter starts resolving to a materially different model, with no version bump to notice | Only the monthly schedule catches this — nothing announces it |
| **Provider API contract change** | e.g. a tool-call argument format changes — already happened once (Ollama sends a parsed dict, OpenAI/OpenRouter send a JSON string) | Monthly schedule, or manual `workflow_dispatch` if suspected |
| **Code change to `sbr.py` / `harness/executor.py` / enforcement logic** | The one thing that should never ship without re-verification | Automatic — `pull_request` trigger runs H3 on every touching PR |
| **New attack shape reported** | Someone finds a bypass technique not in the current battery | Becomes a code change (a new `test_*.py` case) → covered by the PR trigger above |
| **Search or model provider swapped** | e.g. Tavily → Brave/Serper, or a new backend added | Manual `workflow_dispatch` before the swap ships |
| **Pre-release checklist** | Don't tag a release under an unverified regression | Manual `workflow_dispatch`, part of the release checklist |

**Live tracking:** [SBR Maintenance Triggers](https://docs.google.com/spreadsheets/d/1xAbS0aQSfGQTuUMMvrpdCbKsWLO4Tmql7ETvaxJgoBQ/edit) —
a `Log` tab for actual events (date, trigger type, source, what was
affected, dispatch method, status, evidence link) and a `Trigger Types`
reference tab mirroring the table above. Log an event there whenever
one of these fires, whether it was caught automatically or noticed by
a human.

## How re-testing actually runs

[`.github/workflows/redteam.yml`](.github/workflows/redteam.yml) — two
jobs:

- **`fast-checks`** — H3 (enforcement precision) only. No API keys
  needed, runs in seconds. Fires on every pull request touching
  `sbr.py`, `harness/**`, or `tests/redteam/**`. This is the one that
  should never be skipped or overridden — it's free and it's exactly
  the layer a code change to enforcement logic could silently weaken.
- **`full-redteam`** — all 5 hypotheses (H1, H2, H4, H5 — H3 already
  ran in `fast-checks`), live model calls, real API spend. Fires on:
  - `schedule` — the 1st of every month, UTC 06:00. The calendar-based
    safety net for silent drift.
  - `workflow_dispatch` — manual, with an optional `reason` input that
    shows in the run log. Use before a tagged release, or to check
    something right now.
  - `repository_dispatch` — two event types, `new-model-released` and
    `failure-reported`, meant to be fired by an external process (a
    monitoring workflow, a script watching provider changelogs, or a
    human via `gh api`) without that process needing to know anything
    about this repo beyond its name and these two event names:
    ```bash
    gh api repos/iamstefanp/superbasic-research/dispatches \
      -f event_type=new-model-released \
      -f 'client_payload[model]=example/new-model-name'
    ```

Every hypothesis step captures its actual exit code (0=PASS, 1=FAIL,
2=INCONCLUSIVE — see `tests/redteam/_shared.py`'s `exit_code_for`), not
just success/failure, because GitHub Actions' own step outcome can't
tell a real regression apart from an external outage. **Only a genuine
FAIL fails the workflow** — an INCONCLUSIVE (a provider having a bad
day, same as the real Mistral outage this evaluation hit once already)
is surfaced in the job summary and the committed evidence, not treated
as a build break. Evidence from every full run is committed back to
`tests/redteam/evidence/` automatically.

## One-time setup (you, not me)

The workflow needs three repo secrets I cannot set myself — GitHub
secrets require repo admin access through the web UI or `gh secret set`
run by someone authenticated as an admin on the repo:

```bash
gh secret set OPENROUTER_API_KEY --repo iamstefanp/superbasic-research
gh secret set TAVILY_API_KEY --repo iamstefanp/superbasic-research
gh secret set MISTRAL_API_KEY --repo iamstefanp/superbasic-research
```

(Each prompts for the value, or pipe it in: `echo "$KEY" | gh secret set ... `.)

Without these, `fast-checks` still works (no keys needed), but
`full-redteam` will fail every hypothesis step with a harness error —
which is the correct, honest behavior (INCONCLUSIVE, not a false PASS)
rather than silently skipping.

## Adding a new model to the support table

1. Add it to the relevant `TARGETS`/`MODELS` list in the `tests/redteam/test_*.py`
   files you want to cover it (at minimum `test_repeat_consistency.py`
   for a real consistency read).
2. Run locally first (`python3 tests/redteam/test_repeat_consistency.py`)
   or fire `workflow_dispatch` to run it in CI.
3. Update the model-support table in `README.md` with the result and
   link the evidence.
4. Log the addition in the Maintenance Triggers sheet.

## Known gap in this process, stated plainly

Provider changelogs aren't monitored by anything in this repo — the
`repository_dispatch` hooks exist so an external process *can* do that
and notify this repo, but building that watcher is not part of this
repo's own scope. Until something feeds `new-model-released` events in,
the monthly schedule is the only thing standing between a silent model
change and this repo's claims going stale without anyone noticing.
