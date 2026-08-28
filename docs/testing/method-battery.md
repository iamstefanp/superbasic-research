# Method Battery

Two layers of testing exist in this project, both published in full,
both including the honest miss rather than only the wins. This page
covers the first: testing the *method itself*.

[`tests/`](https://github.com/iamstefanp/superbasic-research/tree/main/tests)
is an 11-card adversarial battery, each card built around a specific trap
the method has to survive: sources that look independent but share one
origin, catalogs that genuinely disagree, entities that collide under one
name, evidence that's paywalled rather than absent, the same brief run
three times blind to check whether the method reproduces or just guesses
well once. Every run is graded by an adversarial judge with no memory of
writing the method, who independently re-fetches sources rather than
trusting the transcript.

The honest result is in there too: most cards passed, one (the replication
card) did not clear its own bar, and that failure is logged in the open
rather than smoothed over.

```
tests/
  BATTERY.md            the 11 cards
  RUBRIC.md              gates, scoring, verdict format
  RESULTS.md              the registry, one row per graded run
  CORRECTIONS.md           the change log — including a reopened finding
  FINDINGS-MEMO.md          the one-page report card
  capability-ledger.md      known-blocked domains, demonstrated per-run
  answer-keys/V-T2.md       the one frozen ground-truth key
```

- [`BATTERY.md`](https://github.com/iamstefanp/superbasic-research/blob/main/tests/BATTERY.md) — the 11 cards
- [`RESULTS.md`](https://github.com/iamstefanp/superbasic-research/blob/main/tests/RESULTS.md) — full results registry
- [`FINDINGS-MEMO.md`](https://github.com/iamstefanp/superbasic-research/blob/main/tests/FINDINGS-MEMO.md) — the one-page report card, including the reopened finding

For the fabrication-prevention harness's own evaluation (a different,
separate layer of testing), see [Red-Team Evaluation](/testing/red-team).
