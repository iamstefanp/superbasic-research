# Source Profiles

Training material on creating and evaluating source profiles during
research operations. Agents need a standard method to document source
characteristics, access experience, and reusability constraints before
scoring. Use this guide during INTEL to create profiles; reference it
during CHECK/VERIFY/SYNTHESIZE to contextualize decisions.

## Introduction

A **source profile** is the operational record of your interaction with
a single source. It captures not the content (that goes to Source
Scoring), but the *experience* of accessing, understanding, and
evaluating the source itself. Think of it as the metadata layer: where
you went, what barriers you hit, how deep you got, what biases you
observed, whether this source can be reused for future research.

Source profiles exist because sources are not interchangeable. A
peer-reviewed journal article, a company's LinkedIn job posting, a
journalist's Twitter thread, and an analyst's presentation deck all look
different when you actually sit down with them. The profile documents
those differences in a way that feeds directly into two downstream
decisions: (1) **Source Scoring** — your 30-point evaluation of
reliability, (2) **Reusability flagging** — whether this source is worth
preserving and citing in future research on the same topic. Together,
they form the audit trail that lets you (and your successor agents) trace
why a given claim got its confidence level (CONFIRMED/LIKELY/ESTIMATED/UNKNOWN).

Profiles serve three critical functions in the research pipeline:

1. **CHECK phase** — When you're validating whether your source pool is
   complete, profiles show you what ground you've actually covered. "I
   found 5 sources on X topic" is incomplete. "I found 3 news articles, 1
   industry report, and 1 company direct statement — here's the barrier
   preventing academic papers" is actionable.

2. **VERIFY phase** — When you're cross-checking claims, profiles remind
   you of each source's angle and blind spots. A CEO's press statement
   and an employee's Glassdoor review contradict on "company culture."
   The profile tells you why they're not equally reliable sources for
   that claim, even if both scored 20+ points.

3. **SYNTHESIZE phase** — When you're synthesizing findings into a
   report, profiles give you the context to explain *how* you know what
   you know. Why is this claim CONFIRMED vs. ESTIMATED? Because three
   sources (with these profiles) converged on it, or because one credible
   source said it and nobody contradicted it.

Profiles are created once, during INTEL, and then live in the Source
Registry as a permanent record. They are not rewritten. They are
referenced.

---

## What Source Profiles Capture

A source profile contains five core dimensions, each with specific fields
and scoring guidance. Think of it as the answer to: *"What happened when
I visited this source, what did I find, what couldn't I access, and what
should the next agent know?"*

**The five dimensions are:**

1. **Access Experience** — The practical logistics of getting to the
   source and moving through it
2. **Content Depth** — How much of the source you examined and the
   richness of what you found
3. **Observed Biases** — The source's angle, incentives, and blind spots
4. **Reusability Rating** — Whether this source is trustworthy enough to
   cite in future research and what conditions apply
5. **Metadata Capture** — The audit trail (URL, date, format, how to
   cite it)

Each dimension feeds directly into Source Scoring and downstream
decision-making. The profile is not subjective — it is factual
description of your experience, with observed bias being the closest to
interpretation (but still grounded in evidence).

---

## Deep Sections: The Five Dimensions of a Source Profile

### 1. Access Experience

**Why This Matters**

Research halts at barriers. If you can't reach a source, you can't score
it or extract claims from it. If you can reach it, but it takes 40
minutes of authentication, the profile captures that cost. Future agents
need to know: did we exhaust this source, or does it have gated layers we
didn't penetrate?

Access experience is not about whether the source is paywalled (that's
metadata). It's about: *How long did it take to get to the actual
content? What surprised you? What was locked away?* These details affect
source reliability scoring (a rushed, shallow visit may mean you missed
important caveats) and reusability (can the next agent repeat your
access, or did you hit a temporary gate?).

**What to Document**

- **Timeframe to access:** How long from decision to first usable
  content? (Minutes: instant / 5–15 min / 15–60 min; Hours/Days: if
  authentication or special request required)
- **Barriers encountered:** None / Paywall / Registration required /
  Authentication (special credentials) / Geographic block / Age gate /
  Search-based (had to dig to find relevant content)
- **Authentication required?** None / Standard email sign-up / Special
  access request / Credential-based (API, institutional, paywall) /
  Workarounds used (describe)
- **Special access conditions:** Any temporary token? Time-limited view?
  Limited by device or location? Cached/archived version?
- **Depth of navigation:** Surface-level (landing page + one sub-section)
  / Mid-level (explored 3–5 sections) / Deep dive (spent 20+ minutes,
  followed internal links)
- **Completeness assessment:** Did you feel you saw the whole source? Was
  there a sense of layers you couldn't reach? (Yes/Partial/No)

**Scoring Guidance**

If a source required instant access and you explored deeply, rate it
**Favorable** for reusability — the next agent can repeat your work. If
it required special authentication or you hit significant barriers, rate
it **Conditional** — it's usable but with friction. If you only saw a
cached version or surface-level content, rate **Limited**.

**Common Mistakes**

- Confusing "I was in a hurry" with "the source was hard to access."
  Document what the source presents, not your time constraints.
- Assuming instant access for one source means all sources of that type
  are equally accessible. A company's press release might be instant,
  but their investor deck might be buried in an archive.
- Not noting workarounds. If you used an archive service (Internet
  Archive, etc.), that belongs in the profile — it changes how the next
  agent accesses it.
- Claiming "completeness" when you only skimmed. Be honest: "I read the
  summary and two key sections" is not the same as "I read the full
  report."

**Real Example**

**Source:** LinkedIn profile of a hiring manager at a regional sports
club

**Access Experience Profile:**
- Timeframe: 3 minutes (instant)
- Barriers: None (public profile)
- Authentication: None required
- Navigation: Surface-level (profile + experience section + recommendations)
- Completeness: Partial — profile public but posts/activity feed not
  available without connection
- Special notes: Profile subject actively posts job listings; updates
  appear recent

**Reusability:** Favorable (accessible anytime, unlikely to change
significantly)

---

**Real Example 2**

**Source:** Industry research report (e.g., an analyst firm on the music
streaming market)

**Access Experience Profile:**
- Timeframe: 45 minutes (required account registration + paywall)
- Barriers: Paywall (pay-per-report model); registration required
- Authentication: Email + password; report token valid for 7 days
- Navigation: Deep (full report explored, all sections reviewed,
  interactive charts examined)
- Completeness: Yes (subscription gives full access; no gated
  subsections)
- Special notes: Report dated Q3; PDF download available; data snapshot
  frozen at report date

**Reusability:** Conditional (paywall requires future agents to purchase
separately; content reliable but time-sensitive, may need
re-subscription for updated version)

---

### 2. Content Depth

**Why This Matters**

A source can be accessible but shallow. You might find a company's blog
post about "our diversity initiatives" in 30 seconds, but if you only
read the headline, you've missed the reported numbers, challenges, and
contradictions that live in the body. Content depth captures: *How much
of the source's actual substance did you examine?* This directly affects
Source Scoring — a high reliability score requires substantial
engagement, not surface-level reading.

Depth also flags when a source has media richness (charts, video, audio)
that adds credibility or reveals bias. A data visualization can show
patterns that narrative text obscures. A video interview can capture tone
and hesitation that a transcript flattens.

**What to Document**

- **Percentage examined:** What % of the source did you actually
  read/view/listen to? (0–25% / 26–50% / 51–75% / 76–100%)
- **Sections/areas covered:** List the main content areas you engaged
  with (e.g., "introduction, methodology, findings, limitations,
  references" vs. "headline and first two paragraphs only")
- **Media richness:** Text only / Text + static images / Text + data
  visualizations / Embedded video / Audio / Interactive elements (charts,
  calculators)
- **Time spent engaged:** Minutes spent actively reading/listening (not
  just time on the page; estimate focused attention time)
- **Density of claims:** Estimate how many factual claims the source
  makes per unit (e.g., "1–2 per paragraph" for analysis piece; "10+ per
  page" for densely-cited report)
- **Caveats and limitations section?** Did the source disclose its own
  limits, methodology caveats, or data constraints? If yes, did you read
  them?

**Scoring Guidance**

Sources examined at 76–100% depth with high media richness and
transparent caveats score higher on reliability. Sources examined at
0–25% depth, even if they seem credible, get flagged as *preliminary* —
they're usable for direction but not for foundational claims. Sources
with no caveats section, especially if dense with claims, warrant
skepticism.

**Common Mistakes**

- Conflating "the source is long" with "I read all of it." A 50-page
  report with an 8-page executive summary is not the same depth as
  reading the full 50 pages.
- Ignoring media. A data visualization can contradict a narrative text.
  The depth score must reflect that you saw both.
- Not reading the caveats. Academic papers and credible reports always
  have a "limitations" section. If you didn't read it, you didn't
  understand the source.
- Assuming all text is equally dense. A news article with 5 claims is
  not the same depth as a technical whitepaper with 50 claims per page.

---

### 3. Observed Biases

**Why This Matters**

Every source has a perspective. A company investor relations page wants
to make the company look good. An activist blog wants to expose a
problem. A news outlet wants engagement. An academic paper wants to
publish findings. None of this disqualifies them — it just explains
where they're coming from. Observed bias is not about "bias = bad." It's
about *what is this source trying to convince me of, and what might it
be blind to?*

Documenting observed bias serves two functions: (1) it helps you
interpret claims correctly (a CEO's statement about profitability is
useful but should be triangulated with third-party audits), and (2) it
flags blind spots that might affect downstream synthesis (if every source
on "artist well-being" is from artist advocacy groups, you're missing the
economics perspective).

**What to Document**

- **Source's stated angle or mission:** What is it trying to do?
  (Inform / Convince / Advocate / Profit / Educate)
- **Funding or ownership:** Who pays for this? (Direct commercial
  interest / Nonprofit agenda / Independent / Venture-backed /
  Advertising-supported) — note if not disclosed
- **Incentive structure:** What outcome would the source benefit from?
- **Tone and language:** Neutral/factual / Advocacy / Persuasive /
  Sensationalist / Technical
- **What it emphasizes:** What aspects get heavy coverage, graphics, or
  prominent placement?
- **What it de-emphasizes or omits:** What relevant information is
  absent?
- **Blind spots or one-sidedness:** Specific limitations in perspective

**Scoring Guidance**

High bias is not automatically a low score. A source with explicit bias
(known agenda, transparent funding, stated perspective) is often more
reliable than one that claims neutrality while harboring hidden bias. The
key is *transparency* and *consistency with downstream checking*. A
CEO's pro-company statement scores higher if you have a contradictory
employee statement or third-party audit to triangulate against.

**Common Mistakes**

- Assuming "scientific" or "academic" means unbiased. Academic papers
  have incentive structures too (publish novel findings, secure grants
  from particular sources, advance career reputation).
- Confusing "I disagree with the conclusions" with "this source is
  biased." Political disagreement is not the same as methodological bias.
- Not investigating funding. A "nonprofit research group" funded by a
  corporation or foundation with a specific agenda is not neutral, even
  if structured as nonprofit.
- Assuming omission = bias without evidence. The absence of a topic from
  a source might be intentional bias, or it might just be out of scope.

**Real Example**

**Source:** A streaming platform's investor-relations blog post on artist
compensation

**Observed Biases Profile:**
- Stated angle: Informational (explaining platform's economics)
- Funding/ownership: The platform itself; author is VP of Public Policy
- Incentive structure: Benefits from appearing artist-friendly and
  transparent; would not publish deeply critical data
- Tone: Professional, measured, with selected positive data points
- Emphasis: Payment mechanisms, volume of artists paid, growth in
  payouts (absolute figures)
- Omissions: Does not address per-stream rates declining over time; does
  not compare payouts to platform revenue; does not surface independent
  artist survival rates
- Blind spots: "Success story" framing; emphasis on aggregate (total
  payout growth) rather than per-artist impact

**Bias Assessment:** Moderate — source has clear incentive to present
positively, but tone is professional (not sensationalist). Reliable for
facts about payment mechanisms; unreliable as sole source for artist
well-being claims. Requires triangulation.

---

### 4. Reusability Rating

**Why This Matters**

Not all research is one-shot. If you find a high-quality source on a
topic today, you might need it again in three months when a new project
asks about the same subject. Reusability rating captures: *Can the next
agent (or you, six months from now) reliably use this source again? Are
there conditions or constraints that limit how much you can depend on
it?*

Reusability is distinct from reliability. A source can be reliable
(well-sourced, transparent, high-depth examination) but time-limited (a
report with a specific quarterly data snapshot, an article from last year
that's no longer current). Another source might be moderately reliable
but infinitely reusable (a founder's biographical information, a
company's founding date, a permanent archive record).

**What to Document**

- **Reusability timeframe:** Is this source's content static or
  time-sensitive? (Static/permanent / Time-limited: [specify] / Rapidly
  outdated / Requires regular refresh)
- **Reusability conditions:** Can any agent access this again under the
  same conditions?
- **Content freshness requirement:** No refresh needed / Annual refresh /
  Quarterly refresh / Monthly refresh
- **Citation constraints:** Can this source be directly cited in reports?
- **Complementary sources needed?** Sufficient / Requires 1 supporting
  source / Requires 2+ supporting sources

**Scoring Guidance**

Rate reusability on a three-tier scale:

- **Favorable:** Source is static, permanently accessible, no paywall
  friction, doesn't require refresh, can be cited directly. Example:
  academic paper in permanent archive, founding date of a company,
  government report.
- **Conditional:** Source has a time-limited component (subscription,
  quarterly data snapshot, changing content), requires refresh annually
  or less frequently, or needs supporting sources.
- **Limited:** Source is time-sensitive, requires special access, rapidly
  becomes outdated, or has high bias requiring multiple supporting
  sources to be usable.

**Common Mistakes**

- Assuming a source that helped you today is "automatically reusable."
  Time sensitivity matters.
- Confusing accessibility (can you get to it?) with reusability (can you
  rely on it staying the same?). A LinkedIn profile is always accessible
  but constantly changes.
- Not documenting the need for supporting sources.
- Rating bias as "therefore not reusable." A biased source is still
  reusable *if you and the next agent understand the bias*.

---

### 5. Metadata Capture

**Why This Matters**

Metadata is the audit trail. It answers the practical question: *How do I
cite this source, and how does the next agent find the exact version I
saw?* The internet changes. URLs shift. Articles get updated. Archives
get moved. Metadata is the insurance against losing track of your
evidence.

Metadata capture is not optional. It is the precondition for Source
Scoring and reusability. A high-quality claim that came from a source you
can't cite again is scientifically worthless.

**What to Document**

- **URL or persistent identifier:** Full URL or DOI. If archived, include
  Archive.org link.
- **Access date:** When you examined this source (YYYY-MM-DD)
- **Version or edition:** If applicable
- **Media type:** Web page / PDF document / Academic paper / Blog post /
  Social media post / Video / Podcast / Interview / Dataset / Image /
  Presentation
- **Author/publisher:** Individual name or organizational name
- **Publication date:** When source was published (not when you accessed
  it)
- **Citation format:** Full citation in APA, MLA, or Chicago style
- **Special notes:** API endpoint used, cached version accessed, behind
  paywall, deleted post (if captured screenshot), etc.

**Scoring Guidance**

Complete metadata increases confidence in source reliability. Incomplete
metadata raises questions about verification. Missing metadata can make a
high-quality source later un-citable if the URL changes or the source
updates between your examination and the synthesis phase.

**Common Mistakes**

- Saving the URL but not the access date.
- Not capturing version info for time-sensitive sources.
- Assuming Archive.org has everything.
- Creating sloppy citations.

---

## Creating Profiles: Step-by-Step Workflow

### When to Create

Profiles are created during the **INTEL phase**. You create one profile
per source as you examine it. Do not batch-create profiles after you've
examined multiple sources — the details will blur. Profile as you go.

### The Template

```
## [Source Name/Title]

### Access Experience
- Timeframe: [instant / 5-15 min / 15-60 min / hours / days]
- Barriers: [none / paywall / registration / authentication / geographic block / other]
- Authentication required: [description if applicable]
- Navigation depth: [surface-level / mid-level / deep]
- Completeness: [yes / partial / no]
- Special notes: [workarounds, archived versions, temporary access, etc.]

### Content Depth
- Percentage examined: [0–25% / 26–50% / 51–75% / 76–100%]
- Sections covered: [list]
- Media richness: [text only / + images / + data viz / + video / + interactive]
- Time spent: [estimate in minutes]
- Density: [claims per unit]
- Caveats section: [yes/no; note if read]

### Observed Biases
- Stated angle: [what it's trying to do]
- Funding/ownership: [who pays]
- Incentive structure: [what outcome benefits it]
- Tone: [neutral / advocacy / persuasive / sensationalist]
- Emphasis: [what gets highlighted]
- Omissions: [what's missing]
- Blind spots: [specific limitations]
- Bias assessment: [low / moderate / high; with reasoning]

### Reusability Rating
- Timeframe: [static / time-limited with duration / rapidly outdated]
- Conditions: [accessibility for next agent]
- Freshness requirement: [none / annual / quarterly / monthly]
- Citation constraints: [yes / with caveats / no]
- Supporting sources needed: [none / 1 / 2+ / as noted]
- Overall rating: [Favorable / Conditional / Limited]

### Metadata
- URL/persistent identifier: [full link or DOI]
- Access date: [YYYY-MM-DD]
- Version: [if applicable]
- Media type: [web page / PDF / academic paper / etc.]
- Author/publisher: [name]
- Publication date: [YYYY-MM-DD]
- Citation format: [full citation]
- Special notes: [archive status, paywall status, etc.]
```

### How to Reference Profiles During Later Phases

**During CHECK phase:** Review all profiles together. Do they show
balanced coverage? "5 profiles all from platform industry sources; 0 from
artist side" flags a gap. Write a brief CHECK summary: "Source pool
covers [X, Y, Z perspectives]; examined at [average depth]; gaps
include [A, B]."

**During VERIFY phase:** When sources contradict, open their profiles.
Do they have different observed biases? Different access depths? This
explains the contradiction. Note in your findings: "Claim [X] is
contradicted by [Source A] and [Source B]. Profile analysis shows
[Source A — high bias but deep engagement] vs. [Source B — neutral but
shallow examination]. Recommend [triangulating with third source /
deepening examination of shallow source]."

**During SYNTHESIZE phase:** When drafting claims, reference the
profiles to justify confidence levels. "CONFIRMED: Three sources
(profiles show 75%+ depth, neutral tone, no observed blind spots on this
claim) converge on this finding." "LIKELY: Two sources support this,
though one has noted bias (profile shows [specific bias]); triangulation
with third source validates the finding despite bias."

---

## Common Pitfalls and How to Avoid Them

### Pitfall 1: Incomplete Profiles
**The Problem:** You rush through a source, create a profile with missing
fields, and later realize you don't have enough detail to use it.
**The Fix:** Treat the template as mandatory. If you can't fill a field,
the source hasn't been examined enough. Incomplete information beats
fabricated information.

### Pitfall 2: Copying Profiles from Other Agents
**The Problem:** Another agent created a profile for Source X; you copy
it into your own registry.
**The Fix:** You can read another agent's profile for context, but if
you're using the source, create your own. Your access experience, depth,
and observed biases might differ.

### Pitfall 3: Bias-Blindness
**The Problem:** You acknowledge bias but then rate the source as
"Favorable" reusability anyway.
**The Fix:** High bias does not automatically mean "don't use it." But
it does mean "use it conditionally, with supporting sources."

### Pitfall 4: Profile Inflation
**The Problem:** You examined 50% of a source but rated it as "high
depth" because you feel confident in what you read.
**The Fix:** Confidence in your understanding is not the same as depth
of examination. Be literal.

### Pitfall 5: Conflating "Outdated" with "Unreliable"
**The Problem:** A source is old, so you rate it as "Limited"
reusability and move on.
**The Fix:** Rate based on the information type, not the publication
date. Timeless methodology stays favorable; time-bound figures don't.

---

## Worked Examples: Three Source Profiles in Full

### Example 1: Company Direct Source (High Bias, Static, Highly Reusable)

**Source:** A regional sports club's official social media account —
statement on community engagement

**Access Experience**
- Timeframe: 2 minutes (instant)
- Barriers: None (public social media)
- Navigation: Surface-level (read 3 recent posts, reviewed pinned
  content)
- Completeness: Partial — posts current; no access to deleted or older
  posts

**Content Depth**
- Percentage examined: 100% of available visible posts (3–5 posts,
  limited sample size)
- Media richness: Text + embedded images
- Time spent: 2 minutes
- Density: 1–2 claims per post
- Caveats: None (expected for social media)

**Observed Biases**
- Stated angle: Self-promotion, brand building, community engagement
- Funding/ownership: The club itself (direct commercial/brand interest)
- Incentive structure: Benefits from appearing community-focused; would
  not post self-criticism
- Tone: Promotional, engaging, positive
- Emphasis: Youth development, community events, achievements
- Omissions: No operational challenges, budget constraints, or internal
  organizational changes

**Reusability Rating**
- Timeframe: Time-limited (content changes frequently)
- Freshness requirement: Monthly
- Citation constraints: Yes, citable as an official statement, but only
  for what the organization claims about itself
- Supporting sources needed: 1–2 (independent verification, third-party
  accounts)
- Overall rating: **Conditional**

**Metadata**
- Access date: [YYYY-MM-DD]
- Media type: Social media posts (text + embedded images)
- Publisher: [Organization]'s official account
- Special notes: Account verified official status; posts reflect current
  organizational priorities as of access date

---

### Example 2: Journalist Reporting (Moderate Bias, Static, Conditional Reusability)

**Source:** Investigative sports journalism article on tournament
economics vs. player development

**Access Experience**
- Timeframe: 15 minutes (free article, no paywall)
- Navigation: Deep (article scrolled entirely, followed one external
  link to source report)
- Completeness: Yes

**Content Depth**
- Percentage examined: 95%
- Media richness: Text + embedded data visualization + embedded video
  interview
- Time spent: 15 minutes
- Density: 4–5 claims per section, heavily cited
- Caveats: No explicit "limitations" section (expected for journalism)

**Observed Biases**
- Stated angle: Investigative journalism; explores a tension
- Incentive structure: Outlet benefits from engagement; may emphasize
  conflict over nuance
- Tone: Investigative, critical, balances multiple perspectives
- Blind spots: Tournament economics from one stakeholder's perspective
  only

**Reusability Rating**
- Timeframe: Static (published article; content doesn't change)
- Citation constraints: Yes, citable as journalism; pair with primary
  sources to verify claims
- Overall rating: **Conditional**

---

### Example 3: Academic Research (Low Bias, Static, Highly Reusable)

**Source:** Academic paper on youth development models and long-term
outcomes — 10-year cohort study

**Access Experience**
- Timeframe: 45 minutes (open-access, no authentication required)
- Navigation: Deep (read abstract, methodology, findings, limitations,
  references; spot-checked three references)
- Completeness: Yes

**Content Depth**
- Percentage examined: 88%
- Media richness: Text + statistical tables + figures
- Time spent: 45 minutes
- Density: 6–8 claims per page, heavily cited (350+ references)
- Caveats: Explicit "limitations and future research" section

**Observed Biases**
- Stated angle: Academic research
- Incentive structure: Academic incentive to publish novel findings
- Tone: Neutral, technical, evidence-driven
- Blind spots: Quantitative focus may miss qualitative aspects; sample
  limits generalizability

**Reusability Rating**
- Timeframe: Static (published research; findings stand unless
  contradicted by later studies)
- Citation constraints: Yes, directly and fully citable
- Overall rating: **Favorable**

---

## Summary: Why Source Profiles Matter

Source profiles are operational discipline. They prevent shortcuts ("I
found it, so it's true"), document rigor (the next agent can see exactly
what you did), and build institutional memory (we know why we trust or
distrust this source, so we don't repeat the work).

They are not optional. They are the foundation of scientific integrity in
research operations. When someone asks, "Why did you rate that claim as
CONFIRMED?" you point to three source profiles showing depth,
convergence, and lack of contradictory sources. That is how research
becomes auditable.

Create them. Reference them. Preserve them.
