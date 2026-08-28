# Answer Key — V-T2: EU AI Act GPAI Compliance Deadlines

**Built:** before any run agent is launched against card V-T2. **Frozen at
commit time** — do not edit after a run has been graded against it; add
an addendum instead.

**Built by:** direct retrieval, not by a run agent. Retrieval attempted
against EUR-Lex directly (`eur-lex.europa.eu`, both URL forms) — **both
attempts returned empty content**, consistent with the reachability
problem stranger test A hit against the same target. Retrieval succeeded
against `artificialintelligenceact.eu`, which the Future of Life
Institute maintains as a verbatim reproduction of the enacted text, and
was cross-checked against secondary reporting (law-firm alerts, a cloud
security research note) for the amendment's scope. **This key is
therefore itself graded at LIKELY confidence on primary-source retrieval
— logged honestly rather than presented as a canonical retrieval this
key-builder did not actually achieve.** A run agent that reaches the raw
EUR-Lex text where this key-building attempt failed should be scored
*higher* on the canonical-source rule, not penalized for disagreeing with
this key's provenance.

---

## The claims, keyed

| # | Claim | Legal basis | Confidence this key assigns |
|---|---|---|---|
| K1 | Chapter V of the AI Act (Articles 53–56, GPAI obligations) applies from **2 August 2025** | Art. 113 | **CONFIRMED** — corroborated across primary reproduction and independent secondary sources |
| K2 | Providers of GPAI models must: (a) maintain technical documentation (Annex XI) · (b) share integration information with downstream providers (Annex XII) · (c) implement an EU-copyright compliance policy respecting Art. 4(3) DSM reservations · (d) publish a training-content summary on the AI Office template | Art. 53(1) | CONFIRMED |
| K3 | The free/open-source exemption covers only (a) and (b) above, not (c) or (d), and does not apply at all to systemic-risk models | Art. 53(2) | CONFIRMED |
| K4 | Systemic-risk GPAI providers must additionally: model-evaluate with adversarial testing · assess/mitigate Union-level systemic risk · report serious incidents without undue delay · maintain adequate cybersecurity | Art. 55(1) | CONFIRMED |
| K5 | A model is presumed to carry systemic risk above **10²⁵ FLOP** of cumulative training compute; the Commission may also designate a model by decision under Annex XIII criteria independent of that threshold | Art. 51 | CONFIRMED |
| K6 | **Article 101 (fines up to 3% of global annual turnover or €15m, whichever is higher) was carved out of the 2 August 2025 tranche** and applies from **2 August 2026** — meaning GPAI obligations were legally binding for a full year before the Commission could fine anyone for breaching them | Art. 113(3), Art. 101 | CONFIRMED |
| K7 | Providers of GPAI models **already on the market before 2 August 2025** have until **2 August 2027** to bring them into compliance | Art. 111(3) | CONFIRMED |
| K8 | Regulation (EU) 2026/1744 ("Digital Omnibus on AI"), published in the OJ **24 July 2026**, in force **27 July 2026**, amended the Act | — | CONFIRMED |
| K9 | **The Omnibus did NOT delay the GPAI obligations in K1–K7.** What it delayed: standalone high-risk (Annex III) obligations, from 2 Aug 2026 to **2 December 2027**; product-embedded high-risk (Annex I), to **2 August 2028**; it also converted the Art. 111(2) grace-period cutoff from a fixed date to one tied to Chapter III's actual application date | Reg. (EU) 2026/1744, amending Arts. 111, 113 | CONFIRMED on the high-risk deferral dates; **ESTIMATED** on "Chapter V itself is textually untouched" — multiple secondary sources state this by omission (describing what changed and not naming Chapter V), not by an affirmative statement that Arts. 53/55/101/111(3) are unamended. A run agent that retrieves Reg. 2026/1744's consolidated text directly and confirms this affirmatively should score above this key. |
| K10 | A narrower, GPAI-adjacent date did move: providers of generative/GPAI systems placed on the market before 2 Aug 2026 get until **2 February 2027** instead of 2 Aug 2026 to comply with **Article 50(2)** (the AI-content transparency/labelling duty — a Chapter IV provision, distinct from the Chapter V GPAI-provider duties in K1–K7) | Reg. (EU) 2026/1744, amending Art. 50(2) application | LIKELY — single secondary source found for this specific sub-date; not independently corroborated within this key-building pass |

## The three dates a run MUST get right, and the trap each sits inside

1. **2 August 2025** — GPAI obligations bind. The trap: many sources
   present this alongside 2 August 2026 or 2027 without distinguishing
   *which* obligations attach to which date. A run that gives one date
   for "GPAI obligations" without separating K1 from K6/K7 has
   under-resolved the question.
2. **2 August 2026** — NOT when GPAI obligations start. It's when Article
   101 fines start, and separately (unrelated to GPAI) when the Digital
   Omnibus's amendments took hold of the high-risk track. A run that
   states "GPAI enforcement" or "GPAI compliance" begins 2 August 2026 is
   **wrong** — enforcement power begins then; the obligations themselves
   began a year earlier.
3. **2 August 2027** — legacy-model compliance deadline (K7), commonly
   confused with the pre-Omnibus Art. 6(1) high-risk classification date,
   which the Omnibus moved. A run conflating these two different "2027"
   dates has failed to disambiguate.

## What "correct enough" looks like for grading

A run passes calibration on this card if:
- K1, K6, K7 are stated correctly with dates and distinguished from each
  other (this is the core of the question — "what obligations, and
  when").
- K9's substance (Chapter V not touched by the Omnibus) is stated at
  LIKELY or higher, sourced, not asserted from memory.
- The run does not conflate the Art. 101 date (2026) with the Chapter V
  application date (2025).
- If the run reaches the raw EUR-Lex or a consolidated-text mirror where
  this key-building pass could not, and CONFIRMS K9 directly from that
  retrieval under the canonical-source rule — that is a **better** result
  than this key, not a disagreement to penalize.

A run fails calibration if it states GPAI obligations begin 2 August
2026 or 2027, or presents the Omnibus as having delayed Chapter V.
