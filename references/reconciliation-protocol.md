# Reconciliation Protocol

## Opening Definition

**What is Reconciliation?** Reconciliation is the process of deciding
what to do when two or more sources contradict each other during
research. It is not about averaging away disagreement. It is not about
hiding the contradiction. Reconciliation is a deliberate decision
framework that asks: *Which source is more reliable?* *Do both claims
belong in the report as tension?* *How do I document this choice?*

Reconciliation happens in the **VERIFY phase** ("Reconcile anomalies:
contradictory claims → how do we resolve?"). It feeds three downstream
outputs:

1. **Reconciliation Record** — the decision log showing which
   contradiction you resolved and how
2. **Synthesis** — where contradictions often reveal deeper complexity
   (tensions as evidence)
3. **Research Report** — formal findings tier, where contradictions are
   disclosed honestly

The core principle: **Transparency beats consensus.** If two credible
sources disagree, the reader deserves to know. Your job is not to smooth
it over — it is to explain *why* the disagreement exists and what it
means.

---

## Why Contradictions Matter

Contradictions are not research failures. They are signals. A
contradiction often reveals:
- **Different scopes** — Company says "no layoffs" (official) vs.
  insider says "restructuring" (happening now). Both true, different
  time horizons.
- **Conflicting incentives** — Competitor's press release vs. industry
  insider's assessment. One side has incentive to understate, the other
  to exaggerate.
- **Real disagreement** — Two credible experts genuinely disagree. This
  is important information, not noise.
- **Data quality** — One source collected data more rigorously than the
  other.

Reconciliation forces you to *understand* the contradiction, not ignore
it. That understanding is often the most valuable part of your research.

---

## Decision Framework: Four-Step Reconciliation Process

When you identify a contradiction during VERIFY, follow this flow:

### Step 1: Assess Source Reliability (Both Sides)

For Source A and Source B:
- **Reliability Score** — Use the standard source-scoring dimensions
  (see `source-scoring.md`)
- **Source Tier** — Gold (triangulated, 2+ sources) / Silver (single
  source, cross-referenced) / Bronze (inference, partial)
- **Persona Type** — Consult `source-personas.md`
- **Independence** — Are these sources making claims independently, or
  is one amplifying the other? (If both cite the same underlying fact,
  that's one source, not two.)

**Critical question:** Is the disagreement between independent sources,
or are both reporting the same underlying data?

### Step 2: Identify the Actual Disagreement

State the contradiction explicitly. Do not paraphrase into vagueness.

- **Source A claims:** [Direct quote or precise paraphrase]
- **Source B claims:** [Direct quote or precise paraphrase]
- **The disagreement:** [What exactly contradicts? Tone? Magnitude?
  Timing? Scope?]

Common false contradictions (where the disagreement disappears on closer
reading):
- **Different time periods** — Both true, different cycles.
- **Different scope** — "UK sales rose" vs. "Global sales fell." Both
  true, different markets.
- **Different populations** — "Engineers hired" vs. "Headcount fell."
  Both true, different departments.
- **Tone vs. fact** — "Aggressive growth" (optimistic frame) vs. "market
  saturation pressure" (cautious frame). Facts may not contradict, only
  interpretation.

Reframe if the disagreement dissolves when scopes are clarified. If it
doesn't, move to Step 3.

### Step 3: Decide the Outcome

Once you have assessed both sources and clarified the actual
disagreement, pick one of four outcomes:

#### Outcome 1: WINNER CLEAR
One source is materially more reliable than the other.
- **When to use this:** Reliability scores differ substantially, or one
  source is Gold and the other is Bronze.
- **Action:** Cite the reliable source. Note the contradiction in
  Assumptions and Limitations (transparency).
- **Rationale example:** "Analyst report vs. LinkedIn comment. Winner
  clear. Cite analyst. Mention contradiction in limitations."

#### Outcome 2: BOTH VALID
Both sources are credible, but they describe different perspectives on
the same reality.
- **When to use this:** Both sources score similarly. Disagreement
  reflects different vantage points (insider vs. public, short-term vs.
  long-term, optimistic vs. cautious).
- **Action:** Present both claims as a **tension** in your synthesis.
  Frame it as complexity, not contradiction.
- **Rationale example:** "Company says 'stable margins' (IR
  perspective). Competitor says 'margin pressure' (market perspective).
  Both credible, different angles. Both in report as tension."

#### Outcome 3: UNRESOLVABLE
You cannot determine which source is more reliable. The disagreement
cannot be settled with available evidence.
- **When to use this:** Sources score similarly, but the disagreement is
  not about perspective — it is about fact (one is objectively wrong).
  You have no third source to break the tie.
- **Action:** Flag the claim as **UNKNOWN confidence**. Disclose the
  disagreement and note that you cannot resolve it.
- **Rationale example:** "Board size: Company says 7, filing says 9.
  Both appear official. No third source. Mark as UNKNOWN."

#### Outcome 4: REFRAMING
The apparent contradiction dissolves when you understand the context
more deeply.
- **When to use this:** Step 2 analysis reveals that the sources
  actually agree but use different language, or that the disagreement is
  semantic rather than factual.
- **Action:** Explain the reframing in your report. No longer a
  contradiction.
- **Rationale example:** "Competitor A announced 'layoffs' (50 people).
  Insider said 'restructuring' (same 50 people, reassigned). Same event,
  different framing. Reframe as reorganization, not layoff."

---

## Reconciliation Outcomes — Quick Reference

| Outcome | Use When | Action | Report Placement | Disclosure |
|---------|----------|--------|------------------|------------|
| **WINNER CLEAR** | Reliability scores differ substantially, or Gold vs. Bronze | Cite reliable source, note contradiction | Assumptions and Limitations | "Some sources claimed X, but [reliable source] shows Y" |
| **BOTH VALID** | Scores similar, reflects different perspectives | Present as tension in synthesis | Findings section with tension framing | "X is contested between [camps]. Both perspectives have merit." |
| **UNRESOLVABLE** | Scores similar, but one side is objectively wrong (unknown which) | Flag as UNKNOWN confidence | Findings + Limitations | "Claim X is disputed. Evidence insufficient to resolve. Treated as UNKNOWN." |
| **REFRAMING** | Apparent contradiction dissolves with context | Explain reframing, remove from contradictions | Incorporate into narrative | "Apparent contradiction resolved: [explanation]" |

---

## Reconciliation Record Template

For every contradiction you identify, complete a Reconciliation Record.
This becomes your audit trail and feeds directly into VERIFY phase
documentation.

| Claim | Source A Says | Source B Says | Source A Score | Source B Score | A Tier | B Tier | Independence Check | Outcome | Rationale | Report Placement | Status |
|-------|---------------|---------------|-----------------|-----------------|--------|--------|------------------|---------|-----------|-----------------|--------|
| [Name the claim being disputed] | [A's exact statement or quote] | [B's exact statement or quote] | [score] | [score] | [Gold/Silver/Bronze] | [Gold/Silver/Bronze] | [Independent? Yes/No/Partial] | [WINNER/BOTH/UNRESOLVABLE/REFRAME] | [Why this outcome?] | [Where in final report?] | [RESOLVED/FLAGGED/PENDING] |

### Example Entry

| Claim | Source A Says | Source B Says | Source A Score | Source B Score | A Tier | B Tier | Independence | Outcome | Rationale | Report Placement | Status |
|-------|---------------|---------------|-----------------|-----------------|--------|--------|--------------|---------|-----------|-----------------|--------|
| Q1 headcount | "Headcount grew 3%" (Quarterly earnings call, CFO statement) | "Headcount flat, cost cuts masked growth" (Glassdoor insider reviews, 8 entries) | High | Low | Gold | Bronze | Independent (company data vs. employee perception) | WINNER CLEAR | CFO has access to actual payroll data. Employee perception is retrospective and may confuse hiring cycles with restructuring. Cite company data. | Assumptions and Limitations: "Employee reviews suggested flat headcount; official filings show 3% growth, consistent with normal hiring variance." | RESOLVED |

---

## Reliability Scoring Recap (for Reconciliation)

When reconciling, the source-scoring dimensions (see `source-scoring.md`)
are your primary tool: Proximity, Recency, Verifiability, Independence,
Specificity, Track Record (plus Clarity and Expertise on HEAVY). Score
both sides of a contradiction independently before deciding an outcome.

---

## Common Mistakes in Reconciliation

| Mistake | Example | Why It's Wrong | Correction |
|---------|---------|----------------|-----------|
| **Averaging away disagreement** | "One source said 10%, another said 20%, so the truth is 15%." | Averaging assumes both sources are equally reliable and measuring the same thing. Often they're not. | Score both sources. If unequal, cite the stronger one. If equal and measuring different things, present both as perspective. |
| **Hiding the contradiction** | Omit Source B's contradicting claim from the report entirely. | Lack of transparency. Reader doesn't know a contradiction exists. | Disclose all contradictions. Explain why you chose one over the other. |
| **Treating all sources as equally reliable** | "Two sources disagree, I'll just mention both and let the reader decide." | Abdication of research responsibility. | Score both. Explain the scoring logic. Guide the reader toward the more reliable source. |
| **Not documenting rationale** | Pick an outcome but don't explain why. | Future readers won't understand the decision. | Complete the Reconciliation Record fully. |
| **Overstating reframing** | Claiming sources agree when they actually contradict. | Misses real disagreement. | Use reframing only when the disagreement actually dissolves. Test: if both claims are simultaneously true, it's reframing. If one must be false, it's a real contradiction. |
| **Confusing scope with contradiction** | Treating different-scope claims as contradictory. | Wastes reconciliation effort on false problem. | Always ask: Are these sources measuring the same thing? Same time period? Same population? |
| **Citing weak sources to avoid contradiction** | Picking the weaker source because it fits a narrative. | Undermines the whole reliability framework. | Score objectively. Let scoring guide the decision. |
| **Unresolved contradictions in final report** | Present both sides without flagging as UNKNOWN. | Reader thinks you couldn't decide, not that the evidence is genuinely insufficient. | Explicitly mark unresolvable contradictions as UNKNOWN confidence. |

---

## Persona Types (for Independence Assessment)

When reconciling, check whether sources are independent using the twelve
personas in `source-personas.md`. **Independence rule:** If both sources
are the same persona type *and* they likely know each other (same
organization), they are **not independent**. Count as one source. If
they're different personas, or the same persona at different
organizations, they are **independent**.

---

## Practical Workflow: Reconciliation in VERIFY Phase

### Step 1: Identify All Contradictions
Pull every claim flagged as a contradiction during INTEL. If not already
flagged: read through all source notes side-by-side, cross-reference key
claims, and create a contradiction list (later becomes your
Reconciliation Record).

### Step 2: Clarify the Disagreement
For each contradiction, state exactly what disagrees. **Test:** Can both
claims be true? If yes, it's not a contradiction (reframe). If no, it's a
real contradiction (move to Step 3).

### Step 3: Score Both Sources
Score each source in the contradiction independently. Record scores in
the Reconciliation Record.

### Step 4: Assess Independence
Are the sources making claims independently, or does one depend on the
other? If Source B is just quoting or amplifying Source A, treat them as
**one source** (Source A + echo).

### Step 5: Decide Outcome and Rationale
Use the four outcomes. Record the decision and explain *why*.

### Step 6: Determine Report Placement
For each contradiction, decide where it appears in the final report.
Complete the Reconciliation Record status as **RESOLVED**.

---

## Full Example: Multi-Claim Reconciliation

**Scenario:** You are researching a music festival's attendance and
artist compensation. You have two sources that contradict on multiple
dimensions.

**Source A:** Official press release from festival organizers
- "Attended by 45,000 music fans"
- "Paid artists a combined $2.8M in artist fees"
- "80% of revenue went to artist compensation"

**Source B:** Music industry analyst report, published six weeks later
- "Attendance was likely 28,000–35,000 based on [methodology]"
- "Artist compensation is typically 40–60% of revenue; 80% claim seems
  high"
- "If $2.8M is accurate, total revenue was ~$3.5M (high for this
  festival tier)"

### Reconciliation Process:

#### Claim 1: Attendance
- **Source A says:** 45,000. **Source B says:** 28,000–35,000 (based on
  comparable festivals).
- **Independence:** Independent (company official vs. third-party
  analyst).
- **Outcome:** BOTH VALID
- **Rationale:** Festival organizers have incentive to report high
  attendance. Analyst is using comparative method, which is credible but
  not definitive. The disagreement reflects different measurement
  methods rather than one being wrong. Attendance is likely between
  30,000–45,000.
- **Report Placement:** "Attendance estimates range from 28,000–45,000.
  Festival organizers claimed 45,000 (unverified). Industry analysis
  suggests 28,000–35,000 based on comparable events. Actual attendance
  likely between 30,000–40,000."
- **Status:** RESOLVED

#### Claim 2: Artist Compensation
- **Source A says:** $2.8M. **Source B:** questions whether 80% is
  realistic if $2.8M is accurate, not the dollar amount itself.
- **Outcome:** BOTH VALID
- **Rationale:** No direct contradiction on the $2.8M figure. Analyst is
  questioning the *percentage*, not the dollar amount. On amount:
  Source A credible (organizers have actual data). On percentage:
  industry analyst provides context that 80% is unusually high.
- **Report Placement:** "Artists received $2.8M in compensation (per
  organizers). This represents approximately 80% of festival revenue if
  total revenue was $3.5M. Industry norms for this festival tier are
  typically 40–60% artist payout, suggesting this festival prioritized
  artist compensation unusually heavily."
- **Status:** RESOLVED

#### Claim 3: Revenue Figure
- Both sources agree on the implied math ($2.8M ÷ 0.80 = $3.5M). No
  contradiction — agreement disguised as one.
- **Outcome:** BOTH VALID (actually agreement).
- **Status:** RESOLVED

### Result:
The initial apparent contradiction (45,000 attendees vs. 28,000–35,000)
is real but resolved as **two credible but different measurement
methods**. Both figures go in the report with context. No figure is
discredited. Reader understands the range and why disagreement exists.

---

## Checklist: Reconciliation Verification

Before finalizing your VERIFY phase outputs, verify that you've handled
all contradictions:

| Item | Question | Red Flag | Status |
|------|----------|----------|--------|
| **Contradiction ID** | Have I identified all contradictions in my source pool? | Contradictions hidden or missed | ✓ / ✗ |
| **Clarity** | Can I state each contradiction in one sentence without paraphrase? | Vague or complex statement | ✓ / ✗ |
| **Scoring** | Have I scored both sources? | Scoring omitted or unclear | ✓ / ✗ |
| **Independence** | Have I checked whether sources are independent or echoes? | Not assessed; false independence assumed | ✓ / ✗ |
| **Outcome** | Have I picked one of four outcomes for each? | Outcome missing or vague | ✓ / ✗ |
| **Rationale** | Can I explain *why* I chose the outcome? | Rationale circular or missing | ✓ / ✗ |
| **Placement** | Have I decided where each contradiction appears in the final report? | Placement undefined; contradiction may get lost | ✓ / ✗ |
| **Reconciliation Record** | Is my Reconciliation Record complete? | Columns empty or incomplete | ✓ / ✗ |
| **Assumptions disclosed** | Have I drafted disclosure for WINNER CLEAR contradictions? | Contradictions glossed over; reader blind | ✓ / ✗ |
| **Tensions in Synthesis** | Have I identified BOTH VALID contradictions as *tensions* to explore? | Tensions missed; synthesis misses complexity | ✓ / ✗ |
| **UNKNOWN Flags** | Have I flagged UNRESOLVABLE contradictions as UNKNOWN confidence? | UNKNOWN claims stated as certain | ✓ / ✗ |
| **Reframing Justified** | For every REFRAME outcome, can I explain the reframe in one clear sentence? | Reframe feels like sophistry or avoidance | ✓ / ✗ |

---

## Downstream: How Reconciliation Feeds the Report

Once reconciliation is complete (VERIFY phase), your decisions feed
three sections of the final Research Report:

### 1. Assumptions and Limitations
Contradictions with WINNER CLEAR outcome go here. Format:

> "We initially encountered reports claiming X (Source B). However, we
> weighted Source A over Source B because Source A has direct authority
> and Source B is estimation-based. Assumption: Our assessment that
> [Source A reason] is more reliable than [Source B reason]."

### 2. Findings (for BOTH VALID)
Tensions go here. Format:

> "On [claim], there is credible disagreement. Proponents (Source A)
> argue [position]. Critics (Source B) contend [position]. Both
> perspectives have evidence. This tension likely reflects [underlying
> cause: different incentives / time horizons / constituencies]."

### 3. Limitations & Unknowns (for UNRESOLVABLE)
UNKNOWN claims go here. Format:

> "[Claim] could not be verified. Evidence conflicts: Source A asserts
> X, Source B asserts NOT X. Equivalent credibility. No third source
> available. Therefore, [claim] is marked UNKNOWN confidence and
> excluded from recommendations pending further evidence."

### Synthesis
Tensions (BOTH VALID contradictions) become opportunities for
interpretation:

> "The disagreement about [topic] reveals deeper complexity: [analysis
> of why both sides are right, what they prioritize differently, what
> this means for the bigger picture]."

---

## Key Principles

**Reconciliation rests on three non-negotiable principles:**

1. **Transparency > consensus**
   - Contradictions are not embarrassments. They are information.
   - Always disclose that a contradiction exists and explain how you
     resolved it.

2. **Scoring guides decisions**
   - Use the source-scoring rubric. Don't override it for narrative
     convenience.
   - If the score feels wrong, re-examine the score. Don't ignore it and
     pick the source you prefer.

3. **One source, not two**
   - Always check independence.
   - If Source B is quoting Source A, you have one source (A) plus an
     echo (B). Count as one.
   - This prevents false triangulation (the illusion that two sources
     agree when they're really one source cited twice).

---

## Linked References

- `source-scoring.md` — how to score sources (prerequisite for
  reconciliation)
- `source-personas.md` — persona classification for independence
  assessment
- `independence-test.md` — following a source back to its origin
