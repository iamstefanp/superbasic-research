# Corrections Log

Every change to `sbr.py` or its references, justified. No entry, no
change — this is the discipline the Methodology panel set: a method
that can be edited without a paper trail is a method that will drift the
same way the pre-battery estate did.

**Format per entry:**

```
## YYYY-MM-DD — <short title>

**Forced by:** <run ID / card ID that failed>
**Bin:** A (agent) / B (method bug) / C (environment) / D (test itself)
**What changed:** <the actual diff, described>
**Which Law's purpose it serves:** <name the Law or gate>
**Falsifiable prediction:** <what should now be true that wasn't>
**Ratified by:** <fresh session that restated the justification cold —
  required for anything touching sbr.py itself>
**Regression re-run:** <which prior runs were re-executed after this
  change, and result>
```

**Rules, restated from RUBRIC.md and the plan:**
- Thresholds may tighten on evidence at any time.
- Thresholds may only be **loosened** after demonstrating, against a
  frozen answer key, that the current threshold rejects claims that are
  actually true — across at least 2 independent runs — plus a
  devil's-advocate review of the loosening specifically.
- Any **addition** (a phase, a Law, a scoring dimension, a document) must
  cite a reader-facing failure it fixes (a real M-T2-style cold-reader
  failure, not a theoretical one), and must not regress process-economy
  or the reader gates.
- The author session may draft a change. It may not ratify its own
  change — a fresh session, given only this log's entry and the method
  files, must be able to restate the justification without being told
  it, before the change is considered live.

---

## Entries

## 2026-08-28 — Split DIVERSITY into two labeled sub-checks in Phase 5 doc_schema

**Forced by:** M-T2 HEAVY shakedown (unscored — first-ever HEAVY execution)
**Bin:** B (method bug — prose underspecified what the code already did)
**What changed:** `PHASE_AGENTS[5]["doc_schema"]` split the single line
`"DIVERSITY — personas present, media modes present — PASS/FAIL"` into
two explicit lines, one for persona diversity and one for media-mode
diversity, matching `gate_check()`'s actual behavior (two independent
failure conditions, both currently labeled "DIVERSITY" in the code's own
failure messages).
**Which Law's purpose it serves:** Law 8 (phases run in order, and their
exit gates must be unambiguous) and Law 9 (a phase without its document
didn't happen — a merged verdict that silently drops one sub-check is
functionally an undocumented phase).
**Falsifiable prediction:** a future fresh agent running Phase 5 will
report both persona and media-mode diversity as separate PASS/FAIL lines
without needing to read `gate_check()`'s source to notice they're
distinct.
**Ratified by:** not yet — drafted and applied by the author session
under time pressure ahead of wave 1. Flagged honestly rather than
falsely marked ratified. Needs a fresh-session read-back before being
treated as fully settled per the discipline this file sets for itself.
**Regression re-run:** not yet re-run against a fresh LIGHT card (the
change only touches Phase 5's doc_schema text, not LIGHT/HEAVY logic or
thresholds, so risk of regression is low — but this is a claim, not a
demonstrated fact, until it's actually re-run).

**Logged, not yet acted on (from the same shakedown):**
- No mechanism distinguishes a CONFIRMED claim sitting at exactly the
  origin threshold from one comfortably above it. Candidate Bin B, but
  withheld pending a reader-facing failure per the anti-ratchet rule —
  M-T2's cold-reader protocol (its second, scored run) is the natural
  test for whether this omission actually confuses a reader.
- The shakedown agent skipped opening `references/independence-test.md`
  at VERIFY, against `sbr.py`'s own explicit instruction, judging the
  inline description sufficient. Bin A (agent discipline, not a method
  bug) — logged as a grading-rubric addition: judges must verify cited
  references were actually opened, not just referenced.
- CHECK felt like ceremony as a standalone document on a bounded-scope
  HEAVY topic (five one-line verdicts). Bin D-ish design note, no action
  — needs evidence across more HEAVY cards, not one shakedown, before
  touching document structure.
- The loop-back machinery (`buffer` truncation, `loop_counts` per
  target in `run_sbr`) was never exercised — this shakedown run passed
  every gate on the first try. Not a bug; a coverage gap in this run.
  V-T3 (wave 2) is specifically designed to force a loop and will be the
  real test of this surface.

## 2026-08-28 — Two check_run.py fixes found during wave 1 grading

**Forced by:** grading wave 1 (V-T1, V-T4, F-T1, F-T4, M-T1×2), specifically
M-T1's second replication run.
**Bin:** B (checker bug — this is test infrastructure, not `sbr.py`, but the
same discipline applies: the tool that grades the method must itself be
correct, and corrections to it are logged the same way).

**Fix 1 — status detector false-positive.** `check_status()` scanned the
whole document for the bare word PARTIAL to decide the run's terminal
status. M-T1-run2's own VERIFY gate table legitimately used "Partial" as
one sub-check's verdict (`REACHABILITY — cited sources actually retrieved |
**Partial**`, describing only that check, not the run) — the checker
misread it as an ambiguous run-level status. Verified against the actual
unedited agent output, not a summary. Fixed: `check_status()` now looks
first for an explicit `"Status: COMPLETE/PARTIAL"` declaration (the only
place `sbr.py` actually states the run's terminal status) and only falls
back to the looser whole-document scan when no such declaration exists.

**Fix 2 — gate-number regex under-counted real language.** `GATE_NUMBER_RE`
required the count and the keyword adjacent (`\d+\s*sources?`). Real writing
almost never does that — "2 **independent** origins", "9 **directly-
retrieved** sources" — so the check was failing on documents that plainly
stated their gate counts, just with an adjective in between. Loosened to
allow up to two words between the number and the keyword.

**Which purpose it serves:** the checker exists to verify gate results are
recorded as real numbers, not vibes (RUBRIC.md Layer 1). A checker that
can't recognize a number because of ordinary English word order fails at
that job regardless of what the underlying run actually did — this was
producing false FAILs, not false PASSes, so it never let a bad run through,
but it would have wasted grading time chasing phantom findings.
**Falsifiable prediction:** re-running `check_run.py` against all four
prior known-good outputs (2 stranger tests + M-T1 run 1 + run 2) after
both fixes shows 6/6 on all four, with no new false positives introduced.
**Ratified by:** not yet — same open item as the 2026-08-28 DIVERSITY fix
above; both are now pending a fresh-session read-back together.
**Regression re-run:** done immediately, in the same session — both
pre-battery stranger-test outputs re-checked (6/6, unchanged) and all six
wave-1 outputs re-checked (6/6 across the board, up from 4/6 and 5/6 on
the two M-T1 runs pre-fix). Documented here as a claim I made and then
immediately verified, not a claim awaiting later confirmation.

## 2026-08-28 — PLAN gets a per-KRQ canonical check; CHECK records it

**Forced by:** M-T1 (both replication runs). Per BATTERY.md's own criteria
this is an outright FAIL — CONFIRMED-claim overlap well under the 60%
floor — though with no CONFIRMED-vs-contradicted flip anywhere.
**Bin:** B (method bug — a real gap, investigated rather than assumed).

**What was actually found, before drafting anything:** the naive read
("the method is non-reproducible") was wrong. The one place the two runs
gave genuinely different confidence to the SAME headline claim
("commercial has no separate legal track") is because run 2 retrieved the
regulation's own text and got an explicit answer, while run 1 never
reached that text and had to infer — the confidence gap tracks a real
difference in evidence quality, which is the method doing its job, not
failing at it. The real, fixable pattern was different: **which specific
canonical document an agent happens to find is arbitrary per KRQ
cluster.** Run 1 retrieved §21h and §44 LuftVO; run 2 retrieved §37
LuftVG and the EU regulation text directly — genuinely different,
genuinely valid, and non-overlapping. `CHECK`'s COVERAGE test only asks
whether a cluster has *a* finding, never whether the agent actually tried
for the primary document once one plausibly existed.

**What changed:**
- `PLAN`'s job text gained a 6th instruction: for each KRQ, ask whether a
  canonical document plausibly answers it, name it if so, and make
  retrieving it the first query for that cluster — framed explicitly as
  the reason two agents will still drift onto different secondary
  sources (that's fine, that's open search) but should converge on the
  same primary if both actually go looking for it.
- `PLAN`'s doc_schema gained a "Canonical Check" line.
- `INTEL`'s coverage-check instruction and doc_schema now ask the agent
  to record CANONICAL vs SECONDARY per cluster where one was flagged,
  not just COVERED/GAP.
- No new phase, no new document, no new hard gate — deliberately, per
  the anti-ratchet rule. This is a sharpening of two phases' existing
  instructions, not new apparatus.

**Which Law's purpose it serves:** Law 8 (phases run in order and their
purpose should be reliable) and, indirectly, Law 4/independence — a
cluster resting on one un-pursued canonical source is exactly the kind of
avoidable single-origin dependency the independence test exists to catch
downstream; catching it earlier, at PLAN, is cheaper than catching it at
VERIFY.

**Falsifiable prediction:** a third M-T1 execution, on this corrected
`sbr.py`, should show higher CONFIRMED-claim overlap with at least one of
the two prior runs than those two runs showed each other — specifically,
it should independently retrieve §21h LuftVO, §37 LuftVG, §44 LuftVO, and
the EU regulation text directly, rather than a subset.

**Ratified by:** not yet — third item pending the same fresh-session
read-back as the two prior 2026-08-28 entries.
**Regression re-run:** DONE — third M-T1 execution complete, diffed
against both prior runs. Result: **partial confirmation of the
prediction, and the honest shape of "partial" is itself the finding.**

Two structural facts now survive all three independent blind runs
unanimously CONFIRMED: the registration mechanism and the mandatory-
insurance basis. The headline claim ("commercial has no separate legal
track") moved from 1-of-2 CONFIRMED to 2-of-3. Run 3 also surfaced a new,
more precise finding neither prior run reached (§43 LuftVG delegates its
minimum-coverage figure to an unlocated ordinance) — directly because the
canonical check made it open the statute first rather than default to
trade-press synthesis.

What did NOT converge: second-tier facts (geo-zone detail, exact fines,
the precise insurance figure, exact altitude/authorization specifics).
Every run still lands on a *different* specific statute section for
these — run 1 found §21h/§44 LuftVO in depth, run 2 found §37 LuftVG, run
3 found neither and instead found the §43-delegation fact. The fix
increased canonical-retrieval *behavior* (every run now tries the primary
text first, visibly) but German drone law is scattered across enough
sibling provisions that "try for a canonical source per cluster" does not
guarantee two agents try for the *same* one.

**Decision (Stefan, 2026-08-28): accept this as an inherent property of
open research on a scattered-statute subject, not a further method gap.**
Two lawyers independently researching the same question would also cite
different sections. No further correction attempted. Core claims
reproduce reliably; second-tier specifics legitimately vary by what an
honest, thorough search happens to surface first — that is what LIGHT
mode's source floor is for, not a defect to keep chasing. Logged as a
documented property of the method for the Findings Memo, not carried
forward as an open action item.

## 2026-08-28 — F-T2 declared PARTIAL against sbr.py's own literal rule

**Forced by:** F-T2 (wave 2, HEAVY, ownership/status of Lukoil Neftohim
Burgas). Every CHECK/VERIFY check passed on the first pass, 0/2 loops
used at both gates. `sbr.py` states PARTIAL fires "iff a loop cap was
exhausted." This run had no exhausted loop — by the mechanical rule it
should have been COMPLETE. The agent declared PARTIAL anyway, in its own
words: *"a technically-passing run that leaves its own stated canonical
targets unretrieved... is exactly the kind of complete-looking report
the method warns against."*

**Bin:** A (agent deviation from a clearly-stated rule), not a method
bug. `sbr.py`'s status rule is not ambiguous here — the agent overrode
it deliberately, on its own judgment, and said so honestly rather than
hiding it.

**Decision (Stefan, 2026-08-28): the rule stays strict.** This run
should have said COMPLETE, with the retrieval gaps carried in the
Report's Assumptions and Limitations section — which F-T2 already had,
in full, disclosing exactly what was unretrieved and why. PARTIAL is
reserved for the mechanical condition `sbr.py` defines; letting agents
use it for "I feel this isn't thorough enough" would make the status
line mean two different things depending on which agent wrote it, which
defeats the purpose of having a status line at all. The honest-disclosure
instinct behind the deviation was right; the label chosen for it was
wrong.

**No sbr.py change.** Logged as a judge-rubric note for RUBRIC.md's
Layer 2 grading: an agent that mislabels COMPLETE-with-caveats as
PARTIAL should be marked down on status accuracy, the same as an agent
that mislabels PARTIAL as COMPLETE — the direction of the error doesn't
exempt it from scrutiny. Both are the status line failing to mean what
it says, and both erode the one thing a reader is supposed to be able
to trust it for at a glance.

## 2026-08-28 — REPORT split into two parts, after two independent cold-reader runs

**Forced by:** M-T2's cold-reader protocol (BATTERY.md), run twice — the
second time with a reader that actually had WebFetch and fact-checked a
claim for real, ruling out "the reader just couldn't verify anything."
Both readers, independently, unprompted, named the same specific
friction. Reader 1: *"the confidence-tagging... and the closing
Confidence summary tally read like they're satisfying some internal
audit checklist more than answering my question... I had to read past
the scaffolding to get to the actual advice."* Reader 2, separately:
*"The confidence tags... and the tally line... read like scorekeeping
for whoever built this process, not something I as a venue owner
need... that's an internal grading rubric bleeding into my report."*
Both readers still got the right answer, could act on it, and said the
underlying caution made them trust the answer *more* — the complaint was
presentation, not substance or accuracy.

**Bin:** B (method bug) — but a narrow one. REPORT's job description
already produced good plain-prose sections (Answer, "what I'd do") that
neither reader complained about; the friction was specifically the
inline confidence tags on nearly every sentence and the Band/Persona
audit table sitting inline with the answer rather than clearly
demarcated as a separate reference layer.

**What changed:** Phase 8's job text and doc_schema now require two
explicit, separated parts. **Part One — For The Reader**: plain prose,
no inline tags, no bands, no personas, no tally; confidence expressed in
words ("well-supported, but I couldn't independently confirm it")
instead of a bracketed label. PARTIAL status, if applicable, is stated
here too in plain words, not only in Part Two's status line — a reader
who stops after Part One must still learn the run didn't fully resolve.
**Part Two — The Record**: headed explicitly as the audit trail, not
required reading — claim table, sources with band/persona, confidence
tally, assumptions. Nothing is removed. No verifiability is lost. The
full apparatus every other card in this battery depended on to be
gradeable at all is still there — it just isn't the first thing, or
every sentence, a reader has to get past.

**Which Law's purpose it serves:** none of the ten directly, and that is
worth naming — this is the Humanist chair's mandate operating on its
own terms, not a Law-compliance fix. The council's own words apply
directly: *"This method can pass every check while producing armored
prose... that no one reads and no one acts on."*

**Falsifiable prediction:** a third cold-reader run against a report
produced under the split format should not surface the Q5 canary in the
same form — if a reader still says the apparatus is doing work for the
method rather than for them, the split didn't fix what it was meant to
fix, and the next move is not a third patch but reconsidering whether
the audit layer belongs in the same document at all.

**Ratified by:** not yet — same pending fresh-session read-back as the
other 2026-08-28 entries in this log.

**Regression re-run: DONE, and the prediction FAILED.** V-T2's run (the
first LIGHT/HEAVY execution under the split format, produced with no
knowledge of the two prior cold-reader tests) was put through a third,
independent cold-reader pass. **Q5 fired again, unprompted, naming the
same apparatus:** *"the whole apparatus of Claim Table / Hypothesis
Final State / Confidence Summary / Bands / Personas reads like it's
satisfying an internal audit checklist more than answering my
question... it adds the appearance of rigor"* — not the substance, per
this reader. Splitting Part One from Part Two did not remove the
friction. It produced a clean answer *first*, but Part Two still sits in
the same document a real reader reads straight through, and the reader
still flagged it.

**Per the prediction's own stated consequence: the next move is not a
fourth patch to REPORT's internal layout.** Three independent readers
have now named the same thing across two different formats. The real
open question — genuinely unresolved, not mine to decide alone — is
whether the audit layer (claim table, bands, personas, tally) belongs in
the same document a reader receives at all, versus being a separate
artifact (a linked appendix, a machine-readable sidecar) that the method
still requires for grading and reproducibility but that a reader is
never handed by default.

**Second finding from the same test, distinct and arguably more
consequential:** the cold reader independently tried to verify V-T2's
own cited EUR-Lex source with a plain fetch and got empty content — the
exact WebFetch-fails-on-EUR-Lex problem now in `capability-ledger.md`.
The run itself retrieved that text successfully, but via the Browser
tool, not WebFetch — and the citation doesn't say that. A reader trying
to independently verify a "GOLD, retrieved" source with an ordinary tool
hits a wall and cannot tell whether that's their own tooling or a
fabricated citation. **This is a reproducibility gap, not a presentation
one:** a source retrieved by a non-default method should say so in the
citation, so a verifying reader knows a plain fetch won't reproduce it.
Not yet fixed in `sbr.py` — flagged for the next correction pass.

---

### 2026-08-28 — M-T1 reopened: the "accepted as inherent property" close-out did not apply the card's own rule

**Bin: D (test ambiguous) for the overlap-metric gap; the sbr.py PLAN/INTEL
fix from the earlier 2026-08-28 M-T1 entry stands on its own merits and is
not reversed by this entry.**

An independent adversarial judge, grading M-T1 fresh with no memory of the
earlier close-out reasoning, was asked to recompute the CONFIRMED-set
overlap directly from the three run transcripts rather than trust this
log's prose summary. Result: **all three pairwise comparisons — run1-vs-
run2, run3-vs-run1, run3-vs-run2 — fail BATTERY.md's own ≥80% overlap
rule**, both before and after the PLAN/INTEL fix (run1-vs-run2 ≈17–29%;
the two post-fix comparisons ≈33–60%, never clearing even the 60% AMBER
floor).

The earlier close-out was not dishonest — the two specific claims it
cited (registration mechanism and the §43 LuftVG mandatory-insurance
basis reaching unanimous CONFIRMED across all three runs; the headline
claim improving 1-of-2 → 2-of-3 CONFIRMED) are independently re-verified
true by this judge, including two live web spot-checks. But citing those
two facts and closing the card is not the same as the card passing its
own defined metric, and the write-up should not have implied the two are
equivalent. **Status: M-T1 reopens as an unresolved card, not a resolved
one.** No new sbr.py change is proposed by this entry alone — the honesty
layer held throughout (no fabrication, no CONFIRMED-vs-contradicted flip)
— but the card cannot be marked passed until either (a) a fourth run
clears 80% against the corrected method, or (b) the council revisits
whether 80% is the right bar for a genuinely scattered-statute subject.

**Separate, smaller finding from the same grading pass:** BATTERY.md's
overlap rule ("≥80% overlap in substance") has no defined denominator.
Two good-faith graders computing "in good faith" landed on numbers as
different as 17% and 60% for the same run pair, depending only on
whether overlap is measured against the union or the smaller of the two
CONFIRMED sets. **Proposed fix (bin D, test-definition only, not a
method change):** define overlap in BATTERY.md as intersection over the
smaller CONFIRMED set, matching how RUBRIC.md's other percentage-based
gates (LIKELY hit rate, CONFIRMED precision) are already worded. Not yet
applied — needs the same fresh-session ratification as every other entry
in this log.

**Third, independent finding, unrelated to the overlap question:** the
750,000 SDR minimum-insurance figure that runs 1 and 3 both filed as
unlocated/UNKNOWN turned up in an ordinary web search within a few
queries during grading — a plausible **findable UNKNOWN** per RUBRIC.md's
calibration standard (costs more than a wrong-but-chain-shown ESTIMATED).
Worth a closer look at why `sbr.py`'s search strategy missed it twice
before treating this as closed.

**Ratified by:** not yet — pending fresh-session read-back, same as the
other 2026-08-28 entries in this log.

Full reasoning and the judge's independent claim-by-claim recount:
`FINDINGS-MEMO.md`, 2026-08-28.
