# Anomaly Investigation: Signal Detection & Treatment
**How to Recognize, Investigate, and Use Outlier Data in Research**

---

## What Is an Anomaly?

An anomaly is a claim, data point, or source behavior that **contradicts
the emerging pattern** and stands out as unusual. It is not noise to
average away. It is a signal.

Anomalies are evidence of **complexity** — hidden realities, tensions,
exceptions that disprove simple rules, or unique insights that others
have missed. They demand investigation before treatment.

**Why not ignore anomalies?**
- **Pattern visibility:** Anomalies reveal where your pattern breaks.
  They expose assumptions.
- **Hidden reality:** An anomaly often means someone is seeing something
  others missed — privileged access, different angle, more recent data,
  or the actual exception that proves the rule.
- **Synthesis power:** Anomalies drive sophisticated synthesis. They move
  from "X is true" to "X is true, **except when** Y, which reveals Z
  about the system."
- **Report credibility:** Reporting anomalies and how you treated them
  builds trust. Hiding them erodes it.

**The research principle:** If a source contradicts your pattern, that
source gets investigated **before** it gets averaged, discounted, or
ignored. Investigation may conclude the source is unreliable — but you
conclude that *after* investigation, not before.

---

## Anomaly Detection: What Counts?

Flag anomalies during the **INTEL phase** (source capture and early
analysis). An anomaly is one of these:

| Pattern | Example | Trigger |
|---------|---------|---------|
| **Direct contradiction** | 5 sources say "X hired 20 people." One source says "X laid off 10 people." | Claims are logically opposite |
| **Tier mismatch** | Bronze source claims something that contradicts Gold tier consensus | Lower reliability contradicts higher reliability |
| **Persona contradiction** | All Independent Observers report "X is declining." One Primary Artifact (X's press release) says "X is growing." | Same claim, different signals from different personas |
| **Pattern break** | 9 sources show pattern: "all firms in sector are hiring." One source: "Firm A is hiring; all others freezing." | One outlier in consistent series |
| **Statistical outlier** | Industry average hiring rate: 5%. Firm X: 35%. | Data point is 3+ standard deviations from mean |
| **Recency conflict** | Old sources say "X is stable." New source says "X pivoted strategy." | Time dimension creates apparent contradiction |
| **Scope mismatch** | Sources claim "UK market growing." One source claims "London division shrinking." | Same claim at different geographic scope |
| **Persona inconsistency** | Same source changes position across different captures | Source contradicts itself |

---

## Anomaly Investigation Flowchart

When you flag an anomaly, follow this decision tree:

```
                    ┌─────────────────────────────────────┐
                    │  ANOMALY DETECTED                   │
                    │  X says [claim] but pattern         │
                    │  suggests [different claim]         │
                    └─────────────────┬───────────────────┘
                                      │
                          ┌───────────▼───────────┐
                          │ STEP 1: SCOPE CHECK   │
                          │ Is this actually a    │
                          │ contradiction or      │
                          │ different scope/time? │
                          └───────────┬───────────┘
                                      │
                    ┌─────────────────┴─────────────────┐
                    │                                   │
         ┌──────────▼──────────┐         ┌──────────────▼──────────┐
         │ SCOPE EXPLAINS IT   │         │ REAL CONTRADICTION      │
         │ (Not an anomaly)    │         │ Proceed to Step 2       │
         │ Document & exit     │         └──────────────┬──────────┘
         └─────────────────────┘                        │
                                         ┌──────────────▼──────────┐
                                         │ STEP 2: SOURCE CREDIBLE │
                                         │ Score source X:         │
                                         │ • Tier (Gold/Silver/etc)│
                                         │ • Persona type          │
                                         │ • Track record          │
                                         │ • Bias alignment        │
                                         └──────────────┬──────────┘
                                                        │
                            ┌───────────────────────────┴────────────────────────┐
                            │                                                    │
              ┌─────────────▼──────────────┐              ┌────────────────▼────┐
              │ X IS HIGHLY CREDIBLE       │              │ X IS LOW CREDIBLE  │
              │ Proceed to Step 3          │              │ Consider rejecting │
              └─────────────┬──────────────┘              └────────────────┬───┘
                            │                                              │
           ┌────────────────▼────────────────┐        ┌───────────────────▼─────┐
           │ STEP 3: PRIVILEGE CHECK        │        │ STEP 6: DOCUMENT IN LOG │
           │ Does X have access that others │        │ Entry: "Rejected X due  │
           │ don't? Hidden insight angle?   │        │ to low credibility"     │
           └────────────┬───────────────────┘        └─────────────────────────┘
                        │
        ┌───────────────┴───────────────┐
        │                               │
  ┌─────▼──────────┐           ┌───────▼────────┐
  │ X HAS SPECIAL  │           │ X HAS NO SPECIAL│
  │ INSIGHT        │           │ ACCESS/ANGLE    │
  │ Proceed Step 4 │           │ Investigate more│
  └────────┬───────┘           └────────┬────────┘
           │                            │
      ┌────▼─────────────────────────────▼─────┐
      │ STEP 4: DEEPER INVESTIGATION           │
      │ • More captures from X?                │
      │ • Triangulate X's claim?               │
      │ • Check X's track record for accuracy? │
      │ • Is X's data fresher/different scope? │
      └────┬──────────────────────────┬────────┘
           │                          │
      ┌────▼───────────┐   ┌──────────▼───────┐
      │ X'S CLAIM HOLDS│   │ X'S CLAIM FAILS  │
      │ Investigate    │   │ Source error or  │
      │ further (Step 5)   │ methodological   │
      └────┬───────────┘   │ flaw detected    │
           │               └──────────┬───────┘
           │                          │
           │        ┌─────────────────┘
           │        │
      ┌────▼────────▼──────────────────────┐
      │ STEP 5: DECIDE TREATMENT          │
      │ Error in X? Insight in X?         │
      │ Different valid perspective?       │
      │ (See treatment table below)        │
      └────────────┬─────────────────────┘
                   │
      ┌────────────▼──────────────┐
      │ STEP 6: DOCUMENT IN LOG   │
      │ Record decision & rationale│
      └───────────────────────────┘
```

---

## Anomaly Treatment Options

Once you've investigated, decide **how to treat** the anomaly. Use this
table:

| Treatment | When to Use | Evidence Threshold | How to Document |
|-----------|-------------|-------------------|-----------------|
| **Reject anomaly** | Source X is clearly unreliable, compromised, or contains methodological error | Score <2/5 OR source caught in error OR clear bias override | Anomaly Log: "Rejected X due to [reason]. X is [tier/persona], makes [claim] contradicting pattern. Investigation found [specific error/bias/conflict]." |
| **Integrate anomaly** | Anomaly reveals hidden tension, nuance, or exception that enriches understanding | Any tier if investigation validates insight | Anomaly Log: "Integrated X into analysis. X's unique position/access reveals [complexity]. Treated as [evidence of exception/tension]." Include in SYNTHESIZE essays. |
| **Investigate further** | Anomaly might hold unique insight but need more triangulation before deciding | Score 3-4/5 AND single-sourced claim OR contradictory signals from credible sources | Anomaly Log: "Investigate further. X claims [claim]. Need to triangulate with [specific sources/data]." Add to Gap list for next phase. |
| **Flag as UNKNOWN** | Cannot resolve anomaly despite investigation; need to report it | Score 2-4/5 AND investigation inconclusive | Report with ESTIMATED confidence, disclose limitation: "[Claim] is ESTIMATED (single credible source, anomalous in pattern). Limitation: [reason we can't triangulate]." |

---

## Anomaly Log Template

Maintain a running record of all flagged anomalies and their treatment.
Use this format:

| Anomaly | Source | Pattern It Contradicts | Source Credibility | Investigation Result | Treatment |
|---------|--------|----------------------|-------------------|----------------------|-----------|
| Source X says "hiring down 5%"; pattern is "all hiring up" | Firm X press release | 8 other sources reporting sector-wide hiring surge | Gold tier, Primary Artifact, but press releases are self-promotional | Press release may lag actual hiring; LinkedIn data (Silver, Independent) confirms hiring activity. X's own job board shows 6 open roles. Likely X is hiring but press release hasn't updated. | Integrated: Treat as evidence that firms *lag in communication* about hiring. Include in essay as complexity. |
| Source Y says "firm pivoted to AI"; all others focus on compliance | CEO interview | Consistent narrative that compliance is only growth area | Silver tier, Promo Insider, CEO incentive to claim innovation | Checked LinkedIn hires past 6 months: 4 AI roles, 8 compliance roles. AI is secondary focus. CEO is claiming priority beyond actual investment. | Integrated: Treat as evidence of *stated direction vs. actual resourcing*. Include as essay point on leadership narrative vs. reality. |
| Source Z claims "market saturated"; 6 sources claim "market growing" | Blog post (author unknown) | Strong triangulation across 3+ personas showing market growth | Bronze tier, Well-Meaning Generalist, no author credentials | Blog cites no sources. Author has no track record. No corroboration found. Likely author has outdated understanding or different segment. | Rejected: "Source Z is unattributed blog post with no evidence. Does not meet threshold for anomaly investigation." |
| Source A reports "firm X laying off"; press release says "restructuring" | Anonymous insider contact | 9 sources reporting hiring activity in same period | Silver tier, Anonymous Insider, incentive to be accurate but identity unverified | Checked job postings: firm posted 15 new roles same week as restructuring. Layoff number (30 people) and hiring number (15 new roles) could coexist if restructuring moved teams. Insider may be accurate about layoff *process* while hiring continues for *new strategy*. | Integrated: Treat as evidence that hiring and restructuring occurred simultaneously. Include in essay as evidence of *portfolio shift within organization*. |
| Source B says "only UK market growing"; all others report "all EU markets growing" | Regional analyst report (Silver) | 5+ sources (mix of personas) reporting EU-wide growth | Silver tier, Captured Expert, but analyst covers only specific region | Checked: report covers UK only. Analyst's data is accurate for UK but incomplete for EU. Not an anomaly — scope difference. | Not treated as anomaly. Document as scope note: "B's claim accurate for UK but incomplete for Europe." |

---

## Investigation Checklist (Step 2–5)

Use this checklist when investigating an anomaly:

### Step 2: Source Credibility (5 points)

- [ ] What is source X's tier? (Gold/Silver/Bronze — affects
      interpretation weight)
- [ ] What persona does X represent? (affects bias direction)
- [ ] Does X have a track record? (Has this source been accurate on
      similar claims before?)
- [ ] What is X's incentive structure? (Why would X make this claim?
      Does that incentive override evidence?)
- [ ] Are there known errors in X's category? (Do press releases lag
      actual data? Do insiders have selective view?)

### Step 3: Privilege Check (3 questions)

- [ ] **Access:** Does X have privileged access that others lack?
- [ ] **Angle:** Is X observing a different slice of reality?
- [ ] **Recency:** Is X's data more recent than pattern sources?

### Step 4: Deeper Triangulation (4 checks)

- [ ] **More from X?** Are there other captures from source X that
      corroborate or contradict this claim?
- [ ] **Triangulate X?** Can we find **independent sources** supporting
      X's claim? (Not echoes of X, not derivatives of X — truly
      independent verification?)
- [ ] **Track record?** Has source X made similar claims before that
      turned out to be accurate or false?
- [ ] **Methodology?** How did X arrive at this claim? Does the method
      seem sound?

### Step 5: Decision Criteria (choose one)

- [ ] **Reject:** Investigation reveals X is unreliable, method is
      flawed, bias is clear. Document reason.
- [ ] **Integrate:** Investigation reveals X's insight is valid and
      enriches understanding. Document how it changes interpretation.
- [ ] **Further investigate:** Need more data. Document what specific
      sources/data would resolve anomaly.
- [ ] **Flag UNKNOWN:** Cannot resolve. Report with appropriate
      confidence level, disclose limitation.

---

## Common Anomaly Investigation Mistakes

| Mistake | Example | Correction |
|---------|---------|------------|
| **Reject without investigating** | "X contradicts pattern, so X must be wrong." Discard without checking X's credibility or scope. | Always investigate first. Anomalies often reveal complexity, not error. |
| **Average anomalies away** | Five sources say "trend is up"; one says "trend is down." Report: "Trend is mixed." | Don't average contradictions. Investigate each. |
| **Treat anomaly as primary finding** | One credible outlier contradicts 10 sources. Report starts with the outlier's claim as main finding. | Anomalies inform interpretation, not dominate it. |
| **No scope checking** | Assume contradiction without checking geography, time, or segment. | Always Step 1: check scope. Many "anomalies" are just different scopes. |
| **Confuse anomaly with error** | One source is wrong on a detail. Discard entire source's analysis. | Investigate the detail specifically. Source may be reliable overall but wrong on one point. |
| **Echo chamber anomaly** | Two "independent" sources both cite the same underlying data. Treat as triangulation. | Verify independence in Step 3. One underlying source = one source, not two. |
| **Undisclosed anomaly treatment** | Investigation shows X is unreliable, exclude X without documenting why. | Always document treatment. Report credibility builds from transparency. |
| **Wrong scope blame** | Assume scope explains anomaly without checking whether the scopes actually nest. | Verify scope logic before dismissing a real contradiction. |

---

## Field Use: Integration with the Research Cycle

### INTEL Phase: Flagging Anomalies

During source capture and early analysis, flag potential anomalies:

1. **As you capture each source,** note if claim contradicts what you've
   already captured
2. **Pattern check:** After 5–10 sources, pause to ask: "Are there
   outliers in this set?"
3. **Low-confidence claims:** Sources with lower tier or single-sourced
   claims are anomaly candidates
4. **Mark in Source Registry:** Add "ANOMALY FLAG" column.

### VERIFY Phase: Investigate Anomalies

During fact-checking and source scoring:

1. **For each flagged anomaly,** run the investigation flowchart
   (Steps 1–5 above)
2. **Use Anomaly Log** to document each investigation
3. **Adjust source scores** based on investigation results
4. **Triangulation update:** If anomaly is integrated or investigated
   further, add new sources to the Independence Map

### SYNTHESIZE Phase: Use Anomalies

In synthesis, anomalies become evidence of complexity:

- **Pattern + anomaly = nuance:** "The sector is hiring (pattern),
  **except** Firm X is restructuring (anomaly), which suggests
  [interpretation]."
- **Anomalies as turning points:** "Through June, hiring was flat. Then
  [anomaly event]. Since July, hiring surged. This reveals
  [complexity]."
- **Exception as rule:** "All firms follow strategy X, **except** Firm
  Y, which follows strategy Z. Y's exception reveals [hidden reality
  about the system]."
- **Disclose treatment:** Include a note on anomalies you investigated
  and why you treated them as you did.

### REPORT Phase: Disclose Limitations

- **Anomaly table:** For major anomalies, include a table showing the
  contradiction, investigation, and treatment
- **Confidence adjustments:** If anomaly investigation lowered confidence
  on a claim, state it: "[Claim] is LIKELY, though [anomaly] suggests
  [caveat]."
- **Gaps:** If anomaly cannot be resolved, include in Searched And Not
  Found: "Claim X contradicts Claim Y. We investigated [what we did];
  further triangulation needed."
- **Transparency wins credibility:** Reporting anomalies and how you
  handled them makes the report more trustworthy, not less.

---

## Example Anomaly Investigation

**Research Context:** Investigating hiring trends in a European
compliance sector.

**Pattern Established:** 8 sources (mix of personas, Gold/Silver tier)
show compliance hiring surge across sector, +30–40% year over year.

**Anomaly Flagged:**
- Source: Firm Z press release
- Claim: "Firm Z restructured compliance team, moving to an AI-first
  approach"
- Contradicts: Pattern that says "compliance hiring is UP"; this sounds
  like lateral or DOWN

**Step 1: Scope Check**
- Pattern timeframe: Last 12 months. Source timeframe: 3 months old.
  Pattern: Sector-wide. Source: Firm Z only.
- **Verdict:** Real difference in scope (single firm vs. sector). But
  claim still anomalous within Firm Z itself. Continue.

**Step 2: Source Credibility**
- Tier: Gold (press release = primary artifact). Persona: Primary
  Artifact. Incentive: Position Z as forward-thinking. Track record:
  Z's press releases are accurate on announcements but often lag actual
  business reality.
- **Score: 3/5** — credible on announcement but may not reflect
  execution

**Step 3: Privilege Check**
- Access: Yes, Z has direct knowledge of own restructuring. Angle: Yes,
  Z sees inside the firm. Recency: 3 months old.
- **Verdict:** Z has special access but press releases often lag
  reality.

**Step 4: Deeper Investigation**
- Checked Z's LinkedIn hiring data: posted 4 AI roles, 9 compliance
  roles — 70% compliance-heavy despite the announcement.
- Triangulated with 2 recruiter contacts (Silver, Anonymous Insiders):
  "Z is hiring for both but compliance still dominates."
- Track record: Z made a similar "pivot" announcement 2 years earlier;
  hiring reality showed 80% compliance, 20% other.

**Step 5: Decision**
- Finding: Z's press release is aspirational (what Z wants to project)
  but doesn't match hiring reality.
- Treatment: **INTEGRATE AS EVIDENCE OF NARRATIVE-REALITY GAP** — what
  firms *say* they're doing ≠ what they're *doing*. Suggests compliance
  hiring is strong enough that even "AI-first" firms can't resist hiring
  compliance staff.

**Step 6: Document**

| Anomaly | Source | Pattern It Contradicts | Source Credibility | Investigation Result | Treatment |
|---------|--------|----------------------|-------------------|----------------------|-----------|
| "Z moving to AI-first" suggests compliance staff down; pattern shows up | Firm Z press release | 8-source consensus: compliance hiring +30–40% YoY | Gold tier (primary artifact), but Z's press releases are promotional and often lag execution. Score 3/5. | LinkedIn hiring data shows Z hired 4 AI, 9 compliance roles = 70% compliance focus. Recruiter contacts confirm compliance still dominates. Z's 2-year track record: aspirational announcements, compliance-heavy hiring. | **Integrated:** Treat as evidence of *narrative-reality gap*. Firms claim AI pivot but hire compliance staff. Reveals that regulatory urgency overrides technology strategy. |

---

## Anomaly Investigation at Scale

For large research operations with 20+ sources and multiple anomalies:

1. **Dedicate one researcher** to anomaly investigation (don't let it
   slow main pattern analysis)
2. **Use the Anomaly Log as a live document** — update as investigations
   conclude
3. **Periodic anomaly review** — bring unusual findings to team
   discussion
4. **Independence Map + Anomaly Log together** — anomalies inform
   independence adjustments
5. **Flag before rejecting** — investigate before dismissing any
   credible source
6. **Build anomaly pattern** — if multiple anomalies point to the same
   hidden reality, that's your synthesis insight

---

## Confidence Language for Anomaly-Informed Claims

When writing findings that involved anomaly investigation, use precise
language:

| Finding Type | Language | Example |
|--------------|----------|---------|
| Pattern with no anomalies | CONFIRMED (direct, high confidence) | "Compliance hiring is surging across all firms." |
| Pattern with rejected anomaly | CONFIRMED (high confidence despite outlier) | "Compliance hiring is surging (rejected X because [reason])." |
| Pattern with integrated anomaly | LIKELY (pattern holds, but with caveat) | "Compliance hiring is surging, though firms often claim broader pivots than hiring reflects." |
| Pattern with unresolved anomaly | ESTIMATED (pattern is probable but limited confidence) | "Compliance hiring is likely surging (based on 8 sources), though [anomaly] creates some uncertainty." |
| Single anomalous claim | UNKNOWN (insufficient verification) | "Z's claim on regulatory change is unverified (single-sourced, anomalous)." |

---

**Field use:** When you encounter a claim that doesn't fit the pattern,
**don't average it away**. Investigate it. It might be error — or it
might be insight that changes everything.
