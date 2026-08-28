# SuperBasic™ Research

![License: CC BY-SA 4.0](https://img.shields.io/badge/license-CC%20BY--SA%204.0-blue)
![Red-teamed](https://img.shields.io/badge/red--teamed-4%2F5%20hypotheses%20confirmed-brightgreen)
![Models verified](https://img.shields.io/badge/models%20verified-6%20families-brightgreen)
![Telemetry](https://img.shields.io/badge/telemetry-none-lightgrey)
![No CLA](https://img.shields.io/badge/CLA-none%20required-lightgrey)

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

[**Read this before you rely on it for anything that matters →**](#one-thing-to-know-before-you-use-this)

---

## Quick start

**1. No install — paste it.**

Open [`SKILL.md`](SKILL.md), copy everything in it, paste it into the
start of a conversation with an AI chat **that has live search or
browsing turned on.** Ask your actual research question. The method
should first ask whether it actually has a usable search tool right
now, then what mode to run in (LIGHT or HEAVY).

**2. Programmatic — real tool-calling, verified against 6 model families.**

```python
import sys
sys.path.insert(0, "harness")
import executor, sbr

card = sbr.RunCard({"question": "your real research question", "mode": "LIGHT"})
ctx  = sbr.RunContext({"destination": None})

result = sbr.run_sbr(
    card, ctx,
    agent_executor=executor.make_executor(
        model="anthropic/claude-sonnet-5", backend="openrouter", max_tokens=12000,
    ),
    writer=lambda dest, name, content: {"id": name, "url": None},
)
print(result.status)      # COMPLETE | PARTIAL | STOPPED
```

**3. HEAVY mode — more sources, stricter thresholds, same code.**

```python
card = sbr.RunCard({"question": "your real research question", "mode": "HEAVY"})
# everything else identical — mode is the only thing that changes
```

See [Connect your setup](#connect-your-setup) below for Claude Code,
claude.ai, ChatGPT, Gemini, and running it as part of an agent.

---

## One thing to know before you use this

**Bare-paste mode (step 1 above) can fabricate.** Cross-model testing
found that pasting `SKILL.md` with no real search tool wired into the
request makes some models fabricate entire source tables — fake
outlets, fake dates, fake quotes — and stamp them CONFIRMED using the
method's own scoring apparatus, which reads as *more* credible than a
plain hallucination, not less. **Do not use bare-paste mode for any
claim where being wrong carries real cost.**

**Step 2 (the harness) closes this.** Real tool-calling, verified
across 6 model families — Claude, Gemini, ChatGPT, Mistral, DeepSeek,
Llama — with a formal, pre-registered red-team evaluation against the
enforcement mechanism itself, including one **live-caught fabrication
attempt** that the harness correctly overrode.

| | Where to look |
|---|---|
| The original discovery, the fix, and the full narrative log | [`tests/CROSS-MODEL.md`](tests/CROSS-MODEL.md) |
| The formal evaluation — pre-registered hypotheses, injection resistance, repeat-run consistency, cross-domain generalization, raw evidence for every claim | [`tests/RED-TEAM.md`](tests/RED-TEAM.md) |
| The harness itself — setup, backends, usage | [`harness/README.md`](harness/README.md) |

---

## Model support

Verified live against the harness, not assumed from a vendor name.

| Model family | Status | Notes |
|---|---|---|
| Claude | ✅ Verified | Also the runtime for the 11-card method battery ([`tests/`](tests/)) |
| Gemini | ✅ Verified | Clean across both LIGHT-mode and cross-domain tests |
| ChatGPT (GPT-5) | ✅ Verified | Needed a raised `max_tokens` budget — see [`harness/README.md`](harness/README.md#max_tokens-matters--the-default-will-silently-fail-on-some-models) |
| Mistral | ✅ Verified | Direct backend (bypasses a since-found OpenRouter routing bug); **the one model caught actually fabricating** — 5 of 7 invented sources, all correctly overridden |
| DeepSeek | ✅ Verified | Clean, and correctly resisted a live prompt-injection attack |
| Llama (3.3 70B, cloud) | ✅ Verified | The model a prompt-level gate alone did *not* stop — the harness did |
| Llama (local, via Ollama) | ⚠️ Partial | Real tool-calling confirmed working at the API level; two distinct failure shapes found at 3B and 8B — see [`tests/CROSS-MODEL.md`](tests/CROSS-MODEL.md) |
| Qwen | ✅ Verified (extra) | Not on the required list, tested anyway — clean |

Full methodology and raw evidence: [`tests/RED-TEAM.md`](tests/RED-TEAM.md).

---

## For security teams

- **No telemetry, no phone-home.** Nothing in this repo reports usage,
  errors, or content anywhere. The only network calls the harness makes
  are to the search/LLM providers you configure yourself.
- **Nothing is trusted by default.** The harness's core mechanism exists
  because "the model says it searched" is not evidence — every cited
  source is cross-checked against what a real tool call actually
  returned, in code, not by asking the model to self-report.
- **API keys stay local.** `OPENROUTER_API_KEY` / `TAVILY_API_KEY` /
  `MISTRAL_API_KEY` are read from your own environment; nothing in this
  repo transmits them anywhere but the provider they're for.
- **Adversarially tested, with the design frozen before results
  existed.** [`tests/redteam/PROTOCOL.md`](tests/redteam/PROTOCOL.md)'s
  git history proves the test hypotheses predate the outcomes — not
  fitted to what happened after the fact.
- **Zero disk writes required to run the method itself** — `sbr.py`
  returns documents in memory; where they're written (Drive, local
  disk, nowhere) is entirely up to the `writer` callback you supply.

## For legal & procurement

- **CC BY-SA 4.0** — use it, adapt it, build on it. Share adaptations
  under the same terms. Full text: [LICENSE](LICENSE).
- **No CLA.** Nothing to sign to use, fork, or modify this.
- **SuperBasic™ is a trademark; the method is not.** The process itself
  is open under the license above — the name has separate, narrower
  terms. See [TRADEMARK.md](TRADEMARK.md).
- **Not source-available, not open-core.** There is no paid tier, no
  feature gated behind a license key, and no separate "enterprise"
  version of this repo.

---

## What's in this repo

Three parts, matching how you'd actually use them:

| | What | Where |
|---|---|---|
| **Process** | The method itself — what you must do, in order, with gates that can fail | [`sbr.py`](sbr.py), [`SKILL.md`](SKILL.md) — both at the repo root |
| **Standards** | The depth layer — how to do each step well, opened when the process tells you to | [`standards/`](standards/) — 14 files |
| **Testing** | Proof the method survives adversarial pressure, including one honest miss | [`tests/`](tests/) — an 11-card battery, graded, plus [`tests/RED-TEAM.md`](tests/RED-TEAM.md), a pre-registered formal evaluation of the fabrication-prevention harness |

Read [`PHILOSOPHY.md`](PHILOSOPHY.md) for why any of this exists.

---

## Connect your setup

**Claude Code** — copy `sbr.py`, `SKILL.md` and `standards/` into a skill
folder:

```bash
git clone https://github.com/iamstefanp/superbasic-research.git
cp -r superbasic-research ~/.claude/skills/superbasic-research
```

**claude.ai** — zip the repo (minus `tests/`, which is proof material, not
part of the method) and upload it under Settings → Customize → Skills.

**ChatGPT, Gemini, Cursor, anywhere else** — `SKILL.md` reads as plain
markdown and works as a system/first message anywhere. See
[**One thing to know before you use this**](#one-thing-to-know-before-you-use-this)
first — bare-paste mode's limitations apply everywhere it's pasted, not
just in one client.

**Programmatically, with real tool-calling** — use `harness/executor.py`
directly (see [Quick start](#quick-start) above and
[`harness/README.md`](harness/README.md) for backend options: OpenRouter,
Mistral direct, or local Ollama).

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

Two layers of testing, both published in full, both including the honest
miss rather than only the wins:

**The method itself** — [`tests/`](tests/) is an 11-card adversarial
battery, each card built around a specific trap the method has to
survive: sources that look independent but share one origin, catalogs
that genuinely disagree, entities that collide under one name, evidence
that's paywalled rather than absent, the same brief run three times blind
to check whether the method reproduces or just guesses well once. Every
run is graded by an adversarial judge with no memory of writing the
method, who independently re-fetches sources rather than trusting the
transcript. Most cards passed; one (the replication card) did not clear
its own bar, and that failure is logged in the open — see
`tests/RESULTS.md` and `tests/FINDINGS-MEMO.md`.

**The fabrication-prevention harness** — [`tests/RED-TEAM.md`](tests/RED-TEAM.md)
is a formal, pre-registered evaluation of `harness/executor.py`: 5
falsifiable hypotheses frozen in [`tests/redteam/PROTOCOL.md`](tests/redteam/PROTOCOL.md)
*before* any test ran, adversarial prompt injection, direct attacks on
the URL-enforcement mechanism, repeat-run consistency, cross-domain
generalization — with raw, committed evidence for every claim under
`tests/redteam/evidence/`. 4 of 5 hypotheses fully confirmed; the fifth's
Mistral leg is an honest INCONCLUSIVE from a real API outage
mid-evaluation, disclosed as a dated protocol amendment, not smoothed
over.

```
tests/
  BATTERY.md            the 11 cards (method battery)
  RUBRIC.md              gates, scoring, verdict format
  RESULTS.md              the registry, one row per graded run
  CORRECTIONS.md           the change log — including a reopened finding
  FINDINGS-MEMO.md          the one-page report card
  capability-ledger.md      known-blocked domains, demonstrated per-run
  answer-keys/V-T2.md       the one frozen ground-truth key
  check_run.py, structural_precheck.py   mechanical checkers

  CROSS-MODEL.md         the fabrication discovery + fix, narrative log
  RED-TEAM.md            the formal harness evaluation (published report)
  redteam/                the evaluation itself
    PROTOCOL.md            frozen hypotheses, severity taxonomy, evidence policy
    test_*.py               5 standalone, re-runnable test files
    evidence/                raw, committed evidence per run
```

---

## Development

The red-team suite in `tests/redteam/` is designed to be re-run, extended,
and pointed at new models — each test file runs standalone:

```bash
python3 tests/redteam/test_enforcement_near_miss.py   # no API needed, seconds
python3 tests/redteam/test_prompt_injection.py
python3 tests/redteam/test_repeat_consistency.py
python3 tests/redteam/test_cross_domain.py
python3 tests/redteam/test_heavy_mode.py
```

This suite also runs in CI — see [`MAINTENANCE.md`](MAINTENANCE.md) for
the full trigger taxonomy (new model releases, failure reports, silent
provider drift, and more), the schedule, and how to add a new model.

Adding a new model to the model-support table above means adding it to
the relevant test file's target list and re-running — the harness code
itself doesn't change. See [`tests/redteam/PROTOCOL.md`](tests/redteam/PROTOCOL.md)
for the hypotheses each test is checking and the evidence format expected.

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
