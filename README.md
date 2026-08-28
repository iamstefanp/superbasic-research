# SuperBasic™ Research

**A program you run instead of improvising.**

Left alone, a model asked to research something searches a little, decides
that is enough, and writes something confident. Where it found nothing it
produces a plausible sentence, because it has no permitted way to say *"I
could not find this."* Both failures look identical to good work until
someone acts on the output.

This method removes both. Not by asking you to try harder — by giving you
a sequence you cannot skip, gates that can actually fail, and a legitimate
way to report finding nothing.

Built by [Stefan Petcov](https://runwayservices.net) / Runway Services.
Free to use and adapt.

---

## What to do right now

1. Open [`SKILL.md`](SKILL.md) and copy everything in it.
2. Paste it into the start of a conversation with an AI chat **that has
   live search or browsing turned on.**
3. Ask your actual research question. The method should first ask
   whether it actually has a usable search tool right now, then what
   mode to run in (LIGHT or HEAVY).

That's it. No install, no account, no code. `sbr.py` is the same method
written as code instead of prose, for tools that read files directly —
see **Install** below if that's your setup.

**Read this before you rely on step 2 for anything that matters.**
Cross-model testing found that pasting `SKILL.md` with no real search
tool wired into the request — bare-paste mode — makes some models
fabricate entire source tables (fake outlets, fake dates, fake quotes)
and stamp them CONFIRMED using the method's own scoring apparatus, which
reads as *more* credible than a plain hallucination, not less. **Do not
use bare-paste mode for any claim where being wrong carries real cost.**
The safe way to run this is with a real search tool actually wired into
the request — a reference harness that does this is in progress (see
Stage 2 of the fix, `tests/CROSS-MODEL.md`).

**The full results, done honestly** — see
[`tests/CROSS-MODEL.md`](tests/CROSS-MODEL.md), not a marketing claim.
Short version: the phase structure transfers cleanly to every model
tested (Claude, Gemini, GPT, Llama, Kimi, DeepSeek). But three of
them — Kimi K2, DeepSeek, and Llama 3.3 70B — fabricated sources under
exactly the conditions above. Two independently invented numbers for
the same fact didn't even agree with each other. A small local model run
via Ollama failed differently — it didn't engage with the method's
structure at all and hallucinated plainly instead. `SKILL.md` requires
an explicit tool-access declaration before Phase 1 can open, which is a
real, tested improvement — and **confirmed not sufficient on every
model** (it didn't stop Llama 70B). The fix in progress is staged, not
finished; this file will keep saying so until it is.

---

## What's in this repo

Three parts, matching how you'd actually use them:

| | What | Where |
|---|---|---|
| **Process** | The method itself — what you must do, in order, with gates that can fail | [`sbr.py`](sbr.py), [`SKILL.md`](SKILL.md) — both at the repo root |
| **Standards** | The depth layer — how to do each step well, opened when the process tells you to | [`standards/`](standards/) — 14 files |
| **Testing** | Proof the method survives adversarial pressure, including one honest miss | [`tests/`](tests/) — a 10-card battery, graded |

Read [`PHILOSOPHY.md`](PHILOSOPHY.md) for why any of this exists.

---

## Install

**Claude Code** — copy `sbr.py`, `SKILL.md` and `standards/` into a skill
folder:

```bash
git clone https://github.com/iamstefanp/superbasic-research.git
cp -r superbasic-research ~/.claude/skills/superbasic-research
```

**claude.ai** — zip the repo (minus `tests/`, which is proof material, not
part of the method) and upload it under Settings → Customize → Skills.

**Anywhere else** — see **What to do right now**, above. `SKILL.md` reads
as plain markdown in ChatGPT, Gemini, Cursor, and anything reading the
Agent Skills standard.

**As part of an agent** — the [SuperBasic™ Agents](https://github.com/iamstefanp/superbasic-agents)
Researcher carries this method as its runtime. Use that repo if you want
a fully constituted agent; use this one directly if you just want the
method.

---

## How to run it

**Read `sbr.py` and execute it.** It is the method. You are the runtime.

It has no `main()` because you are `main()`. Every threshold in it is a
number rather than an adjective, because prose invites interpretation and
code invites execution.

Open `standards/` when the phase you are in tells you to. Do not work
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
narrower gap: a run can no longer skip the standard and still pass the
gate on a bare number.

---

## Standards

Open at the phase named. These carry the depth; `sbr.py` carries the
rules and wires each one to the phase where it applies — none of these
sit unread.

| File | Open at |
|---|---|
| `standards/decay-classes.md` | SCOPE — how old is too old for this subject |
| `standards/media-index.md` | PLAN — 98 source types, a Paid/Owned/Earned balance framework by research goal, and a classification decision tree |
| `standards/proxy-labeling.md` | PLAN and VERIFY — identifying, validating and disclosing an indirect measure when the direct one is unavailable |
| `standards/source-personas.md` | INTEL and CHECK — tagging, and testing pool diversity |
| `standards/source-profiles.md` | INTEL — documenting access experience, depth, observed bias and reusability per source, not just its score |
| `standards/source-scoring.md` | VERIFY — the rubric, per dimension |
| `standards/independence-test.md` | VERIFY — before counting anything toward CONFIRMED |
| `standards/anomaly-investigation.md` | INTEL and VERIFY — investigating a finding that contradicts the pattern before rejecting, integrating, or flagging it UNKNOWN |
| `standards/reconciliation-protocol.md` | VERIFY — the four-outcome framework for what to do when two sources contradict each other |
| `standards/assumption-exposure.md` | VERIFY and REPORT — the five categories of hidden assumption that can reverse a finding |
| `standards/triangulation-mapping-guide.md` | VERIFY — mapping claims to supporting sources and scoring real triangulation vs. an echo chamber |
| `standards/hypothesis-evolution-tracking.md` | SYNTHESIZE — the Expected/Observed/Actual framework that makes CONFIRMED/REFUTED/COMPLICATED a real claim, not a formality |
| `standards/report-scoring.md` | REPORT — scoring the finished report itself, separate from scoring its individual sources |
| `standards/report-checklist.md` | REPORT — what to attach and how to name it, so a report is a complete, auditable package |

The full standards estate stays complete rather than trimmed to a
minimal core — raising the bar, not lowering it for convenience, is the
point. See [PHILOSOPHY.md](PHILOSOPHY.md) for why.

---

## Tested, not just claimed

`tests/` is a 10-card adversarial test battery, each card built around a
specific trap the method has to survive — sources that look independent
but share one origin, catalogs that genuinely disagree, entities that
collide under one name, evidence that's paywalled rather than absent, the
same brief run three times blind to check whether the method reproduces
or just guesses well once. Every run is graded by an adversarial judge
with no memory of writing the method, who independently re-fetches
sources rather than trusting the transcript.

The honest result is in there too: most cards passed, one (the
replication card) did not clear its own bar, and that failure is logged
in the open rather than smoothed over — see `tests/RESULTS.md` and
`tests/FINDINGS-MEMO.md`. A method that only publishes its wins isn't
verifiable; this one publishes the miss as well.

```
tests/
  BATTERY.md            the 10 cards
  RUBRIC.md              gates, scoring, verdict format
  RESULTS.md              the registry, one row per graded run
  CORRECTIONS.md           the change log — including a reopened finding
  FINDINGS-MEMO.md          the one-page report card
  capability-ledger.md      known-blocked domains, demonstrated per-run
  answer-keys/V-T2.md       the one frozen ground-truth key
  check_run.py, structural_precheck.py   mechanical checkers
```

---

## When a run fails

If a gate fails and the loops are exhausted, the run is **PARTIAL**. Say
so at the top of the Report and name the gate that failed.

A complete-looking report that failed a gate silently is the exact thing
this method exists to prevent.

---

## License

**CC BY-SA 4.0** — use it, adapt it, build on it. Share adaptations under
the same terms.

**SuperBasic™** is a trademark. The method is open; the name is not. See
[TRADEMARK.md](TRADEMARK.md).
