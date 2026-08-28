# Source Scoring

**Used at:** VERIFY (Phase 6) — score every source. No source without a score.

Every source is an actor who invested time, money, or motivation to create something. Judging its quality is not about trusting prestigious names or dismissing promotional material wholesale — it is about scoring a small number of distinct dimensions that tell you whether the source deserves your attention and, just as importantly, *how to read it*. A source with a middling total can still be exactly the right source for a specific question. The score does not tell you to like a source. It tells you what weight it can carry.

---

## The scale at a glance

**Every dimension is scored 0–5.** Two modes, depending on the run.

| Mode | Dimensions | Total |
|---|---|---|
| **LIGHT** | Proximity · Recency · Verifiability · Independence · Specificity · Track Record | **/30** |
| **HEAVY** | the six above **plus** Clarity · Expertise | **/40** |

### Bands

| Band | LIGHT /30 | HEAVY /40 | What it means |
|---|---|---|---|
| **GOLD** | 26–30 | 34–40 | Use confidently as primary evidence. Can carry a major claim alone. Cite prominently. |
| **SILVER** | 21–25 | 27–33 | Use with context. Good for corroboration and for carrying a claim alongside one other source. |
| **BRONZE** | 16–20 | 21–26 | Use cautiously. Requires corroboration from a higher band. Good for establishing a pattern, not a standalone fact. |
| **QUESTIONABLE** | 11–15 | 14–20 | Background and landscape only. Never evidence. Limitations flagged explicitly wherever it appears. |
| **REJECT** | 0–10 | 0–13 | Do not use. Go find a better source. |

### The floor rule

**Anything below BRONZE leaves the evidence pool.** A Questionable or Reject source may be mentioned as context — "the trade press has been saying X for two years" — but it may not support a claim, may not be the reason a finding exists, and may not appear in a triangulation set. If removing every sub-Bronze source would change a conclusion, that conclusion is not yet established.

### Choosing the mode

LIGHT is the default: six dimensions, fast, sufficient for most sourcing. Go HEAVY when the run is adversarial, when the finding will be acted on expensively, when the sources are dominated by interested parties, or when the subject is contested and you need to separate *who is telling the truth* from *who is merely transparent about their angle*. Do not mix modes inside one run — a /30 and a /40 are not comparable.

---

## The triage filter: before you score

Do not spend a full evaluation on a source that was never going to matter. Two questions, thirty seconds:

**1. Direct relevance.** Does this source directly address the specific question I am trying to answer *right now*? A founding-history piece may be Gold for the question "what does this organisation believe" and entirely irrelevant to "what are they hiring for this quarter." A product page is not relevant to a regulatory question even when it comes straight from the organisation.

**2. Sufficient signal.** On a skim, does it contain handholds — names, numbers, dates, facts — related to my topic? Can I extract at least one specific insight, or is it all general commentary?

**Action.** If *either* answer is No → mark "Not Relevant" or "Save for Later Context" and move on without scoring. If *both* are Yes → proceed to full scoring. This filter exists to prevent scoring fatigue and to concentrate analytical effort where it changes the outcome.

---

## Scoring each dimension

A note on the **0 anchor**, which is new to this version of the standard: 0 is not "very bad." 0 means *the dimension cannot be assessed at all* or the source actively fails it — an undated page, an author who cannot be identified, a claim with no traceable origin whatsoever. Where the old rubric bottomed out at 1, the honest answer is often 0, and a 0 should feel disqualifying.

---

### 1. PROXIMITY *(LIGHT + HEAVY)*

**How many steps removed is this source from the actual event or subject?**

Information degrades with distance, because every step between the event and the source introduces interpretation, selection, distortion, and delay. Primary sources are not automatically superior — they have their own agendas — but they sit closer to the raw material, before layers of interpretation accumulate. Think of a game of telephone: the first person knows what was said; by the fifth, the message has morphed. Proximity tells you which position in that chain you are hearing from. Getting as close as possible is ideal; when you cannot, you need to know exactly how far away you are.

| Score | Level | What it looks like |
|---|---|---|
| **5** | Primary | Created by the subject themselves — an organisation's own filing, a minister's published statement, a job posting, a press release, an artist's own liner notes, a lab's raw dataset. |
| **4** | Direct observer | Created by someone with firsthand access — a journalist who conducted the interview, an analyst who studied this specific organisation, a customer describing their own transaction, an attendee describing the event they attended. |
| **3** | Informed secondary | Knowledgeable but indirect synthesis — a trade publication covering the trend, research aggregating multiple cases, expert analysis of public information. |
| **1–2** | Distant secondary | A general observer with no direct access — national media picking up a trade-press story, a blog analysing someone else's analysis, an aggregator. Score 2 with some added observation, 1 with none. |
| **0** | Tertiary or untraceable | Pure compilation with no original observation, or a chain you cannot trace at all — encyclopedia entries, database compilations, AI summaries, reference material with no underlying research. |

**How to assess.** Ask how many steps back you would have to trace to verify the information. Zero steps, because they created it → 5. One step, to a direct observer → 4. Two steps, to someone synthesising observers → 3. Three or more → 1–2. Pure compilation, or a trail that goes cold → 0.

**Important distinctions.** A quote inside an article is not primary — the article is a direct observer (4); the speaker's own statement would be primary (5). An organisation's own website *is* primary when the subject is that organisation, because it is a direct artefact of it. An interview counts as direct observer even though the journalist's framing filters it.

---

### 2. RECENCY *(LIGHT + HEAVY)*

*(This dimension was called Timeliness in earlier versions of the standard. Same substance, clearer name.)*

**Does this source still reflect current reality for the thing it describes?**

Information decays at different rates depending on the subject, and recency is not "new equals good" — it is whether the source still describes the world as it is. Regulatory information decays fast, because rules change on a legislative calendar. Operational information — structure, systems, hiring — decays at a moderate pace. Strategic and cultural information — positioning, values, identity — decays slowly, over years. A five-year-old source on an institution's founding values may be more current than a six-month-old piece on a trend that has already turned. Matching the decay rate to the subject is the whole discipline; see **decay-classes.md**, which is set at SCOPE and should already be fixed before you arrive here.

**Score against the class the Scope document already set:**

| Score | FAST subjects | MEDIUM subjects | SLOW subjects |
|---|---|---|---|
| **5** | within 30 days | within 6 months | within 12 months |
| **4** | 1–3 months | 6–12 months | 1–2 years |
| **3** | 3–6 months | 1–2 years | 2–3 years |
| **2** | 6–12 months | 2–3 years | 3–5 years |
| **1** | over 12 months | over 3 years | over 5 years |
| **0** | undated, or predates a known break in the subject that invalidates it | | |

**How to assess.** Identify what the source is actually telling you about; take the decay class for that; find the date the *content* refers to; score against the row.

**Important distinctions.** Publication date and event date differ — an article published today about events from four years ago is scored on the events, not the publication. Update dates count if the piece was genuinely refreshed, but be sceptical of vague "updated" stamps that are SEO housekeeping. And context can override the class: when the world has shifted sharply — a pandemic, a war, a regulation, a change of government, a technology that reset the baseline — pre-break material may be less current than its age suggests. That is the case for a 0 on a dated source.

---

### 3. VERIFIABILITY *(LIGHT + HEAVY)*

**Can the claims in this source be independently checked?**

Verifiable does not mean true. It means *checkable*. The distinction matters enormously: a source full of specific, checkable claims might be lying, but you can catch it; a source full of vague assertions might be entirely truthful, and you can never tell either way. This is falsifiability in Popper's sense — if it cannot be shown wrong, it is not useful as evidence. Verifiability asks whether the source gives you a route back to the underlying fact: attribution, citation, a link to the primary document, a disclosed method, a named person you could call.

| Score | Level | What it looks like |
|---|---|---|
| **5** | Fully traceable | Claims are attributed and sourced; links to primary documents; disclosed methodology with sample and method; you could reconstruct the finding independently. |
| **4** | Mostly traceable | Core claims attributed and checkable; secondary details not; enough of a trail to verify the main narrative. |
| **3** | Partly traceable | Checkable facts mixed with uncheckable assertions; interpretation woven into fact; plausible but hard to confirm without new work. |
| **1–2** | Hard to verify | Mostly assertion. Anonymous sourcing throughout, no citations, opinion presented as fact. Score 2 if one claim can be traced, 1 if effectively none can. |
| **0** | Unverifiable or circular | No sources at all; circular references to other unverifiable material; or claims that contradict everything else available with nothing offered in support. |

**How to assess.** Trace one major claim. Can you get from the sentence to a document, a dataset, or a named person? Then try a second. The proportion of claims that survive that test is the score.

**Important distinctions.** Attribution is not verification — "Smith told me X" lets you verify that Smith said it, not that X is true; that is worth points, but not five of them. Links matter: a piece with ten citations to primary documents outscores an identical piece with none. Disclosed methodology matters: research that states its sample size and method outscores research that states neither. Red flags: "some say," "many believe," "experts think," round numbers with no baseline, and no dates anywhere.

---

### 4. INDEPENDENCE *(LIGHT + HEAVY)*

**Is this source free of conflicts that would bend the information?**

Everyone has motivations. Some align with accuracy and some do not, and that is the whole distinction. Accuracy-aligned: the journalist whose reputation depends on being right, the researcher whose career depends on findings that hold, the auditor whose liability depends on truthful reporting. Not accuracy-aligned: the vendor who profits when the problem sounds urgent, the trade association paid to defend its members, the organisation describing its own performance. Independence does not mean having no motive — it means the motive does not *require* distorting the truth. Ask what the source has at stake in the outcome. High stakes, high risk of distortion.

| Score | Level | What it looks like |
|---|---|---|
| **5** | Independent | No financial or reputational stake in any particular answer — a national statistical office, an academic with no industry funding, an investigative outlet with editorial independence, a third-party auditor carrying professional liability. |
| **4** | Mostly independent | Minor indirect interests with real safeguards — a reporter at a publication with editorial oversight, a researcher with a disclosed and limited industry connection, a professional firm bound by a code. |
| **3** | Mixed | Clear interest, but transparent about it — a consultancy publishing genuine research while hoping to win clients from it, an organisation publishing self-interested but externally checkable operating metrics. |
| **2** | Low | Significant conflict likely to distort — a vendor white paper selling the solution to the problem it describes, an advocacy body with a campaign position, a promotional case study cherry-picking its own wins. |
| **1** | Captured | Wholly aligned to an interest, and not saying so — undisclosed native advertising, astroturf that presents as grassroots. |
| **0** | Captured and deceptive | Actively misrepresents its independence, or the funder is deliberately obscured. |

**How to assess.** Follow the money: who funded this? What do they gain if you believe it — sales, donations, votes, standing? What do they lose if you do not? Are the conflicts disclosed — transparency does not remove a conflict but it makes it manageable? Are there institutional safeguards: an editorial board, peer review, a regulator, legal liability?

**Important distinctions.** Conflict does not make a source useless — a vendor white paper can carry good data if you adjust for the direction of the bias. Independence does not automatically mean good: an independent observer may simply not care enough to get the details right, which is what the other dimensions are for.

---

### 5. SPECIFICITY *(LIGHT + HEAVY)* — **new dimension**

*(New in this version. Carved deliberately out of the old Verifiability dimension, which was doing two jobs at once: is the claim precise, and can the claim be traced. Those are different failures and they need separate scores.)*

**How precise is what this source actually asserts?**

Verifiability asks whether there is a route back to the fact. Specificity asks whether there is a fact there at all. A source can be impeccably cited and still say nothing — every sentence sourced, every claim a generality. And a source can be precise with no citations at all, which is still useful: precise claims can be checked *against other sources*, and a precise claim that turns out to be wrong teaches you something, whereas a vague claim that turns out to be wrong teaches you nothing because it was never pinned down enough to be wrong.

Specificity is about handholds: names (*who*), numbers (*how many*), dates (*when*), places (*where*), and mechanisms (*by what means*). Handholds are what you grab to pull yourself toward the truth.

| Score | Level | What it looks like |
|---|---|---|
| **5** | Sharp | Named actors, exact figures, dated events, stated magnitudes, described mechanisms. Every substantive sentence commits to something that could be shown false. |
| **4** | Mostly sharp | Core claims are specific; surrounding material generalises. Numbers given as ranges rather than points, but real ranges. |
| **3** | Mixed | Specifics and generalities in roughly equal measure. Some named actors, some "a number of organisations." Enough to work with, not enough to build on. |
| **2** | Vague | Directional statements only — "growing," "significant," "many," "increasingly." One or two concrete details float in a sea of commentary. |
| **1** | Empty | All generality. Nothing in it could be shown false. Reads as informative, asserts nothing. |
| **0** | Evasive | Actively avoids specificity where specificity was clearly available — a report on its own results that gives no results, an announcement that names no date, an official statement that describes no action. |

**How to assess.** Take three substantive sentences and ask of each: *what would it take to prove this false?* If you can answer quickly for all three, you are at 4–5. If you cannot answer for any, you are at 0–1. Then count handholds per paragraph — the density is the tell.

**Important distinctions.** Length is not specificity: a long piece can be entirely vague and a two-line filing entirely sharp. Technical vocabulary is not specificity either — jargon frequently substitutes for commitment. And note the interaction with Independence: an evasive 0 on Specificity from a source with a strong stake in the outcome is usually not sloppiness, it is a choice, and it is itself a finding worth recording.

---

### 6. TRACK RECORD *(LIGHT + HEAVY)* — **new dimension**

*(New in this version. Track Record is about demonstrated past reliability, not claimed credentials. Credentials are scored separately, under Expertise, in HEAVY mode only. The two are genuinely different: a source may have every qualification and a history of being wrong, or none of the qualifications and a history of being right first.)*

**Has this source been right before, and can you tell?**

The most useful thing you can know about a source is what happened the last time it made a checkable claim. Institutions and individuals accumulate a record — of corrections issued, of predictions that landed, of stories that held up when contested, of retractions. That record is evidence in a way that a job title is not. A publication with a corrections policy it actually uses is more reliable than one that never corrects anything, because the second is not more accurate, only less accountable.

| Score | Level | What it looks like |
|---|---|---|
| **5** | Proven | A long, checkable history of accurate claims in this domain. Prior findings held up under scrutiny; errors were corrected publicly and promptly; competitors and critics cite it even when it is inconvenient for them. |
| **4** | Strong | A solid record with no known significant failures. Established outlet, agency, or researcher; corrections issued when needed; nothing notable held against it. |
| **3** | Neutral / unestablished | No record either way. New publication, first-time author, an organisation not previously tested on this kind of claim. Not a mark against — simply no history to lean on. |
| **2** | Spotty | Some documented misses — retracted claims, predictions that did not land, findings quietly walked back without acknowledgement. |
| **1** | Poor | A pattern of overreach or error in this domain. Repeatedly wrong on checkable things; corrections resisted or made silently. |
| **0** | Discredited or anonymous | Known fabrication, plagiarism, or a formal finding against it — or fully anonymous, so that no record can attach to it at all. |

**How to assess.** Search the source's name plus "correction," "retraction," or "disputed." Check whether earlier claims by the same source on the same subject can be evaluated with hindsight — did the forecast hold, did the number get revised, did the story survive the response. Check whether a corrections policy exists and is visibly used. For an individual, look at whether people in the field cite them, and whether that citation is approving or as a cautionary example.

**Important distinctions.** Anonymity is a 0 here, not a 3 — the point of Track Record is accountability, and an anonymous source has none, whatever the quality of what it says. Prominence is not a record: a large audience is a distribution fact, not a reliability fact. And a source that has been wrong before but corrected publicly is worth *more* than a source that has never visibly been tested, which is why 4 sits above 3.

---

### 7. CLARITY *(HEAVY only)*

**Is the source transparent about why it created this and what it is trying to accomplish?**

Clarity is not independence. A source can be biased but clear — a vendor saying plainly "we sell this" tells you exactly how to read it — or independent but murky, leaving you wondering why it published this at all and what is unsaid. That distinction is what makes clarity worth its own score: when you know why something was made, you know what lens to apply. Undisclosed motivation is dangerous precisely because you cannot tell whether you are reading information, promotion, advocacy, or something else. Disclosed motivation is manageable, because you can weight for it deliberately. Transparent bias beats hidden objectivity.

| Score | Level | What it looks like |
|---|---|---|
| **5** | Crystal clear | States its purpose outright — labelled advertising, named commissioning client, bylines with credentials, disclosed methodology, regulatory disclosure. |
| **4** | Clearly inferable | Motive obvious from context without explicit statement — a job posting is plainly recruiting, a product announcement is plainly promotional and also informative, an opinion column labelled as commentary. |
| **3** | Mixed | Several motives, some disclosed and some not — thought leadership that both informs and generates leads, a case study that teaches while it advertises, sponsored content with partial labelling. |
| **2** | Unclear | Motive requires detective work — anonymous posts, unbylined content, affiliations that look independent and are not, vaguely institutional voices. |
| **1** | Obscured | Motive appears deliberately downplayed. |
| **0** | Deceptive | Motive actively misrepresented — unlabelled native advertising built to read as editorial, astroturf, undisclosed conflict paired with a claim of independence. |

**How to assess.** Did they tell you why they made this? If yes, high. Can you infer it easily? Moderate. Are you guessing? Low. Are they hiding it? Zero.

**Important distinctions.** Bias plus clarity is a good combination, not a bad one. Unclear is not automatically bad faith — plenty of people simply do not think to disclose. And multiple motives are normal; what matters is whether they are visible.

---

### 8. EXPERTISE *(HEAVY only)*

**Does this source have deep, specific knowledge of the subject it is discussing?**

Knowledge sits in layers — tourist ("I've heard of this"), generalist ("I understand the basics"), domain ("I work in this"), specialist ("this is exactly my field") — and each layer sees different things. Tourists miss nuance; generalists grasp structure but not insider detail; domain practitioners catch subtleties outsiders cannot; specialists see patterns even the domain misses. Expertise matters because experts ask better questions, recognise plausible nonsense, hold the context that shapes interpretation, and can tell signal from noise. It also carries risk: blind spots from standing too close, capture by the consensus of the field, and a tendency to find complexity where there is none. Value deep expertise without worshipping it — specialists see what generalists miss, and generalists occasionally see what specialists cannot.

| Score | Level | What it looks like |
|---|---|---|
| **5** | Deep specialist | Extensive, specific expertise in exactly this domain — a decade or more in this function, published work on this topic, recognised standing, senior lived experience, relevant professional credentials. |
| **4** | Strong domain knowledge | Works in this field with substantial experience — three to ten years in it, practitioners, advisers who serve this sector regularly, correspondents who have held this beat for years. |
| **3** | Informed generalist | Broad knowledge without specialisation — a general business or civic reporter covering many sectors, a consultant with wide but not specific experience, an educated observer. |
| **2** | Adjacent | Relevant knowledge from a neighbouring field — a practitioner in a related industry, an academic background near but not on the subject, a serious amateur. |
| **1** | Outsider | No domain-specific knowledge; general interest only. |
| **0** | Wrong domain, or unidentifiable | Expertise cannot be established at all, or the author is speaking well outside anything they know. |

**How to assess.** Check background for actual experience, not just titles. Look at the depth of detail — does the source demonstrate things only an insider would know? Look for recognition: who cites them, and in what tone? Look for nuance that reveals complexity an outsider would flatten.

**Important distinctions.** Expertise does not imply neutrality — domain experts often hold the strongest biases, through financial stakes or the groupthink of their field. Credentials are not understanding; someone can hold the qualification and miss the practice. And experience is not currency: twenty years of outdated experience is worth less than three years of current experience. Where Track Record and Expertise disagree, trust Track Record.

---

## Worked examples

### A. A job posting from the organisation being researched *(LIGHT)*

An organisation's own posting for a compliance role, published this month, listing title, reporting line, salary band, start date, and named responsibilities. Subject class: FAST (hiring).

| Dimension | Score | Why |
|---|---|---|
| Proximity | 5 | Primary — the organisation created it about itself. |
| Recency | 5 | Within 30 days on a FAST subject. |
| Verifiability | 4 | Publicly posted and checkable against the org's own site and register; no external attribution needed, but nothing to trace beyond the poster. |
| Independence | 2 | The organisation has an obvious stake in how it presents itself. |
| Specificity | 5 | Title, band, date, duties — every element commits to something falsifiable. |
| Track Record | 4 | Established organisation, postings historically reflect real roles. |
| **Total** | **25/30** | **SILVER** |

The interesting move: independence is low and it barely matters, because a job posting is an *artefact* rather than an *account*. It is excellent evidence for "this organisation is hiring for compliance" and poor evidence for "this organisation takes compliance seriously." Score the source, then use it for what it can carry.

### B. A national statistical office release *(LIGHT)*

Official employment statistics with published methodology, released last quarter, subject class MEDIUM.

| Dimension | Score | Why |
|---|---|---|
| Proximity | 5 | The agency collected the data itself. |
| Recency | 5 | Within six months on a MEDIUM subject. |
| Verifiability | 5 | Methodology, sample, and underlying tables published. |
| Independence | 5 | Statutory independence, no stake in the result. |
| Specificity | 5 | Exact figures, defined populations, stated confidence intervals. |
| Track Record | 5 | Long history of revisions published openly. |
| **Total** | **30/30** | **GOLD** |

### C. A vendor white paper *(HEAVY)*

A software vendor's paper arguing that organisations in a given sector urgently need the category of product it sells. Undated survey of "industry leaders," no sample size, disclosed as vendor research.

| Dimension | Score | Why |
|---|---|---|
| Proximity | 3 | Synthesis of others' situations, not observation of a specific case. |
| Recency | 1 | Survey undated; the sector is FAST. |
| Verifiability | 1 | No sample, no method, no citations. |
| Independence | 2 | Sells the solution to the problem it describes. |
| Specificity | 2 | "Many," "increasingly," "leaders report" — one real number in the whole document. |
| Track Record | 3 | New publication series, nothing known either way. |
| Clarity | 4 | Openly branded as vendor research; you know the angle. |
| Expertise | 4 | The authors do genuinely work in the category. |
| **Total** | **20/40** | **QUESTIONABLE** — below Bronze, leaves the evidence pool. |

Note what happened: clarity and expertise are honest strengths, and the source still cannot support a claim. It is useful for understanding what the solutions landscape *says about itself* — a legitimate research question — and it can be cited as context for that. It cannot be cited for the size of the problem.

### D. A cultural institution's annual report *(HEAVY — business domain, added in this version)*

A mid-size civic arts organisation's annual report, published four months ago: audited financial statements, attendance figures broken out by programme, named board and executive, a narrative section on strategy, and a stated methodology for how attendance is counted. Two subjects, two classes — finances MEDIUM, cultural positioning SLOW.

| Dimension | Score | Why |
|---|---|---|
| Proximity | 5 | Primary. The institution reporting on itself. |
| Recency | 5 | Four months, comfortably inside MEDIUM. |
| Verifiability | 4 | Financials audited and traceable to a named auditor; attendance methodology disclosed; the narrative strategy section is assertion only. |
| Independence | 3 | Self-reported, but the financial half carries external audit and legal liability. Mixed, and the mix is uneven across the document. |
| Specificity | 4 | Numbers throughout; the strategy narrative drops to generality. |
| Track Record | 4 | Reports filed consistently for years; prior figures have not been restated. |
| Clarity | 5 | Purpose is explicit and statutory; audience and obligation both stated. |
| Expertise | 4 | Written by the people running the organisation. |
| **Total** | **34/40** | **GOLD** |

The lesson this example carries: **score the part you are using.** This document is Gold for attendance and finances, where audit and disclosed method do the work, and materially weaker for "what is this institution's strategy," where it is an unverified self-description. When a source splits like this, score it for the claim you intend it to support and record which section you scored. One document can legitimately hold two scores in the Source Registry, provided each is labelled by the section it covers.

---

## Non-text sources

The dimensions do not change for non-text media. What changes is where you look for the evidence to score them.

**Video.** *Proximity:* raw footage of an event or an unedited interview is primary (5); an edited documentary or news package is direct observer (4); commentary over someone else's footage is informed secondary (3). *Recency:* score when it was **recorded**, not when it was uploaded — a talk recorded four years ago and posted last week is four years old. *Verifiability:* continuous unedited footage scores high; heavy cutting, jump cuts, and B-roll lower it, because the edit is an unseen interpretive layer. Can you see the speaker clearly enough to confirm identity? Is the audio clean enough to confirm the quote? *Expertise (HEAVY):* score the **subject's** expertise, not the interviewer's — a generalist host interviewing a deep specialist yields a 5 for the content. On a panel, score the participant whose contribution you are actually using. On a documentary, score the interviewees, not the filmmaker.

**Audio and podcasts.** Are speakers identified by name and credential, or introduced only by first name and vibe? Are claims specific enough to check? Is there a transcript — its existence materially raises verifiability, because it makes the content quotable and therefore contestable. Recency again follows the recording date. Note that conversational formats systematically depress Specificity: people speak in approximations, and an approximate spoken figure is a 3, not a 5, however confidently delivered.

**Images.** *Proximity:* a photograph taken at the event is primary (5); the same photograph published in a news story is direct observer (4); a stock image illustrating a concept is 0 — it is not evidence of anything, and should usually be filtered out at triage. *Recency:* when was it taken? Metadata and context clues — signage, seasons, models of equipment, what people are wearing — carry the answer. *Verifiability:* can you confirm location, date, and context through metadata or independent corroboration, or is it an undated, unlabelled frame? Treat an image with stripped metadata and no corroborating context as unverifiable.

**Data visualisations.** *Proximity:* a raw dataset with methodology is primary (5); a chart built by an analyst with access to the data is direct observer (4); an infographic assembling several sources is informed secondary (3). *Verifiability:* is the underlying data accessible (5)? Is the methodology disclosed (4–5)? Is it a chart with no source note at all (0–1)? *Specificity:* check the axes. Unlabelled axes, truncated baselines, and index values with no stated base are specificity failures dressed as precision — the chart looks quantitative and commits to nothing.

**Live and real-time content.** Score 5 on recency while it is genuinely live, but record that the score expires — live content becomes historical the moment it ends, and a scored-at-5 live source is a 5 *as of the timestamp you scored it*. Always record the timestamp alongside the score.

---

## Recording the score

Every scored source carries its dimension scores, its total, its band, and its mode into the Source Registry — not just the band. The band is what governs use; the dimension scores are what let a later reader see *why* a source was trusted, and what would have to change for it to be trusted more. A Bronze source that is Bronze because it is old is a different problem from a Bronze source that is Bronze because it is captured: the first can be replaced with a newer version of itself, the second cannot be fixed at all.
