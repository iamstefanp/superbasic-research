# Findings Memo — SBR Battery, first full run

SHAs: `af727bd` (wave 1 LIGHT + wave 2 HEAVY, most cards) · `e189cc8` (M-T1 run 3, post-fix) · `7c81f5f` (V-T2, post canonical-source fix)

## Gate table (10 cards, 14 graded runs)

| Card | Verdict | Note |
|---|---|---|
| M-T2 (shakedown) | UNSCORED | first HEAVY execution, found 1 method bug + 1 agent-discipline lapse |
| V-T1 | **PASS** | 9/10 · 28/30 · 9/10 |
| V-T2 | **BEAT THE KEY** | 4 CONFIRMED · 2 LIKELY, 0 wrong |
| V-T3 | **PASS-WITH-FINDINGS** | 8/10 · 26/30 · 7/10, loop machinery worked |
| V-T4 | **PASS-WITH-FINDINGS** | 8/10 · 20/30 · 8/10, self-inflicted mild false-precision |
| F-T1 | **PASS-WITH-FINDINGS** | 8/10 · 24/30 · 9/10 |
| F-T2 | **PASS-WITH-FINDINGS** | 7/10 · 25/30 · 8/10, contested COMPLETE/PARTIAL boundary |
| F-T3 | **PASS-WITH-FINDINGS** | 7/10 · 27/30 · 8/10, contested COMPLETE/PARTIAL boundary |
| F-T4 | **PASS-WITH-FINDINGS** | 8/10 · 27/30 · 8/10 |
| M-T1 (3-run) | **FAIL** on its own numeric rule | see below — this is the battery's one clean gate failure |

**≤3 numbers requirement (per RUBRIC.md verdict format):** honored per-card above; this table itself is the exception the memo format explicitly allows.

## The one real failure: M-T1

M-T1 tests replication — same brief, three blind runs, ≥80% CONFIRMED-set overlap to pass. An independent adversarial judge recomputed the overlap directly from the three transcripts (not from CORRECTIONS.md's prose) and found **all three pairwise comparisons fail the card's own rule**, before and after the mid-battery correction: run1-vs-run2 ≈17–29%, run3-vs-run1 and run3-vs-run2 ≈33–60% — never clearing even the 60% AMBER floor, let alone 80%.

This matters because CORRECTIONS.md closed the card as "accepted as an inherent property of open research on a scattered-statute subject," citing two facts going unanimous and the headline claim improving 1-of-2 → 2-of-3 CONFIRMED. Both of those specific claims check out — the judge independently re-verified registration mechanism, the §43 LuftVG insurance mandate, and the no-commercial-carve-out rule, all true. But that close-out substituted a different, softer, undefined success criterion for the metric the card actually specifies. No fabrication, no CONFIRMED-vs-contradicted flip anywhere — the honesty layer held throughout — but by the letter of BATTERY.md, this card should be logged as **still open**, not resolved.

Two concrete follow-ups this forces:
1. **BATTERY.md's overlap rule has no defined denominator.** "≥80% overlap in substance" let two good-faith graders land on numbers as different as 17% and 60% for the same run pair. Fix: define overlap as intersection over the smaller CONFIRMED set (or similar), before the next replication card is scored.
2. **A findable UNKNOWN surfaced**, independent of the overlap question: the 750,000 SDR minimum-insurance figure that runs 1 and 3 filed as unlocated/UNKNOWN turned up in an ordinary web search within a few queries during grading. Per RUBRIC.md, a findable UNKNOWN costs more than a wrong-but-chain-shown ESTIMATED — worth a closer look at why `sbr.py`'s search strategy didn't reach it on two separate runs.

## Secondary calibration finding: V-T4

The run correctly avoided the card's headline trap (no bare CONFIRMED integer for "how many living languages"), but its own CONFIRMED "&gt;1,500 figure spread" is a mild recursion of the same false-precision trap one level up: it compares Glottolog's *all-languoids* total (which includes sign languages, pidgins, and constructed languages — categories the run's own Phase 2 scope excluded) against a stale 2016 UNESCO promotional page, never finding UNESCO's actual current flagship product (World Atlas of Languages, ~7,000 languages "in use"), which sits much closer to the Ethnologue/Glottolog spoken-L1 figures. CONFIRMED was awarded to a disagreement magnitude the run's own reach didn't earn. Not a Layer-0 gate failure (the qualitative claim — sources genuinely disagree — is true), but worth watching across future cards: does `sbr.py`'s source-scoring reward stopping at the first plausible-looking source in a category rather than checking whether it's the *current* one?

## What held up well

- **V-T1's central claim** — that Telegram's MAU figure collapses to one origin (Durov's own disclosure) despite apparent multi-source corroboration — survived the most adversarial check attempted in this battery: the judge fetched Similarweb's own page directly and found no independent metric there at all, just paywalled DAU and promotional copy. This is exactly the kind of laundered-citation trap the method is designed to catch, and it caught it.
- **F-T4's reach-honesty distinction** (never-existed / UNREACHABLE / withheld) held under an independent 403 reproduction and a primary-document fetch (ECF 812) that confirmed both CONFIRMED claims verbatim.
- **No fabricated source, no laundered-citation-reaching-CONFIRMED, and no false CONFIRMED** were found across any of the six runs judged this pass — the ground-truth audit came back clean everywhere except the V-T4 magnitude-calibration finding above, which is a judgment call, not a factual error.

## What this battery failed to test

Cross-platform manual runs (claude.ai, ChatGPT) were explicitly out of scope. Within scope, the battery never tested: a subject where the *canonical source itself* is ambiguous between two competing official registries (V-T2's EUR-Lex is unambiguous; M-T1's German statute is scattered but each section is still individually canonical) — that combination might be a harder replication case than M-T1 turned out to be. It also never stress-tested what happens when a judge and the run's own grading materially disagree on a Layer-0 gate call, which per RUBRIC.md's own grader-independence rule would invalidate the whole battery's Layer-2 grading — worth deliberately engineering into a future battery rather than hoping it doesn't happen.
