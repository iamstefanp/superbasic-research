# The Eight Phases

```
BRIEF → SCOPE → PLAN → INTEL → CHECK → VERIFY → SYNTHESIZE → REPORT
                         ↑        │        │
                         └────────┴────────┘
                           the two legitimate loops
```

| # | Phase | What happens |
|---|---|---|
| 1 | **BRIEF** | The question, the hypothesis, the clusters. Lock the mode. |
| 2 | **SCOPE** | Bound the territory. What is out. How old is too old. |
| 3 | **PLAN** | Name the sources. Write the queries. Map them to clusters. |
| 4 | **INTEL** | Search. Capture, do not analyse. Log what you did not find. |
| 5 | **CHECK** | Is the pool sufficient? Count, coverage, diversity. GO or back. |
| 6 | **VERIFY** | Score every source. Test independence. Assign confidence. |
| 7 | **SYNTHESIZE** | Observe, analyse, create. What did the hypothesis do? |
| 8 | **REPORT** | Answer the question. Show the evidence. Disclose the gaps. |

Order is not negotiable. Most research fails not because of bad sources but
because of bad sequencing — SCOPE bounds the ground, PLAN picks the route
across it, and you cannot plan a route across unbounded ground.

**Looping back is the process working, not failing.**

## Standards are enforced, not just requested

`sbr.py`'s exit gates don't just check the numbers a run reports — they
check whether the standard behind those numbers was actually applied:

- A source's score has to come with a full per-dimension breakdown that
  sums to the total — not a number chosen first and reverse-fitted.
- Persona and media-mode tags are checked against the real twelve-persona
  taxonomy and Paid/Owned/Earned, not accepted as any two distinct strings.
- Every source needs a stated `origin_trace` — how independence was
  actually established, not just a bare `origin` label standing in for
  work that was never done.

None of this can verify the underlying judgment was good. It closes the
narrower gap: a run can no longer skip the standard and still pass the gate
on a bare number.
