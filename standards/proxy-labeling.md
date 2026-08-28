# Proxy Labeling Reference

Decision framework for identifying, validating, and transparently
disclosing proxy measures when direct data is unavailable. Proxies are
indirect measures standing in for direct ones. Without labeling them,
reports appear factual when they're actually inferred — corrupting
downstream decisions. (1) identify proxies during PLAN, set confidence to
ESTIMATED; (2) validate proxies during VERIFY, tag with correlation
strength; (3) disclose proxies in REPORT, flag impact on confidence.

## 1. What Is a Proxy?

A **proxy** is an indirect measure used to infer or estimate a direct
measure when the direct measure is unavailable, expensive, or
unmeasurable.

**Definition:** A proxy is valid when it is *correlated* with the thing
you actually want to know, but it is not the thing itself.

### 1.1 Proxy vs. Direct Measure

| Measure Type | Definition | Example | Confidence Level |
|---|---|---|---|
| **Direct** | You have the actual data | Revenue report from a public filing | CONFIRMED |
| **Proxy** | You infer from related data | Employee count × industry salary averages | ESTIMATED |
| **Failed Proxy** | Weak or no correlation | Number of office locations → tech maturity | Do not use |

### 1.2 Why Proxies Matter

**Without labeling proxies, three things break:**
1. **Credibility erosion** — downstream readers think an inferred
   number is factual
2. **Decision contamination** — receivers act on ESTIMATED data as if it
   were CONFIRMED
3. **Report degradation** — claims appear authoritative when they should
   appear tentative

**With labeling proxies:**
1. Readers understand confidence level upfront
2. Claims carry appropriate epistemic weight
3. When better data arrives, proxies can be swapped transparently

### 1.3 Proxy Domains in Research

| Domain | Proxy Use | Risk Level |
|---|---|---|
| **Quantitative** | Employee count → revenue potential, hiring rate → confidence | HIGH — numbers appear factual |
| **Qualitative** | Press mentions → market attention, social followers → brand reach | MEDIUM — narrative signals are noted but less precise |
| **Temporal** | Historical hiring as proxy for near-term growth, past spending as proxy for next year's budget | MEDIUM-HIGH — time gaps erode correlation |

---

## 2. Decision Framework: Should I Use This Proxy?

```
START: Do you have the DIRECT MEASURE for this claim?
│
├─ YES → Use direct measure. No proxy needed. Tag as CONFIRMED.
│
└─ NO → Is there a CORRELATED INDIRECT measure available?
    │
    ├─ NO → Cannot support this claim. Mark as UNKNOWN. Do not guess.
    │
    └─ YES → Can you TRIANGULATE this proxy with ≥2 other sources?
        │
        ├─ YES → Move to Proxy Validation. Confidence may be LIKELY or ESTIMATED.
        │
        └─ NO → Single proxy with no triangulation. Confidence = ESTIMATED.
            │
            └─ Must you disclose this proxy to downstream users?
                │
                ├─ YES → Label proxy, tag ESTIMATED, disclose in report.
                │
                └─ NO → (Internal use only) Label proxy, track confidence, keep audit trail.
```

**Decision Rules:**
- **Never use a proxy without naming it.** Hiding the proxy is lying by
  omission.
- **Single proxy without triangulation → ESTIMATED confidence.** Always.
- **Proxy with 2+ independent sources → confidence may improve to
  LIKELY.**
- **If downstream users can't understand the proxy, must disclose.**

---

## 3. Proxy Validation Checklist

Before using any proxy, run this checklist:

```
PROXY VALIDATION CHECKLIST
□ Proxy Name — What indirect measure are we using?
  Example: "employee headcount"

□ Target Measure — What are we actually trying to know?
  Example: "revenue scale / revenue potential"

□ Correlation Claim — How strongly correlated are these?
  Scoring: 1–5 (1=weak, 5=direct causation)
  Example: "3/5 — moderate correlation (industry salary data required)"

□ Triangulation Sources — Which independent sources validate this proxy?
  Minimum for LIKELY: 2 sources
  Example: LinkedIn headcount + Crunchbase + press releases

□ Confidence Impact — Does this proxy lower confidence?
  Original confidence: CONFIRMED / LIKELY / ESTIMATED
  Proxy-adjusted confidence: CONFIRMED / LIKELY / ESTIMATED
  Example: CONFIRMED → ESTIMATED (no direct revenue data)

□ Golden Words Applied — Does the proxy get flagged in prose?
  Example: "Likely has 400–500 employees (proxy: headcount)"

□ Disclosure Required? — Must this proxy appear in the report?
  If YES: Add to the sources block with correlation score
  If NO: Log internally, audit trail only

□ Decay Rate — How quickly does this proxy lose validity?
  24 hours / 1 week / 1 month / 6 months / annual
  Example: "Headcount data sourced this month; valid for ~2 months"

□ Exception Cases — Are there edge cases where this proxy fails?
  Example: "Proxy breaks for holding companies with shell staff"
  Document assumption limits.
```

---

## 4. Proxy Examples + Validation Framework

Seven common proxies used in research operations, with validation
examples.

### 4.1 Employee Headcount → Revenue Potential

| Field | Value |
|---|---|
| **Proxy** | Employee headcount |
| **Represents** | Revenue scale, company maturity, operational capacity |
| **Correlation Strength** | 3/5 — Moderate. Varies by industry (SaaS: 4/5; Manufacturing: 2/5) |
| **Triangulation Sources** | LinkedIn, Crunchbase, press releases, company website ("team" page) |
| **Confidence Impact** | CONFIRMED → ESTIMATED (no direct revenue filing) |
| **Golden Words** | "Estimated $X revenue (proxy: headcount × industry average salary)" |
| **Common Error** | Treating headcount as direct revenue measure without industry context |
| **Decay Rate** | 6–8 weeks (hiring/layoffs shift fast; quarterly updates recommended) |

**Validation Example:** Three sources cluster within ~3% of each other
(127, 130, "grew team to 125") → confidence LIKELY. Revenue proxy: avg
headcount × industry-average salary (SaaS tier) implies a revenue range.
Report disclosure: "Estimated $X–Y revenue (proxy: headcount × industry
salary averages; confidence: LIKELY)."

---

### 4.2 Hiring Rate → Company Confidence/Expansion

| Field | Value |
|---|---|
| **Proxy** | Net hiring over past 6 months (headcount growth %) |
| **Represents** | Company confidence in near-term growth, capital availability, market opportunity |
| **Correlation Strength** | 4/5 — Strong. Hiring almost always signals confidence (exceptions: consolidation hires, panic hires) |
| **Triangulation Sources** | Job posting sites, hiring-timeline data, press announcements, company growth charts |
| **Confidence Impact** | ESTIMATED → LIKELY (with 2+ sources) |
| **Golden Words** | "Likely expanding (proxy: 23% hiring growth in 6M; confidence: LIKELY)" |
| **Common Error** | Ignoring consolidation hires or temporary contract roles |
| **Decay Rate** | 2–4 weeks (hiring trends change quarterly) |

---

### 4.3 Press Mentions → Market Attention

| Field | Value |
|---|---|
| **Proxy** | Number and quality of press mentions in past 3 months |
| **Represents** | Market attention, thought leadership, narrative momentum |
| **Correlation Strength** | 2/5 — Weak. Press is noisy and often driven by paid placement or investor relations |
| **Triangulation Sources** | News aggregators, industry blogs, social mentions, press release archives |
| **Confidence Impact** | ESTIMATED (always, even with triangulation) |
| **Golden Words** | "Some market attention (proxy: N mentions in a quarter; confidence: ESTIMATED)" |
| **Common Error** | Treating press volume as market impact without checking mention quality |
| **Decay Rate** | 1–2 weeks (media cycles are fast) |

---

### 4.4 Job Posting Count → Growth Plans / Hiring Urgency

| Field | Value |
|---|---|
| **Proxy** | Number of open job postings (absolute and relative to headcount) |
| **Represents** | Near-term growth plans, capital availability, hiring urgency |
| **Correlation Strength** | 4/5 — Strong. Job postings are committed spend |
| **Triangulation Sources** | Job boards, careers page, press announcements |
| **Confidence Impact** | ESTIMATED → LIKELY (with 2+ sources, if recent) |
| **Golden Words** | "Planning growth (N open roles = X% hiring target; confidence: LIKELY)" |
| **Common Error** | Not accounting for how long a job posting has been live (stale postings inflate counts) |
| **Decay Rate** | 1 week (postings fill or close quickly) |

---

### 4.5 Social Media Followers → Brand Reach / Audience Size

| Field | Value |
|---|---|
| **Proxy** | Follower count across social channels |
| **Represents** | Brand reach, audience engagement potential, market awareness |
| **Correlation Strength** | 3/5 — Moderate. Followers don't predict revenue or engagement quality. Bots inflate counts. |
| **Triangulation Sources** | Each platform, plus engagement metrics (likes, retweets, comments) |
| **Confidence Impact** | ESTIMATED (always) |
| **Golden Words** | "Modest social footprint (~N combined followers; confidence: ESTIMATED — engagement unvalidated)" |
| **Common Error** | Treating raw follower count as proxy for actual reach (engagement rate is better predictor) |
| **Decay Rate** | 1–2 weeks (follows are volatile) |

---

### 4.6 Revenue-per-Employee → Productivity / Unit Economics

| Field | Value |
|---|---|
| **Proxy** | Implied revenue per employee (revenue ÷ headcount) |
| **Represents** | Operational efficiency, unit economics, scalability |
| **Correlation Strength** | 2/5 — Weak. Compounded by proxy-on-proxy risk. Highly industry-dependent. |
| **Triangulation Sources** | Industry benchmarks, peer comparisons, operational efficiency literature |
| **Confidence Impact** | CONFIRMED → ESTIMATED (usually), or ESTIMATED → UNKNOWN (double proxy) |
| **Golden Words** | "Implied efficiency: ~$X revenue per employee (industry benchmark: $Y; confidence: ESTIMATED)" |
| **Common Error** | Using a revenue/employee ratio without validating both revenue and headcount independently |
| **Decay Rate** | 3–6 months (operational changes are gradual) |
| **⚠️ CAUTION** | **Proxy-on-Proxy Risk.** If both revenue AND headcount are proxies, confidence degrades to ESTIMATED even with triangulation. Document this clearly. |

---

### 4.7 Funding Announcements → Capital Availability / Burn Rate

| Field | Value |
|---|---|
| **Proxy** | Total capital raised + funding round size as proxy for available cash / runway |
| **Represents** | Capital availability, burn rate timeline, growth runway |
| **Correlation Strength** | 3/5 — Moderate. Raised capital ≠ available capital (accounting lags, spend timing varies). |
| **Triangulation Sources** | Funding databases, filings (if public), press releases, investor relations |
| **Confidence Impact** | LIKELY → ESTIMATED (even with multiple sources, time lag erodes correlation) |
| **Golden Words** | "Capitalized for ~N month runway (proxy: total raised ÷ estimated monthly burn; confidence: ESTIMATED)" |
| **Common Error** | Assuming announced funding = available cash without accounting for deployment timelines or terms |
| **Decay Rate** | 4–8 weeks (capital deployment and burn rates shift monthly) |

---

## 5. Common Mistakes — What Not To Do

### ❌ Mistake 1: Using a Proxy Without Naming It
**Wrong:** "The company likely has $15M annual revenue."
**Right:** "Estimated $15M revenue (proxy: headcount × industry salary;
confidence: ESTIMATED)"
**Impact:** Without the label, readers think this is a fact, not an
inference. Credibility destroyed when revealed.

### ❌ Mistake 2: Treating a Proxy as Direct Data
**Wrong:** "Job postings show the company is hiring 12 people."
**Right:** "The company has 12 open job postings, likely indicating
plans to hire ~10 people (posting data shows intent, not commitment)."
**Impact:** Job postings are intent signals, not executed hires. Proxy
confidence is ESTIMATED, not CONFIRMED.

### ❌ Mistake 3: Proxy-on-Proxy Without Disclosure
**Wrong:** Using a revenue-per-employee ratio when both revenue and
headcount are proxies, without flagging the compounded uncertainty.
**Right:** "Unit economics suggest ~$X per employee (proxy-on-proxy:
both revenue and headcount are inferred; confidence: ESTIMATED, lower
weight on this measure)"
**Impact:** Stacking proxies geometrically decreases confidence. Must
explicitly disclose.

### ❌ Mistake 4: Not Triangulating a Weak Proxy
**Wrong:** Using a single press mention to claim "market attention."
**Right:** Combining press mentions + social signals + analyst reports
before claiming attention.
**Impact:** Single-source proxies are noisy. Triangulation improves
confidence from ESTIMATED to LIKELY (if sources are independent).

### ❌ Mistake 5: Ignoring Decay Rate
**Wrong:** Using year-old headcount data without noting the age.
**Right:** "128 employees (as of [date]; headcount typically shifts
5–10% per quarter; refresh recommended)"
**Impact:** Proxies degrade over time. Age the data and estimate decay
impact.

### ❌ Mistake 6: Proxy Without Exception Documentation
**Wrong:** Using employee headcount as a revenue proxy for all
companies.
**Right:** "Headcount-to-revenue proxy valid for SaaS/professional
services; breaks for capital-intensive (manufacturing, infrastructure)
and platform models."
**Impact:** Proxies have domain limits. Document them.

---

## 6. Proxy Labeling in Practice: Field Use

### 6.1 PLAN Phase: Identify Proxies Upfront

1. **List all claims** you plan to make in the research
2. **For each claim, ask:** Do I have direct data for this?
   - YES → no proxy needed
   - NO → propose a proxy and note it in the Brief
3. **Set proxy confidence to ESTIMATED** by default
4. **Note triangulation plan** — which sources will validate this
   proxy?

**Example Brief entry:**
```
CLAIM: "Company has $15–20M revenue"
DATA SOURCE: Unavailable (private company)
PROXY: Employee headcount × industry salary averages
CONFIDENCE: ESTIMATED (improved to LIKELY if triangulated with 2+ sources)
TRIANGULATION PLAN: LinkedIn + Crunchbase + press releases
```

### 6.2 INTEL Phase: Source Proxies Transparently

1. Log every source that contributes to a proxy (even weak ones)
2. Tag each source with its role: Primary proxy source / Triangulation
   source / Contextual
3. Note source quality and recency

### 6.3 VERIFY Phase: Validate Proxies, Tag Correlation

1. Run the Proxy Validation Checklist for each proxy used
2. Score correlation strength (1–5)
3. Validate triangulation (do independent sources align?)
4. Adjust confidence level based on triangulation outcome
5. Document any exception cases

### 6.4 SYNTHESIZE Phase: Flag Proxies in Draft

When writing claims that rely on proxies, use the confidence labels:

| Word | Usage | Confidence |
|---|---|---|
| **Confirmed** | Direct data, verified independently | CONFIRMED |
| **Likely** | Multiple corroborating sources, or strong proxy with good triangulation | LIKELY |
| **Estimated** | Single proxy or weak triangulation | ESTIMATED |
| **Unknown** | No data found; no proxy attempted | UNKNOWN |

### 6.5 REPORT Phase: Disclose Proxies Transparently

1. **Main text:** Use confidence labels to flag proxy claims
2. **Sources block:** List all proxy sources and correlation scores
3. **Confidence tiers:** Explicitly disclose if a claim relies on
   proxies
4. **Appendix (if needed):** Full Proxy Validation Checklist for complex
   proxies

---

## 7. Scoring Framework: Proxy Correlation Strength

| Score | Correlation Level | Definition | Example |
|---|---|---|---|
| **5** | Direct causation | Proxy IS almost the target measure; 95%+ predictive | Revenue per employee vs. actual revenue (weak proxy, but strong correlation) |
| **4** | Strong correlation | Proxy highly predicts target; <10% noise | Hiring rate → expansion signal |
| **3** | Moderate correlation | Proxy predicts target with ~20% noise; industry-dependent | Headcount → revenue potential |
| **2** | Weak correlation | Proxy has signal but high noise; many exceptions | Press mentions → market attention |
| **1** | Minimal/no correlation | Proxy unreliable; should not be used | Number of competitors → our market opportunity |

**Rule:** Score ≥3 required to use proxy. Scores 1–2 are not proxies;
they're guesses.

---

## 8. Decay Rate Reference: When Proxies Expire

| Proxy Type | Decay Period | Reason | Refresh Signal |
|---|---|---|---|
| **Headcount** | 6–8 weeks | Hiring/layoffs accelerate | Growth chart, new job postings |
| **Hiring rate** | 2–4 weeks | Hiring trends change monthly | Posting updates, press announcements |
| **Press mentions** | 1–2 weeks | Media cycles move fast | Latest mention date; engagement trend |
| **Job postings** | 1 week | Postings fill or age out rapidly | Posting dates; crawl timestamps |
| **Social followers** | 1–2 weeks | Follower counts volatile | Baseline established; track weekly |
| **Funding data** | 4–8 weeks | Deployment timing lags; burn rate fluctuates | Guidance; spending announcements |
| **Revenue-per-employee** | 3–6 months | Operational changes gradual | Annual reporting cycles |

**Rule:** If proxy data is older than the decay period, note the age and
estimate impact.

---

## 9. Common Confusion: Proxy vs. Assumption

No. Clarify this distinction upfront.

| Term | Definition | Example |
|---|---|---|
| **Proxy** | Indirect *measure* correlated with target | Headcount as proxy for revenue |
| **Assumption** | Belief about relationship or parameter | "Assuming $120k average salary" |

**Proxies need assumptions to work:** "Employee headcount [proxy]
assuming $120k average salary [assumption] implies $15M revenue."

**Rule:** Name both proxy AND assumptions separately. Both must be
disclosed. See `assumption-exposure.md`.

---

## 10. Speed Card: Proxy Labeling in 60 Seconds

```
PROXY LABELING — 60-SECOND CHECKLIST

1. DO I HAVE DIRECT DATA?
   YES → Use it. Tag: CONFIRMED
   NO → Continue

2. WHAT PROXY AM I USING?
   Name it explicitly. Example: "headcount"

3. WHAT AM I ACTUALLY MEASURING?
   Example: "revenue potential"

4. HOW CORRELATED? (1–5 scale)
   3+ → can use / <3 → do not use

5. TRIANGULATION?
   ≥2 independent sources? LIKELY. Single source? ESTIMATED.

6. GOLDEN WORDS?
   Flag in prose: "Likely" (LIKELY) or "Estimated" (ESTIMATED)

7. DISCLOSE?
   Public-facing report → MUST disclose
   Internal use → log it, keep audit trail

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DONE. Document the proxy, move on.
```

---

## 11. Troubleshooting: Common Proxy Problems & Solutions

### Problem 1: Two Sources Disagree Significantly
1. Check source timestamps (which is more recent?)
2. Investigate the difference (recent hiring? layoff? acquisition?)
3. Use a range instead of a point estimate
4. Correlation confidence stays LIKELY if both are strong sources (data
   quality difference, not proxy failure)
5. Widen the confidence interval in downstream claims

### Problem 2: Proxy Sources Are Too Old
1. Note age explicitly
2. Estimate decay using the reference table above
3. Confidence: ESTIMATED (time decay erodes correlation)
4. Flag in report: "Data age may impact accuracy; refresh recommended"

### Problem 3: Proxy Works in Some Industries But Not Others
1. Validate industry BEFORE applying proxy
2. Document exceptions
3. Apply sector-specific benchmarks if available
4. If sector unknown, confidence → ESTIMATED (or UNKNOWN)

### Problem 4: Proxy-on-Proxy Risk
1. Calculate confidence for each proxy independently
2. Multiply confidence degradation: LIKELY × ESTIMATED = ESTIMATED
3. Disclose stacking explicitly
4. Prefer: break into separate claims, each with a single proxy

### Problem 5: Proxy Becomes Outdated Mid-Report
1. Refresh the proxy before finalizing report
2. Note version timestamp
3. Include refresh window in report
4. Update all downstream claims that depend on this proxy
5. Consider sensitivity analysis

### Problem 6: Stakeholder Doubts Proxy Validity
1. Validate the proxy before the report is submitted
2. Present correlation score
3. Show triangulation
4. Offer a sensitivity range
5. Propose direct data collection if the stakes justify it

---

## 12. Integration with SB Research Phases

| Phase | Proxy Role | Action |
|---|---|---|
| **PLAN** | Identify proxies upfront; set confidence ESTIMATED | List all proxies in the Brief |
| **INTEL** | Source proxies transparently; tag source role | Log every source contributing to proxy |
| **CHECK** | Score sources; validate proxy triangulation | Run source scoring on proxy sources |
| **VERIFY** | Validate proxies; adjust confidence; check for decay | Run the Proxy Validation Checklist; document exceptions |
| **SYNTHESIZE** | Use confidence labels; flag proxy claims | Write claims with confidence tags |
| **REPORT** | Disclose proxies; cite sources; note limitations | Sources block + appendix if complex |

---

## 13. Quick Reference: Proxy vs. Related Concepts

| Concept | Definition | Example | Treated as Proxy? |
|---|---|---|---|
| **Proxy** | Indirect measure correlated with target | Headcount for revenue | YES |
| **Assumption** | Belief about parameter or relationship | Salary assumption | NO (disclosed separately) |
| **Benchmark** | Industry average or peer comparison | Per-employee benchmark | NO (reference, not claim) |
| **Estimate** | Inferred value based on data | Revenue estimate | Depends (if proxy-based, YES) |
| **Inference** | Conclusion drawn from available data | "Company is expanding" | Depends (direct or proxy?) |
| **Interpolation** | Filling gaps using related data points | Inferring one quarter's revenue from others | Possibly |

---

## 14. Advanced: Proxy Validation for Complex Claims

For high-stakes research claims, run extended validation:

```
COMPLEX CLAIM: "Company will achieve $50M ARR by 2027"

1. DECOMPOSE the claim into proxy components:
   → Current revenue (proxy needed?)
   → Growth rate (proxy needed?)
   → Market size (proxy needed?)
   → Competitive position (proxy needed?)

2. FOR EACH COMPONENT:
   ☐ Identify proxy
   ☐ Score correlation (1–5)
   ☐ Triangulate (2+ sources)
   ☐ Check decay rate
   ☐ Document assumptions
   ☐ Calculate confidence (CONFIRMED/LIKELY/ESTIMATED)

3. AGGREGATE confidence:
   All CONFIRMED → Claim: CONFIRMED
   ≥2 LIKELY, rest CONFIRMED → Claim: LIKELY
   ≥1 ESTIMATED → Claim: ESTIMATED
   ≥1 UNKNOWN → Claim: UNKNOWN

4. DISCLOSE:
   "Projected $50M ARR by 2027 (confidence: ESTIMATED — proxies for
    current revenue and growth trajectory; direct market-sizing
    unavailable. Sensitivity: ±$10M band if growth assumptions ±2%)"
```
