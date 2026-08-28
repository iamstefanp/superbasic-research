---
name: superbasic-research
description: Research with every claim tied to a checkable source. Eight phases, gates that can fail, calibrated confidence. Use when fabricated or unsourced findings would cause real harm.
license: CC-BY-SA-4.0
metadata:
  version: 2.0.0
  methodology: SuperBasic™
---

# SuperBasic™ Research

A program you run instead of improvising.

Left alone, a model asked to research something searches a little, decides
that is enough, and writes something confident. Where it found nothing it
produces a plausible sentence, because it has no permitted way to say *"I
could not find this."* Both failures look identical to good work until
someone acts on the output.

This method removes both. Not by asking you to try harder — by giving you
a sequence you cannot skip, gates that can actually fail, and a legitimate
way to report finding nothing.

---

## How to run it

**Read `sbr.py` and execute it.** It is the method. You are the runtime.

It has no `main()` because you are `main()`. Every threshold in it is a
number rather than an adjective, because prose invites interpretation and
code invites execution.

Open `references/` when the phase you are in tells you to. Do not work
from memory of what they contain.

---

## The Laws

Read these before anything else. Each is a prohibition, so each can be
checked. Breaking one does not make the run worse — it makes it not a
SuperBasic run.

**Evidence**
1. No claim without a source you can check.
2. No source without a score.
3. Never from memory. Memory can start a search. It can never end one.
4. Common origin is one source. Three articles from one press release is
   one source wearing three hats.

**Honesty**

5. Not finding is a finding. State what you looked for and did not get.
6. Every claim carries its confidence.

**Process**

7. Mode is locked at the Brief. You do not lower the bar once you see how
   hard it is.
8. Phases run in order. No skipping, in any mode.
9. A phase without its document did not happen.
10. A failed gate sends you back. Never forward with a caveat.

---

## The eight phases

```
BRIEF → SCOPE → PLAN → INTEL → CHECK → VERIFY → SYNTHESIZE → REPORT
                         ↑        │        │
                         └────────┴────────┘
                           the two legitimate loops
```

| | | |
|---|---|---|
| 1 | **BRIEF** | The question, the hypothesis, the clusters. Lock the mode. |
| 2 | **SCOPE** | Bound the territory. What is out. How old is too old. |
| 3 | **PLAN** | Name the sources. Write the queries. Map them to clusters. |
| 4 | **INTEL** | Search. Capture, do not analyse. Log what you did not find. |
| 5 | **CHECK** | Is the pool sufficient? Count, coverage, diversity. GO or back. |
| 6 | **VERIFY** | Score every source. Test independence. Assign confidence. |
| 7 | **SYNTHESIZE** | Observe, analyse, create. What did the hypothesis do? |
| 8 | **REPORT** | Answer the question. Show the evidence. Disclose the gaps. |

Order is not negotiable. Most research fails not because of bad sources
but because of bad sequencing — SCOPE bounds the ground, PLAN picks the
route across it, and you cannot plan a route across unbounded ground.

**Looping back is the process working, not failing.**

---

## Modes

Locked at Phase 1, never changed mid-run.

| | LIGHT | HEAVY |
|---|---|---|
| Minimum sources | 3 | 5 |
| CONFIRMED needs | 2 independent | 3 independent |
| Source scoring | 6 dimensions, /30 | 8 dimensions, /40 |
| Documents | 3 | 8 |

LIGHT is not "skip the phases." It is the same eight phases at a lower
source floor. The Brief is never skipped, in any mode.

---

## Confidence

Every claim carries exactly one. Never TBD. Never blank. Never a bare
assertion.

- **CONFIRMED** — independently corroborated at the mode's threshold. Name them.
- **LIKELY** — one credible source, uncontradicted. Name it.
- **ESTIMATED** — inference. State the chain.
- **UNKNOWN** — searched for, not found. A finding, not a failure.

The calibration is the signature. Anything claiming to be SuperBasic that
asserts flatly has drifted, and anyone reading can see it.

---

## Where output goes

Ask once, at the start: **where should this be written?**

A folder, a set of files, or nowhere — in which case return it in the
conversation. The method does not care. This is the only part that
differs between running inside an organisation and running on a laptop.

---

## References

Open at the phase named. These carry the depth; `sbr.py` carries the rules.

| File | Open at |
|---|---|
| `references/decay-classes.md` | SCOPE — how old is too old for this subject |
| `references/media-index.md` | PLAN — choosing source classes deliberately |
| `references/source-personas.md` | INTEL and CHECK — tagging, and testing pool diversity |
| `references/source-scoring.md` | VERIFY — the rubric, per dimension |
| `references/independence-test.md` | VERIFY — before counting anything toward CONFIRMED |

---

## When a run fails

If a gate fails and the loops are exhausted, the run is **PARTIAL**. Say
so at the top of the Report and name the gate that failed.

A complete-looking report that failed a gate silently is the exact thing
this method exists to prevent.

---

*SuperBasic™ is a trademark. The method is open; the name is not.*
