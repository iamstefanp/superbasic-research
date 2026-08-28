"""
sbr.py — SuperBasic™ Research
=============================

THIS FILE IS THE METHOD. You are the runtime.

There is no main(). You are main(). Read this file top to bottom and
execute it. Every threshold here is a number, not an adjective, because
prose invites interpretation and code invites execution.

WHAT THIS IS FOR
    Not a research methodology that happens to be used by agents — an
    agent control system that happens to produce research. It exists to
    stop the two failures of AI research:

      1. Making things up. A model fabricates when it has no legitimate
         way to say "I could not find this." So this method gives it one,
         and requires it.
      2. Having no process. Left alone a model improvises: searches a
         little, decides that is enough, writes something confident.

    The phases exist to break the work into pieces small enough that you
    cannot drift inside one.

TWO LAYERS
    THIS FILE     control     — what you must do. Non-negotiable.
    standards/   competence  — how to do it well. Consulted on demand.

WHO EXECUTES THIS
    agent_executor (the callable run_sbr() takes) can be anything that
    matches its contract. It does NOT have to be a real tool-using
    agent — and testing found that gap matters: pasted as a bare system
    prompt with no real search tool wired in, some models fabricate
    sources and dress the fabrication in this method's own scoring
    language (tests/CROSS-MODEL.md). harness/executor.py is a reference
    agent_executor backed by real function-calling and a real search
    API — the harness inserts genuine tool results into the
    conversation and overrides any source whose URL didn't actually
    come from one, rather than trusting the model's self-report. Use it
    when the sourcing needs to be real, not just formatted like it is.

Locked S270826-2 (2026-08-27). Supersedes all prior statements of the process.
"""


# ─────────────────────────────────────────────────────────
# TOOL ACCESS — checked before anything else, including the Laws
# ─────────────────────────────────────────────────────────
# Found by testing this file's prose form (SKILL.md) against models with
# no search tool wired into the request: two of six — pasted in as a bare
# system prompt, no callable tool — produced full, formatted reports
# anyway. Fake dates, fake outlets, fake quotes, run through this
# method's own scoring apparatus and stamped CONFIRMED. Two independent
# fabrications of the same fact didn't even agree with each other.
#
# This is a categorically different failure from anything the Laws
# address. The Laws are behavioural constraints on a capable agent —
# they assume you CAN search and are choosing whether to cite honestly.
# A model with no search tool at all cannot search, full stop, no matter
# what it types. Narrating a search under those conditions is not a
# lapse in discipline; it is impossible to be anything other than
# fiction. So this is checked first, before Phase 1, as a precondition
# for whether the method can run at all — not as Law 11, which would
# imply it is one more thing to remember to do well.
#
# THE CHECK, before writing a single word of BRIEF:
#   Do you have a callable search or fetch tool in THIS environment,
#   right now — not "can models like me generally browse," but does
#   THIS request give you one you can actually invoke?
#
#   NO  → Say so, plainly, in one sentence. Do not open Phase 1. Do not
#         produce a Report. Do not narrate what a search would probably
#         find. The honest output of a tool-less request is "I cannot
#         run SuperBasic Research here — I have no search tool," and
#         nothing else.
#   YES → Proceed to Phase 1. When you search, cite the literal tool or
#         function you called, not a paraphrase of what you imagine
#         it returned.
#
# There is no code in this file that can verify a self-declared "YES" is
# true — that verification only exists where the runtime itself inserts
# tool results the model cannot author (see README, "Running it for
# real"). What this file CAN enforce mechanically: a declared "NO" must
# actually stop the run. gate_tool_access() below is that enforcement.

TOOL_ACCESS_CHECK = (
    "Before anything else — before the Laws, before Phase 1 — answer "
    "one question honestly: do you have a callable search or fetch tool "
    "in this environment, right now? Not whether models like you "
    "generally can browse — whether THIS request gave you one. If no: "
    "say so in one sentence and stop. Do not open BRIEF. Do not narrate "
    "a search you cannot perform — that produces a report that LOOKS "
    "sourced and is actually invented, which is worse than refusing."
)


def gate_tool_access(tool_access: bool) -> tuple:
    """
    The precondition gate, run before Phase 1 exists.

    `tool_access` is the agent's own declaration. This function cannot
    verify the declaration is honest — only that anything other than an
    explicit `True` actually halts the run rather than being quietly
    treated as a pass. An omitted field is not a pass; it is the same
    failure to declare that this gate exists to catch.
    """
    if tool_access is True:
        return (True, [])
    reason = ("not declared at all" if tool_access is None
              else f"declared {tool_access!r}")
    return (False, [f"TOOL ACCESS — {reason}; run stops here. "
                     "No Report, no claims, nothing to verify."])


# ─────────────────────────────────────────────────────────
# THE LAWS
# ─────────────────────────────────────────────────────────
# Read before anything executes. Every law is a prohibition, so every
# law can be checked. Breaking one does not make the run worse — it
# makes it not a SuperBasic run.

LAWS = {
    "evidence": [
        "1. No claim without a source you can check.",
        "2. No source without a score.",
        "3. Never from memory. Memory can start a search. It can never end one.",
        "4. Common origin is one source. Three articles from one press "
        "release is one source wearing three hats.",
    ],
    "honesty": [
        "5. Not finding is a finding. State what you looked for and did not get.",
        "6. Every claim carries its confidence.",
    ],
    "process": [
        "7. Mode is locked at the Brief. You do not lower the bar once you "
        "see how hard it is.",
        "8. Phases run in order. No skipping, in any mode.",
        "9. A phase without its document did not happen.",
        "10. A failed gate sends you back. Never forward with a caveat.",
    ],
}


# ─────────────────────────────────────────────────────────
# MODES
# ─────────────────────────────────────────────────────────
# Locked at Phase 1. Never changed mid-run (Law 7).
# LIGHT is not "skip the phases." It is the same eight phases at a lower
# source floor and a coarser scoring instrument.

MODES = {
    "LIGHT": {
        "min_sources":        3,
        "confirmed_needs":    2,    # independent sources for CONFIRMED
        "scoring_dimensions": 6,
        "scoring_max":        30,
        "documents":          3,
    },
    "HEAVY": {
        "min_sources":        5,
        "confirmed_needs":    3,
        "scoring_dimensions": 8,
        "scoring_max":        40,
        "documents":          8,
    },
}


# ─────────────────────────────────────────────────────────
# SOURCE SCORING
# ─────────────────────────────────────────────────────────
# Every source is scored. No exceptions (Law 2).
# Each dimension is 0–5. LIGHT uses six. HEAVY adds Clarity and Expertise.

SCORING_DIMENSIONS = {
    "LIGHT": [
        ("Proximity",     "How close is this to the actual facts? Is it the "
                          "source, or a report of the source?"),
        ("Recency",       "How current is it, measured against how fast this "
                          "subject changes?"),
        ("Verifiability", "Can someone else check this claim independently?"),
        ("Independence",  "Is this separate from the others in the pool, or "
                          "does it share their origin?"),
        ("Specificity",   "Is it precise? A source can be perfectly clear and "
                          "still say nothing."),
        ("Track Record",  "Has this source been reliable before? Demonstrated, "
                          "not claimed."),
    ],
    "HEAVY_ADDITIONAL": [
        ("Clarity",       "Is it unambiguous? Can it be misread?"),
        ("Expertise",     "Does the author hold domain authority on this "
                          "specific question?"),
    ],
}

# Five bands. The band is what you say; the number is how you got there.
SCORING_BANDS = {
    "LIGHT": {          # out of 30
        "GOLD":         (26, 30),
        "SILVER":       (21, 25),
        "BRONZE":       (16, 20),
        "QUESTIONABLE": (11, 15),
        "REJECT":       (0,  10),
    },
    "HEAVY": {          # out of 40
        "GOLD":         (34, 40),
        "SILVER":       (27, 33),
        "BRONZE":       (21, 26),
        "QUESTIONABLE": (14, 20),
        "REJECT":       (0,  13),
    },
}

# Anything below BRONZE is out of the evidence pool. It may be mentioned
# as context; it may not support a claim.
SCORE_FLOOR_BAND = "BRONZE"

PASSING_BANDS = ("GOLD", "SILVER", "BRONZE")


def dimension_names(mode: str) -> list:
    """The dimension names a source must be scored on, for this mode."""
    names = [d[0] for d in SCORING_DIMENSIONS["LIGHT"]]
    if mode == "HEAVY":
        names += [d[0] for d in SCORING_DIMENSIONS["HEAVY_ADDITIONAL"]]
    return names


def band_for(score: int, mode: str) -> str:
    """Return the band name for a raw score in this mode."""
    for band, (low, high) in SCORING_BANDS[mode].items():
        if low <= score <= high:
            return band
    return "REJECT"


def clears_floor(score: int, mode: str) -> bool:
    """A source below BRONZE cannot support a claim."""
    return band_for(score, mode) in PASSING_BANDS


# ─────────────────────────────────────────────────────────
# CONFIDENCE
# ─────────────────────────────────────────────────────────
# Every claim carries exactly one of these (Law 6). Never TBD. Never blank.
# Never a bare assertion.
#
# The calibration is the signature. An agent claiming to be SuperBasic
# that asserts flatly has drifted, and anyone reading can see it.

CONFIDENCE = {
    "CONFIRMED": "Independently corroborated. LIGHT needs 2 genuinely "
                 "independent sources; HEAVY needs 3. Name them. "
                 "OR: established by a canonical source you retrieved "
                 "yourself — see CANONICAL below.",
    "LIKELY":    "One credible source, uncontradicted. Name it.",
    "ESTIMATED": "Inference or extrapolation. State the inference chain.",
    "UNKNOWN":   "Searched for and not found. This is a finding, not a "
                 "failure (Law 5).",
}


# ─────────────────────────────────────────────────────────
# CANONICAL SOURCES
# ─────────────────────────────────────────────────────────
# A narrow, deliberate exception to Law 4.
#
# Some documents do not REPORT a fact — they ARE the fact. A statute does
# not describe the law; it is the law. You do not corroborate what it says
# by finding someone who read it. You read it.
#
# Without this, nine commentaries on one regulation collapse to one origin
# and "Article 53 requires technical documentation" comes out LIKELY —
# which is not caution, it is wrong.
#
# TWO CONDITIONS, both required. Neither is negotiable:
#
#   1. The claim is about the document's OWN CONTENT — what it says,
#      requires, records or decides. Not about the world beyond it. A
#      statute is canonical on its own text and canonical on nothing else:
#      it does not establish that anyone complies with it, that it works,
#      or that it is a good idea.
#
#   2. You RETRIEVED IT YOURSELF. Not a reproduction, not a quotation, not
#      a search snippet. If you did not open the document, you have a
#      report of a canonical source, which is an ordinary source, and Law 4
#      applies in full.
#
# Condition 2 is the load-bearing one. Certifying a document you never
# opened, on the strength of nine people who say they read it, is the exact
# failure this method exists to prevent — and it is more seductive here
# than anywhere else, because the document is real and public and everyone
# agrees about it.

CANONICAL_SOURCE_TYPES = [
    "Legislation, regulations and statutory instruments, as published in "
    "the official record",
    "Court judgments and tribunal decisions, as issued",
    "Regulatory determinations, enforcement decisions and licence records",
    "Published technical standards, from the standards body",
    "Statutory filings and registry entries (company, land, patent, "
    "trademark), from the registry",
    "Audited financial statements, as filed",
    "Treaties, contracts and signed agreements, as executed",
    "Official statistical releases, from the issuing body",
]

# NOT canonical, whatever it claims about itself: press releases, company
# blogs, "official" statements about anything other than the speaker's own
# stated position, encyclopedias, aggregators, preprints, and any document
# whose authority rests on the author asserting it.
#
# A press release IS canonical on one thing only: that the organisation
# said this, on this date. It is not canonical on whether it is true.


# ─────────────────────────────────────────────────────────
# PERSONA TAXONOMY
# ─────────────────────────────────────────────────────────
# The twelve personas from standards/source-personas.md, named here so
# the gates can check membership rather than trust the label. Full
# definitions live in the reference file; this list exists only so that
# "2 distinct personas" (gate_check DIVERSITY) cannot be satisfied by two
# invented labels that were never checked against the taxonomy — a lazy
# pass on a check the method exists to make hard to fake.

PERSONA_TAXONOMY = [
    "Primary Artifact", "Independent Observer", "Promotional Insider",
    "Captured Expert", "Leaked Document", "Academic Authority",
    "Well-Meaning Generalist", "Anonymous Insider", "Tertiary Compiler",
    "Promotional Authority", "Direct Witness", "Regulatory Authority",
]

MEDIA_MODES = ["Paid", "Owned", "Earned"]


# ─────────────────────────────────────────────────────────
# REFERENCES — the competence layer
# ─────────────────────────────────────────────────────────
# This file tells you WHAT to do. These tell you HOW to do it well.
# Open the relevant one at the phase named. Do not work from memory of
# what they contain (Law 3 applies to your own instruments too).

REFERENCES = {
    "media_index":    ("standards/media-index.md",
                       "98 source types, each classified Paid / Owned / "
                       "Earned with a default persona, plus a balance "
                       "framework and classification decision tree. Use "
                       "at PLAN to choose source classes deliberately."),
    "source_personas": ("standards/source-personas.md",
                        "The twelve source personas. Use at INTEL to tag "
                        "each source, and at CHECK to test whether the pool "
                        "is actually diverse."),
    "source_scoring": ("standards/source-scoring.md",
                       "The rubric per dimension, with worked examples and "
                       "guidance for video, audio and image sources. Use at "
                       "VERIFY."),
    "source_profiles": ("standards/source-profiles.md",
                        "How to document access experience, content "
                        "depth, observed bias and reusability per source, "
                        "not just its score. Use at INTEL, as you visit "
                        "each source."),
    "proxy_labeling": ("standards/proxy-labeling.md",
                       "How to identify, validate and disclose a proxy "
                       "measure when the direct one is unavailable. Use "
                       "at PLAN when a claim has no direct data path, "
                       "and at VERIFY to validate correlation strength."),
    "anomaly_investigation": ("standards/anomaly-investigation.md",
                              "How to investigate a finding that "
                              "contradicts the emerging pattern before "
                              "rejecting, integrating or flagging it "
                              "UNKNOWN. Use at INTEL when you flag one, "
                              "and at VERIFY to run the investigation."),
    "reconciliation": ("standards/reconciliation-protocol.md",
                       "The four-outcome decision framework for what to "
                       "do when two sources contradict each other. Use "
                       "at VERIFY."),
    "assumption_exposure": ("standards/assumption-exposure.md",
                            "The five categories of hidden assumption "
                            "that can reverse a finding, and how to rate "
                            "and disclose their impact. Use at VERIFY to "
                            "identify them, and at REPORT to disclose "
                            "them."),
    "triangulation_map": ("standards/triangulation-mapping-guide.md",
                          "How to map claims to their supporting sources "
                          "and score whether that support is genuine "
                          "triangulation or an echo chamber. Use at "
                          "VERIFY."),
    "hypothesis_evolution": ("standards/hypothesis-evolution-tracking.md",
                             "The Expected/Observed/Actual framework for "
                             "documenting how your hypothesis actually "
                             "moved against the evidence, so CONFIRMED / "
                             "REFUTED / COMPLICATED is a real claim, not "
                             "a formality. Use at SYNTHESIZE."),
    "report_scoring": ("standards/report-scoring.md",
                       "How to score the finished report itself — "
                       "diversity, quality, triangulation, recency, "
                       "depth — separate from scoring the individual "
                       "sources in it. Use at REPORT."),
    "report_checklist": ("standards/report-checklist.md",
                         "What to attach and how to name it, so a report "
                         "is a complete, auditable package rather than "
                         "just a document. Use at REPORT."),
    "decay":          ("standards/decay-classes.md",
                       "How fast different subjects go stale. Use at SCOPE "
                       "to set the recency gate."),
    "independence":   ("standards/independence-test.md",
                       "How to follow a source back to its origin. Use at "
                       "VERIFY. This is the check most often failed and "
                       "least often run."),
}


# ─────────────────────────────────────────────────────────
# TYPES
# ─────────────────────────────────────────────────────────

def _subject_from(question: str) -> str:
    """Best-effort subject label from the question. Labelling only."""
    q = question.strip().rstrip("?")
    for lead in ("what is the", "what are the", "what does the", "what is",
                 "what are", "what does", "who is", "who are", "how does",
                 "how is", "why does", "why is", "what"):
        if q.lower().startswith(lead):
            q = q[len(lead):].strip()
            break
    return (q[:60].rstrip(" ,;:") or "Untitled") if q else "Untitled"


def _run_id_from(subject: str) -> str:
    """Short stable-ish id from the subject. Labelling only."""
    words = [w for w in "".join(
        c if c.isalnum() or c.isspace() else " " for c in subject).split()][:3]
    return "-".join(w.upper()[:6] for w in words) or "RUN"


class RunCard:
    """
    What to research. Produced before the run starts.

    `category` is free text. It shapes the KRQ clusters at Phase 1 and
    nothing else. Person, Organisation, Market, Topic, Claim, Player,
    Team, City — whatever the subject actually is.

    Only `question` and `mode` are genuinely required. Everything else is
    labelling and will be derived if you do not supply it — do not invent
    ceremony you were not given, and do not ask the requester for a run_id
    they have no way of knowing.
    """
    def __init__(self, data: dict):
        self.question = data["question"]
        self.mode     = data["mode"]                      # LIGHT | HEAVY

        if self.mode not in MODES:
            raise ValueError(f"mode must be LIGHT or HEAVY, got {self.mode!r}")

        self.subject  = data.get("subject") or _subject_from(self.question)
        self.category = data.get("category", "Unclassified")
        self.angle    = data.get("angle") or self.question
        self.run_id   = data.get("run_id") or _run_id_from(self.subject)
        self.priority = data.get("priority", "NORMAL")    # URGENT|HIGH|NORMAL

    @property
    def spec(self) -> dict:
        return MODES[self.mode]


class DomainContext:
    """
    Everything domain-specific lives here and nowhere else.

    The method is domain-blind. Football, lead generation, market
    intelligence, legal research — all identical processes. What changes
    is what you inject here, and it changes only how output is framed,
    never what evidence is required.

    Nothing in this class may relax a Law or lower a threshold.

      domain        free text, e.g. "sports broadcast" / "B2B lead research"
      voice         how the output is written, if the domain has a house voice
      deadline_utc  ISO timestamp, if the work is time-boxed
      framing       one line: what the reader of the Report is about to do
      krq_template  domain-specific KRQ cluster names for Phase 1, optional
      lenses        story/angle lenses the domain uses, optional
      extras        anything else the domain needs surfaced in phase headers
    """
    def __init__(self, data: dict = None):
        data = data or {}
        self.domain       = data.get("domain", "")
        self.voice        = data.get("voice", "")
        self.deadline_utc = data.get("deadline_utc")
        self.framing      = data.get("framing", "")
        self.krq_template = data.get("krq_template", [])
        self.lenses       = data.get("lenses", [])
        self.extras       = data.get("extras", {})

    @property
    def hours_to_deadline(self):
        if not self.deadline_utc:
            return None
        import datetime
        try:
            end = datetime.datetime.fromisoformat(
                self.deadline_utc.replace("Z", "+00:00"))
            now = datetime.datetime.now(datetime.timezone.utc)
            return max(0, int((end - now).total_seconds() / 3600))
        except Exception:
            return None


class RunContext:
    """
    Where output goes, and what domain this run belongs to.

    `destination` is deliberately loose. It is a Drive folder ID, a local
    directory, or None for "return it in the conversation." The method
    does not care. This is the only layer that differs between running
    inside an organisation and running on someone's laptop.
    """
    def __init__(self, data: dict):
        self.destination = data.get("destination")
        self.project     = data.get("project", "")
        self.domain      = data.get("domain") or DomainContext()


class PhaseCard:
    """
    Handoff between phases. The doc_id is what proves the phase happened
    (Law 9).
    """
    def __init__(self, phase: int, name: str, outputs: dict,
                 confidence: str, doc_id: str = None,
                 doc_url: str = None, go: bool = True, loop_to: int = None):
        self.phase      = phase
        self.name       = name
        self.outputs    = outputs
        self.confidence = confidence          # HIGH | MEDIUM | LOW
        self.doc_id     = doc_id
        self.doc_url    = doc_url
        self.go         = go
        self.loop_to    = loop_to


class RunResult:
    def __init__(self):
        self.run_id            = None
        self.destination       = None
        self.documents         = {}
        self.report_url        = None
        self.status            = "PENDING"    # PENDING|COMPLETE|PARTIAL|STOPPED
        self.failed_gate       = None         # set when status == PARTIAL
        self.confidence_scores = {}


# ─────────────────────────────────────────────────────────
# PHASES
# ─────────────────────────────────────────────────────────
# BRIEF → SCOPE → PLAN → INTEL → CHECK → VERIFY → SYNTHESIZE → REPORT
#
# Order is not negotiable (Law 8). Most research fails not because of bad
# sources but because of bad sequencing. SCOPE bounds the territory; PLAN
# picks the route through it. You cannot plan a route across unbounded
# ground.
#
# Two loops exist and both are legitimate: CHECK→INTEL and VERIFY→INTEL.
# Looping back is the process working, not failing.

PHASE_AGENTS = {

    1: {
        "name": "Brief",
        "role": "Research Architect",
        "job": """
You set the foundation. A vague brief produces a vague report.

1. Restate the Research Question. One sentence. Answerable. If it contains
   an "and", it is probably two questions — split it and pick one.
2. State the Working Hypothesis. What do you expect to find? Specific
   enough to be wrong. A hypothesis that cannot be refuted is a mood.
3. Define 3–5 KRQ clusters (Key Research Questions) — the facets that
   together answer the main question. If the domain supplies a KRQ
   template, start there and adapt it. Otherwise derive them from the
   question itself.
4. Lock the mode: LIGHT or HEAVY. This is now fixed for the entire run
   (Law 7). You do not get to lower it later because the searching was
   harder than expected.
5. State what a COMPLETE answer looks like. Substance, not word count.

Do not search yet. Do not reason from what you already believe you know
about the subject — that belief is the hypothesis, not the evidence.
        """,
        "doc_schema": [
            "Tool Access — true or false, answered honestly, before "
            "anything else in this document",
            "Research Question — one sentence, answerable",
            "Working Hypothesis — specific enough to be wrong",
            "KRQ Cluster 1 — name + 2–3 sub-questions",
            "KRQ Cluster 2 — name + 2–3 sub-questions",
            "KRQ Cluster 3 — name + 2–3 sub-questions",
            "KRQ Cluster 4 (optional)",
            "KRQ Cluster 5 (optional)",
            "Mode — LIGHT or HEAVY, and why",
            "Done When — one sentence",
        ],
    },

    2: {
        "name": "Scope",
        "role": "Intelligence Mapper",
        "job": """
You map the territory before anyone moves.

1. Source classes: which kinds of source can answer this? Open
   standards/media-index.md and choose deliberately across Paid, Owned
   and Earned. A pool of only Owned sources is an organisation talking
   about itself.
2. Out of scope: what will you NOT research? Hard boundaries prevent
   drift. Name them now; you cannot add them later to excuse a gap.
3. Language scope.
4. Recency gate: how old may a source be? This is not one answer — it
   depends on how fast the subject changes. Open
   standards/decay-classes.md.
5. Anticipated tensions: where do you expect sources to disagree? Writing
   this now stops you treating disagreement as an error later.

Still no searching.
        """,
        "doc_schema": [
            "Source Classes — chosen, with Paid/Owned/Earned balance stated",
            "Out of Scope — hard boundaries",
            "Language Scope",
            "Recency Gate — and the decay reasoning behind it",
            "Anticipated Tensions",
        ],
    },

    3: {
        "name": "Plan",
        "role": "Research Strategist",
        "job": """
You sequence the work. Scope said where; you say in what order.

1. Named source pool: 8–15 specific sources — actual outlets, databases,
   registries, people. Not categories. "Trade press" is a class;
   "Modern Retail" is a source.
2. Search queries: 5–10, each targeting one KRQ cluster. Specific.
   A generic query returns generic results and you will mistake volume
   for coverage. Not "Acme Logistics problems" but "Acme Logistics
   warehouse automation capital expenditure 2025 annual report".
3. Trip plan: map each query to its KRQ. Any KRQ with no query is a
   cluster you are about to fail.
4. Priority order: most time-constrained first; primary before commentary.
5. Canonical check, per KRQ cluster: could a canonical document plausibly
   answer this one (a statute, a filing, a judgment, a standard, audited
   accounts — see CANONICAL SOURCES)? If yes, name it and make retrieving
   it the first query for that cluster, not a stretch goal. Two agents
   given the identical brief will drift onto different secondary sources
   for the same cluster — that is not a failure, it is what open search
   does — but they will converge on the same primary document if both
   actually go looking for it. This is the difference between a cluster
   that is merely COVERED and one that is covered *reliably*.
6. Contingency: for each critical source, what is the fallback if it is
   unavailable or paywalled?
        """,
        "doc_schema": [
            "Named Source Pool — 8–15 specific sources",
            "Search Queries — 5–10, each with its KRQ target",
            "Trip Plan — query to KRQ map",
            "Priority Order",
            "Canonical Check — per KRQ: does one plausibly exist, and is "
            "retrieving it queried for first",
            "Contingencies",
        ],
    },

    4: {
        "name": "Intel",
        "role": "Field Researcher",
        "job": """
You go and get it. This is the only phase that searches.

1. Execute every query from the Plan. Every one. A query skipped is a
   gap you will not know you have.
2. For each result record: Source Name · the exact literal query string
   you used to find it · a full, resolvable URL (a real scheme and
   domain — never a placeholder like "example.com" or a bare "various
   outlets") · Publication Date · Accessed Date · Persona · Media Mode ·
   Key Facts · Confidence. Tag persona from
   standards/source-personas.md's twelve named personas — exactly one of
   them, not a paraphrase. Tag media mode as Paid, Owned or Earned. A
   gate at CHECK will reject a tag that isn't one of these, and a gate at
   VERIFY will reject a URL that isn't real. If you cannot produce an
   actual, resolvable URL, the source is UNKNOWN — do not populate the
   field with something that merely looks like one.
3. Capture, do not analyse. Interpretation is Phase 7's job. Analysing
   now means you stop looking once you have a story.
4. Log every attempt, including the ones that found nothing. A search
   that returned nothing is data about the world (Law 5).
5. Flag anomalies — anything contradicting the emerging picture. Do not
   average it away. Do not quietly drop it.
6. Coverage check: does every KRQ cluster have at least one finding?
   Name the ones that do not. Where PLAN flagged a canonical document for
   this cluster, record whether you actually retrieved it — a cluster
   covered only by secondary description, when a primary was named and
   available, is a weaker finding than the schema's PASS/FAIL alone shows.
   Say so here rather than letting it surface as a surprise at VERIFY.

A source you could not open is not a source. Record the failure; do not
substitute something else and move on.

A SEARCH RESULT IS NOT A SOURCE. A snippet, summary or preview returned
by a search engine tells you a document exists and roughly what is in it.
It cannot support a claim. Open the document. If you cannot open it, the
claim it would have supported is UNKNOWN and the attempt is a failed
retrieval — not a citation with a shrug attached. This is the most common
way a run quietly stops being sourced: the snippet said it, so it felt
read.

If a source is canonical for your question — legislation, a judgment, a
standard, a filing, audited accounts — retrieving the document itself is
worth several failed attempts at a commentary about it. See CANONICAL
SOURCES: a canonical document you opened yourself can carry a claim alone.
Nine people who read it cannot.

NEVER FILL A GAP FROM MEMORY (Law 3). If you did not find it, the answer
is UNKNOWN. A plausible fabrication is the worst possible output — it is
indistinguishable from good work until someone acts on it.
        """,
        "doc_schema": [
            "Intel Items — source · query_used (the literal search "
            "string) · URL (real, resolvable — UNKNOWN if none) · "
            "published · accessed · persona (one of the twelve) · "
            "media mode (Paid/Owned/Earned) · facts · confidence "
            "(repeat per find)",
            "Failed Retrievals — what would not open, and what you did",
            "Anomalies — findings that contradict the emerging picture",
            "KRQ Coverage — per cluster: COVERED or GAP, and CANONICAL or "
            "SECONDARY where PLAN flagged a canonical document for it",
            "Searched And Not Found — explicit list (Law 5)",
        ],
    },

    5: {
        "name": "Check",
        "role": "Pool Validator",
        "job": """
You decide whether the pool is sufficient to proceed. Binary: GO or LOOP.
You are not assessing whether the findings are interesting. You are
assessing whether there are enough of them, spread widely enough.

Run every check. Report the number you actually counted, not an impression.

  COUNT      — retrieved sources ≥ mode minimum
  COVERAGE   — every KRQ cluster has at least one finding
  DIVERSITY  — at least two source personas, and not all one media mode
  CORE       — the central research question is not UNKNOWN

Sources are NOT scored yet — that is Phase 6. Count what you actually
retrieved. Anything you could not open does not count here or anywhere.

A cluster with some sub-questions unanswered still counts as COVERED.
Those unanswered parts belong in Searched And Not Found, not in a loop.
Loop for a cluster you never looked at, not for a fact you established
is not on the record — that fact is a finding (Law 5).

If any check fails: LOOP TO Phase 4, name the failing check, and write
the exact gap-fill queries. "Do more research" is not gap-fill guidance.
        """,
        "doc_schema": [
            "COUNT — n sources at/above BRONZE vs minimum — PASS/FAIL",
            "COVERAGE — per KRQ cluster — PASS/FAIL",
            "DIVERSITY (persona) — n distinct personas present, ≥2 "
            "required — PASS/FAIL",
            "DIVERSITY (media mode) — n distinct media modes present, "
            "≥2 required — PASS/FAIL",
            "CORE — is the central question answerable — PASS/FAIL",
            "DECISION — GO or LOOP",
            "If LOOP — failing check, reason, exact gap-fill queries",
        ],
    },

    6: {
        "name": "Verify",
        "role": "Source Sceptic",
        "job": """
You are the last line before conclusions. You trust nothing until it
earns trust.

1. Score every source. Open standards/source-scoring.md for the rubric.
   LIGHT: six dimensions, out of 30. HEAVY: eight, out of 40.
   Record every dimension by name, not just the total — the gate below
   checks that the dimensions are all present and actually sum to the
   total you report. A total with no shown working fails.
   Anything below BRONZE leaves the evidence pool.
2. Test independence properly. Open standards/independence-test.md.
   Follow each source back toward its origin. Sources sharing an origin
   collapse into one, and you recount after collapsing (Law 4). This is
   the check most often skipped and the one that most often turns a
   confident report into a wrong one. For every source, write one line
   (`origin_trace`) stating either that it IS the origin — a first
   mention, not a report of one — or naming what you traced it to and how.
   Setting `origin` without `origin_trace` is the domain-counting shortcut
   this step exists to prevent, and the gate below rejects it.
3. Assign confidence to every claim. CONFIRMED needs genuine independent
   corroboration at the mode's threshold — name the sources.
4. Reconcile anomalies. Where sources disagree, record both versions and
   your decision about how to treat the disagreement. Do not silently
   pick the convenient one.
5. Expose assumptions. What are you treating as true that no source
   established?

Then run the exit gate below. It can fail, and that is the point.
        """,
        "doc_schema": [
            "Scored Source Table — source · every dimension named and "
            "scored · total (must equal the sum of the dimensions) · band",
            "Independence Map — origin and origin_trace per source (how "
            "each was actually traced, or why it IS the origin), which "
            "sources share an origin, and the recount after collapsing",
            "Claim Table — claim · sources · confidence",
            "Contradictions — claim, both versions, decision taken",
            "Assumptions — what is being taken on trust",
            "GATE — the five checks, each PASS/FAIL",
            "DECISION — PASS or LOOP",
        ],
    },

    7: {
        "name": "Synthesize",
        "role": "Meaning Maker",
        "job": """
You turn verified evidence into meaning. You may not introduce a single
fact that did not pass Phase 6.

Use OAC:
  Observe   What does the evidence actually say? No interpretation yet.
  Analyse   Where is the tension, the pattern, the arc?
  Create    What does this mean for the person who asked?

1. Synthesis: an argument, not a summary. What do we now know that we did
   not before, and why does it matter?
2. Tensions: where the evidence pulls in two directions. Anomalies belong
   here as evidence of complexity, not as errors to be tidied.
3. Hypothesis evolution — state the original, state what the evidence
   showed, and mark exactly one:
       CONFIRMED  the hypothesis held
       REFUTED    the hypothesis was wrong
       INVERTED   the opposite turned out to be true
       EXPANDED   it held, but the thing is larger than assumed
4. Gaps: what remains unknown, and what it would take to close it.

If the domain supplies a voice or lenses, apply them here. Voice changes
how this reads. It does not change what is claimed.
        """,
        "doc_schema": [
            "Synthesis — an argument, not a summary",
            "Tensions — where evidence pulls in two directions",
            "Hypothesis — Original",
            "Hypothesis — What The Evidence Showed",
            "Hypothesis — Status (CONFIRMED / REFUTED / INVERTED / EXPANDED)",
            "Patterns",
            "Remaining Gaps — and what would close them",
        ],
    },

    8: {
        "name": "Report",
        "role": "Output Architect",
        "job": """
You produce the deliverable. It must stand alone — read by someone with
no memory of this run. It is read by two different people at once: one
who wants the answer, and one who needs to check your work. Write for
both, in that order, in two clearly separated parts. Do not interleave
them — cold readers of earlier reports named this exact friction:
confidence tags on every sentence and a Band/Persona table sitting where
the answer should be read as "performing rigor for an audience other
than me." The rigor is not optional. Where it lives on the page is.

PART ONE — FOR THE READER. Plain prose. No inline confidence tags, no
bands, no personas, no tally. Confidence still matters, but say it in
words a person would actually say out loud — "well-supported, but I
couldn't independently confirm it" rather than "*Confidence: LIKELY*."
1. Answer the research question directly, in the first paragraph.
2. Key findings, each explained in a sentence a non-expert would
   understand, confidence woven into the sentence rather than tagged
   onto it.
3. What's genuinely not known — the gaps that matter to a decision,
   plainly stated.
4. What you'd actually do with this, if it were your decision.
If any gate failed and the run proceeded on maximum loops, PARTIAL is
stated here too, in the first paragraph, in plain words — not only in
Part Two's status line. A reader who stops after Part One must still
learn the run didn't fully resolve.

PART TWO — THE RECORD. Headed clearly as the audit trail, not required
reading. Everything Part One asserts must be traceable here.
1. Status — COMPLETE or PARTIAL, and which gate failed if PARTIAL.
2. Claim table — every claim, its sources, its confidence label.
3. Sources — name, a full resolvable URL (real scheme and domain — if
   you cannot produce one, the source belongs in Searched And Not Found
   instead, not here with a placeholder), date, band, persona.
4. Searched And Not Found (Law 5) — full list, "nothing" if genuinely
   nothing, section never omitted.
5. Confidence summary — count per label.
6. Assumptions and Limitations.

A complete-looking report that failed a gate silently is the thing this
method exists to prevent. So is a report so armored in its own apparatus
that the person it was written for has to dig for the answer.
        """,
        "doc_schema": [
            "PART ONE — FOR THE READER",
            "  Answer — the research question, answered, first, plain prose",
            "  Key Findings — plain sentences, confidence woven in, not tagged",
            "  What's Not Known — the gaps that matter to a decision",
            "  What I'd Do — a direct recommendation",
            "PART TWO — THE RECORD",
            "  Status — COMPLETE or PARTIAL (and which gate failed)",
            "  Claim Table — claim · sources · confidence",
            "  (every Source below carries a real, resolvable URL — see "
            "gate_verify's URL SHAPE check)",
            "  Hypothesis Final State",
            "  Sources — name · URL · date · band · persona",
            "  Searched And Not Found",
            "  Confidence Summary — n CONFIRMED / LIKELY / ESTIMATED / UNKNOWN",
            "  Assumptions and Limitations",
        ],
    },
}


# ─────────────────────────────────────────────────────────
# DOCUMENTS
# ─────────────────────────────────────────────────────────
# A phase without its document did not happen (Law 9). The document is
# the completion signal, not a write-up of work done elsewhere.
#
# HEAVY writes eight, one per phase.
# LIGHT writes three, each covering a contiguous group. The phases still
# all run — grouping changes the filing, never the work.

DOCUMENT_PLAN = {
    "HEAVY": {
        1: ("1. Brief",       [1]),
        2: ("2. Scope",       [2]),
        3: ("3. Plan",        [3]),
        4: ("4. Intel",       [4]),
        5: ("5. Check",       [5]),
        6: ("6. Verify",      [6]),
        7: ("7. Synthesis",   [7]),
        8: ("8. Report",      [8]),
    },
    "LIGHT": {
        1: ("1. Setup",       [1, 2, 3]),
        2: ("2. Evidence",    [4, 5, 6]),
        3: ("3. Report",      [7, 8]),
    },
}


def documents_for(mode: str) -> dict:
    return DOCUMENT_PLAN[mode]


def document_closing_phase(mode: str, phase: int):
    """The document name this phase completes, or None if mid-document."""
    for _, (name, phases) in documents_for(mode).items():
        if phases[-1] == phase:
            return name
    return None


# ─────────────────────────────────────────────────────────
# GATES
# ─────────────────────────────────────────────────────────
# A gate that cannot fail is not a gate. These fail runs, and that is
# the point. Each returns (passed, failures) — failures naming the check,
# never a vague verdict.

def gate_check(pool: list, krq_clusters: list, mode: str) -> tuple:
    """
    Phase 5 exit gate.

    NOTE ON SCORES: sources are NOT scored yet. Scoring is Phase 6, and
    phases run in order (Law 8). This gate counts what was actually
    RETRIEVED. A source that could not be opened is not a source and does
    not count toward anything here.

    `pool` is a list of dicts with at least:
        {"retrieved": bool, "persona": str, "media_mode": str, "krqs": [...]}

    ON COVERAGE: a cluster counts as covered when it has at least one
    finding. A cluster whose sub-questions are only partly answerable
    still passes — the unanswered parts are not a gate failure, they are
    Searched And Not Found (Law 5), and they must appear there. Do not
    loop INTEL over a sub-question you have established is not on the
    record; loop it over a cluster you never looked at.
    """
    spec = MODES[mode]
    failures = []

    usable = [s for s in pool if s.get("retrieved")]
    if len(usable) < spec["min_sources"]:
        failures.append(
            f"COUNT — {len(usable)} retrieved sources, "
            f"{spec['min_sources']} required")

    covered = {k for s in usable for k in s.get("krqs", [])}
    missing = [k for k in krq_clusters if k not in covered]
    if missing:
        failures.append(f"COVERAGE — no findings at all for: {', '.join(missing)}")

    # Persona must be drawn from the twelve in standards/source-personas.md
    # (Law 2's spirit applied to tagging: a tag that was never checked
    # against the taxonomy is not a tag, it is a guess wearing one). An
    # invented or off-taxonomy label fails outright rather than silently
    # not counting toward diversity — two fabricated "distinct" labels
    # must not be able to pass this check.
    off_taxonomy = [s for s in usable
                    if s.get("persona") and s["persona"] not in PERSONA_TAXONOMY]
    if off_taxonomy:
        failures.append(
            f"PERSONA TAXONOMY — {len(off_taxonomy)} source(s) tagged with "
            f"a persona not in standards/source-personas.md's twelve: " +
            "; ".join(sorted({s['persona'] for s in off_taxonomy})))

    personas = {s.get("persona") for s in usable
                if s.get("persona") in PERSONA_TAXONOMY}
    if len(personas) < 2:
        failures.append(
            f"DIVERSITY — {len(personas)} persona(s) present, 2 required")

    off_media = [s for s in usable
                 if s.get("media_mode") and s["media_mode"] not in MEDIA_MODES]
    if off_media:
        failures.append(
            f"MEDIA MODE — {len(off_media)} source(s) tagged with a mode "
            f"outside Paid/Owned/Earned: " +
            "; ".join(sorted({s['media_mode'] for s in off_media})))

    modes_present = {s.get("media_mode") for s in usable
                     if s.get("media_mode") in MEDIA_MODES}
    if len(modes_present) < 2:
        failures.append(
            f"DIVERSITY — {len(modes_present)} media mode(s), 2 required")

    return (not failures, failures)


# A regex cannot tell a real URL from a fabricated one — that needs an
# actual fetch (see the reference harness this is Stage 1 of). What it
# CAN catch, cheaply: a fabrication that didn't even bother to look like
# a URL. Found via cross-model testing (tests/CROSS-MODEL.md, Round
# 1/1.5) that unconstrained models sometimes cite a bare outlet name or
# an obvious placeholder instead of a link at all. This turns that
# specific shortcut into a hard failure — it does not, and cannot,
# confirm the URL resolves to something real.
_URL_PLACEHOLDER_MARKERS = (
    "example.com", "example.org", "yourdomain", "placeholder",
    "various outlets", "various sources", "several outlets", "n/a",
    "unknown url", "tbd",
)


def looks_like_a_real_url(value) -> bool:
    """
    Structural check only: has a scheme and a domain, and isn't a known
    placeholder pattern. Passing this proves nothing about truth — only
    that whoever wrote it did not skip the step of typing something
    URL-shaped. UNKNOWN sources should never reach this check at all;
    they belong in Searched And Not Found, not the pool.
    """
    if not isinstance(value, str):
        return False
    v = value.strip().lower()
    for scheme in ("http://", "https://"):
        if v.startswith(scheme):
            rest = v[len(scheme):]
            break
    else:
        return False
    if len(rest) < len("x.co"):  # shortest plausible domain, no scheme
        return False
    if any(marker in v for marker in _URL_PLACEHOLDER_MARKERS):
        return False
    return True


def gate_verify(pool: list, claims: list, mode: str) -> tuple:
    """
    Phase 6 exit gate. Five checks.

    `pool`   sources, each {"score", "origin", "retrieved": bool}
    `claims` each {"claim", "sources": [...], "confidence"}

    `origin` is the upstream source a citation traces back to. Sources
    sharing an origin collapse to one before counting (Law 4).
    """
    spec = MODES[mode]
    failures = []

    scored = [s for s in pool if "score" in s]
    if len(scored) != len(pool):
        failures.append("SCORE — not every source carries a score (Law 2)")

    # A total with no per-dimension breakdown is a guess wearing a number.
    # standards/source-scoring.md's job docstring already says "record
    # every dimension, not just the total" — this is that instruction
    # enforced rather than requested. A source must carry a `dimensions`
    # dict with exactly this mode's dimension names, and the total must
    # actually be their sum — not a number chosen first and reverse-fitted.
    required_dims = set(dimension_names(mode))
    dim_failures = []
    for s in pool:
        dims = s.get("dimensions")
        if not isinstance(dims, dict) or set(dims) != required_dims:
            dim_failures.append(s.get("id", "?"))
            continue
        if sum(dims.values()) != s.get("score"):
            dim_failures.append(s.get("id", "?"))
    if dim_failures:
        failures.append(
            f"SCORE BREAKDOWN — {len(dim_failures)} source(s) missing a "
            f"per-dimension score, missing a required dimension, or whose "
            f"total does not match the sum of its dimensions: " +
            ", ".join(str(x) for x in dim_failures))

    usable = [s for s in pool if clears_floor(s.get("score", 0), mode)]

    if len(usable) < spec["min_sources"]:
        failures.append(
            f"COUNT — {len(usable)} usable sources, {spec['min_sources']} required")

    unread = [s for s in usable if not s.get("retrieved")]
    if unread:
        failures.append(
            f"REACHABILITY — {len(unread)} source(s) cited but not retrieved")

    # URL SHAPE — structural only, not truth. A source without even a
    # URL-shaped url field skipped the one step that makes a claim
    # falsifiable by a reader in seconds. See looks_like_a_real_url().
    fake_shaped = [s for s in usable if not looks_like_a_real_url(s.get("url"))]
    if fake_shaped:
        failures.append(
            f"URL SHAPE — {len(fake_shaped)} source(s) with no real, "
            f"resolvable URL (placeholder, bare name, or missing): " +
            ", ".join(str(s.get("id", "?")) for s in fake_shaped))

    # POOL INDEPENDENCE — a whole pool that collapses to one origin is one
    # source, however many entries it has.
    origins = {s.get("origin") or s.get("id") or id(s) for s in usable}
    if len(origins) < 2:
        failures.append(
            f"POOL INDEPENDENCE — {len(usable)} sources collapse to "
            f"{len(origins)} origin; the pool is one source wearing "
            f"{len(usable)} hats (Law 4)")

    # ORIGIN TRACING — standards/independence-test.md exists because
    # "count distinct domain names and call that independence" is the
    # single most common way this method gets faked. Domain-counting sets
    # `origin` to the source's own id for everything and calls it done.
    # Require the opposite of silence: any source claiming to BE its own
    # origin (a first-mention, not a report of one) must say so and give
    # one line of why; any source pointing at another origin must name a
    # trace, not just a label. Neither is provable from here — this cannot
    # verify the tracing was done well, only that it was not skipped.
    untraced = [s for s in usable if not s.get("origin_trace")]
    if untraced:
        failures.append(
            f"ORIGIN TRACING — {len(untraced)} source(s) carry an `origin` "
            f"with no `origin_trace` explaining how it was established "
            f"(independence-test.md, Law 4) — a bare origin label is "
            f"exactly the domain-counting shortcut this check exists to "
            f"catch: " + ", ".join(str(s.get("id", "?")) for s in untraced))

    unsourced = [c for c in claims if not c.get("sources")]
    if unsourced:
        failures.append(
            f"EVIDENCE — {len(unsourced)} claim(s) with no source (Law 1)")

    unlabelled = [c for c in claims if c.get("confidence") not in CONFIDENCE]
    if unlabelled:
        failures.append(
            f"CONFIDENCE — {len(unlabelled)} claim(s) unlabelled (Law 6)")

    # CLAIM INDEPENDENCE — the check that actually matters. A pool can hold
    # three origins while every single claim rests on one of them. Test the
    # claims, not the pile.
    overclaimed = [c for c in claims
                   if c.get("confidence") == "CONFIRMED"
                   and not confirmable(c, pool, mode)]
    if overclaimed:
        failures.append(
            f"CLAIM INDEPENDENCE — {len(overclaimed)} claim(s) marked "
            f"CONFIRMED without {spec['confirmed_needs']} independent "
            f"origins: " + "; ".join(
                str(c.get("claim", "?"))[:60] for c in overclaimed))

    return (not failures, failures)


def detect_fabrication_patterns(pool: list, claims: list) -> list:
    """
    Soft tripwires, not gates. Returns a list of warning strings —
    nothing here blocks a run the way gate_verify's failures do, because
    every pattern below has real false positives (legitimately
    convergent good sourcing looks similar to lazily-uniform fabricated
    sourcing from the outside). Call this alongside gate_verify and
    surface the warnings to whoever reads the run — a human decides what
    they mean, this function only decides what's worth a second look.

    Found by testing (tests/CROSS-MODEL.md): Kimi and DeepSeek each
    fabricated a full source table under identical conditions, and their
    two invented numbers for the same fact did not agree with each
    other. That specific shape — sources that are suspiciously uniform
    with each other, or that disagree on what should be one number — is
    what these checks are aimed at. Neither proves fabrication; both are
    cheap enough to be worth flagging every time they occur.
    """
    import difflib
    import re

    warnings = []

    # PATTERN 1: independent-looking sources whose scores cluster tightly
    # AND whose stated facts read as near-paraphrases of each other. Real
    # independent reporting on the same event often agrees on substance
    # but rarely converges on near-identical phrasing; several models
    # tested fabricated a source table where every entry read like a
    # slight rewording of the same invented paragraph.
    scored = [s for s in pool if isinstance(s.get("score"), (int, float))
              and s.get("facts")]
    for i, a in enumerate(scored):
        for b in scored[i + 1:]:
            if abs(a["score"] - b["score"]) > 2:
                continue
            similarity = difflib.SequenceMatcher(
                None, str(a["facts"])[:500], str(b["facts"])[:500]
            ).ratio()
            if similarity > 0.6:
                warnings.append(
                    f"SCORE/PHRASING CLUSTER — sources "
                    f"{a.get('id', '?')!r} and {b.get('id', '?')!r} score "
                    f"within 2 points of each other and their facts text "
                    f"is {similarity:.0%} similar — worth checking these "
                    f"are genuinely independent reporting, not one "
                    f"invented paragraph restated twice")

    # PATTERN 2: claims that plausibly describe the same fact but state
    # different numbers for it. A crude proxy for "the same fact" —
    # heavy term overlap in the claim text — but cheap, and it is
    # exactly the pattern that caught the Kimi-vs-DeepSeek disagreement
    # on Anthropic's valuation, just applied within one run instead of
    # across two.
    numeric_claims = [c for c in claims if c.get("claim")
                       and re.search(r"\d", str(c["claim"]))]
    for i, a in enumerate(numeric_claims):
        for b in numeric_claims[i + 1:]:
            a_words = set(re.findall(r"[a-z]{4,}", str(a["claim"]).lower()))
            b_words = set(re.findall(r"[a-z]{4,}", str(b["claim"]).lower()))
            if not a_words or not b_words:
                continue
            overlap = len(a_words & b_words) / len(a_words | b_words)
            if overlap < 0.4:
                continue
            a_nums = set(re.findall(r"\d[\d,.]*", str(a["claim"])))
            b_nums = set(re.findall(r"\d[\d,.]*", str(b["claim"])))
            if a_nums and b_nums and not (a_nums & b_nums):
                warnings.append(
                    f"NUMERIC DISAGREEMENT — claims "
                    f"{str(a.get('claim'))[:50]!r} and "
                    f"{str(b.get('claim'))[:50]!r} look like they describe "
                    f"the same thing ({overlap:.0%} term overlap) but cite "
                    f"different numbers ({a_nums} vs {b_nums}) — resolve "
                    f"via reconciliation-protocol.md before reporting "
                    f"either as CONFIRMED")

    return warnings


def confirmable(claim: dict, pool: list, mode: str) -> bool:
    """
    Whether a claim may be marked CONFIRMED.

    Ordinary route: enough cited sources to survive origin-collapse, at
    the mode's threshold.

    Canonical route: one retrieved canonical source is sufficient, but
    ONLY for a claim about that document's own content. The claim must
    carry `about_source_content: True` and the source must be both
    `canonical: True` and `retrieved: True`. See CANONICAL SOURCES above.
    """
    needed = MODES[mode]["confirmed_needs"]
    by_id  = {s.get("id"): s for s in pool}
    cited  = [by_id[sid] for sid in claim.get("sources", []) if sid in by_id]
    usable = [s for s in cited if clears_floor(s.get("score", 0), mode)]

    if claim.get("about_source_content"):
        if any(s.get("canonical") and s.get("retrieved") for s in usable):
            return True

    origins = {s.get("origin") or s.get("id") for s in usable}
    return len(origins) >= needed


# ─────────────────────────────────────────────────────────
# PROMPT BUILDER
# ─────────────────────────────────────────────────────────

def build_phase_prompt(phase_number: int, run_card: RunCard,
                       context: RunContext,
                       previous_card: PhaseCard = None) -> str:
    """Assemble the full instruction for one phase."""
    phase  = PHASE_AGENTS[phase_number]
    spec   = run_card.spec
    domain = context.domain

    lines = [
        f"# SuperBasic™ Research — Phase {phase_number}: {phase['name']}",
        f"You are the {phase['role']}.",
        "",
    ]
    if phase_number == 1:
        lines += ["## Before Anything Else", f"  {TOOL_ACCESS_CHECK}", ""]
    lines += ["## The Laws"]
    for group in LAWS.values():
        lines += [f"  {law}" for law in group]

    lines += [
        "",
        "## Run Card",
        f"Run ID:    {run_card.run_id}",
        f"Subject:   {run_card.subject}",
        f"Category:  {run_card.category}",
        f"Angle:     {run_card.angle}",
        f"Question:  {run_card.question}",
        f"Mode:      {run_card.mode}  "
        f"(min {spec['min_sources']} sources · CONFIRMED needs "
        f"{spec['confirmed_needs']} · scored out of {spec['scoring_max']})",
        f"Priority:  {run_card.priority}",
    ]

    if domain.domain or domain.framing or domain.voice:
        lines += ["", "## Domain"]
        if domain.domain:
            lines.append(f"Domain:   {domain.domain}")
        if domain.framing:
            lines.append(f"Framing:  {domain.framing}")
        if domain.voice and phase_number in (7, 8):
            lines.append(f"Voice:    {domain.voice}")
        if domain.lenses and phase_number == 7:
            lines.append(f"Lenses:   {', '.join(domain.lenses)}")
        if domain.krq_template and phase_number == 1:
            lines.append(f"KRQ template: {', '.join(domain.krq_template)}")
        hrs = domain.hours_to_deadline
        if hrs is not None:
            lines.append(f"Hours to deadline: {hrs}")
        for k, v in domain.extras.items():
            lines.append(f"{k}: {v}")
        lines.append(
            "Domain context shapes framing and voice only. It never relaxes "
            "a Law or lowers a threshold.")

    if previous_card:
        import json
        lines += [
            "",
            f"## Phase {previous_card.phase} Output ({previous_card.name})",
            json.dumps(previous_card.outputs, indent=2, ensure_ascii=False),
        ]

    lines += ["", "## Your Instructions", phase["job"].strip()]

    refs = _references_for_phase(phase_number)
    if refs:
        lines += ["", "## Open These"]
        for path, why in refs:
            lines.append(f"  {path} — {why}")

    lines += [
        "",
        "## Confidence Labels",
    ]
    for word, meaning in CONFIDENCE.items():
        lines.append(f"  {word} — {meaning}")

    lines += [
        "",
        "## Output",
        "Return a JSON object keyed to the schema below.",
        "Every factual claim carries a confidence label. Never TBD. Never blank.",
        "Do not summarise previous phases. Execute this one.",
        "",
        "## Schema",
    ]
    for item in phase["doc_schema"]:
        lines.append(f"  - {item}")

    lines += ["", "Begin."]
    return "\n".join(lines)


def _references_for_phase(phase_number: int) -> list:
    mapping = {
        2: ["decay"],
        3: ["media_index", "proxy_labeling"],
        4: ["source_personas", "source_profiles", "anomaly_investigation"],
        6: ["source_scoring", "independence", "anomaly_investigation",
            "reconciliation", "assumption_exposure", "proxy_labeling",
            "triangulation_map"],
        7: ["hypothesis_evolution"],
        8: ["assumption_exposure", "report_scoring", "report_checklist"],
    }
    return [REFERENCES[k] for k in mapping.get(phase_number, [])]


# ─────────────────────────────────────────────────────────
# THE RUN
# ─────────────────────────────────────────────────────────

MAX_LOOPS = 2   # per gate. Loops are legitimate; endless loops are not.


def run_sbr(run_card: RunCard, context: RunContext,
            agent_executor, writer) -> RunResult:
    """
    Execute the eight phases in order.

    agent_executor  callable(phase_number, run_card, context, previous_card)
                    → PhaseCard.  Any LLM. You, most likely.

    writer          callable(destination, doc_name, content) → {id, url}
                    Drive, local files, or a stub that returns the content
                    when there is nowhere to write.

    On max loops the run does NOT quietly continue as if it passed. It is
    marked PARTIAL, the failing gate is named, and the Report says so at
    the top (Law 10, honoured as far as it can be).
    """
    import json

    result = RunResult()
    result.run_id      = run_card.run_id
    result.destination = context.destination

    previous_card = None
    phase         = 1
    loop_counts   = {}
    buffer        = []          # phases accumulated toward the current document

    while phase <= 8:
        config = PHASE_AGENTS[phase]

        card = agent_executor(
            phase_number=phase,
            run_card=run_card,
            context=context,
            previous_card=previous_card,
        )

        # Precondition gate, checked once, before Phase 1 counts as having
        # happened at all (see TOOL_ACCESS_CHECK above). A declared "no
        # tools" halts the run here — no buffer entry, no document, no
        # claims left standing to be mistaken for researched ones.
        if phase == 1:
            passed, failures = gate_tool_access(card.outputs.get("tool_access"))
            if not passed:
                result.status      = "STOPPED"
                result.failed_gate = failures[0]
                return result

        buffer.append((phase, config["name"], card))
        result.confidence_scores[config["name"]] = card.confidence

        # A gate failed — go back, if there are loops left.
        if not card.go:
            target = card.loop_to or 4
            if loop_counts.get(target, 0) < MAX_LOOPS:
                loop_counts[target] = loop_counts.get(target, 0) + 1
                previous_card = card
                buffer = [b for b in buffer if b[0] < target]
                phase = target
                continue
            # Out of loops. Proceed, but the run is PARTIAL and says so.
            result.status      = "PARTIAL"
            result.failed_gate = f"Phase {phase} ({config['name']})"
            card.go = True

        # Write the document if this phase closes one (Law 9).
        doc_name = document_closing_phase(run_card.mode, phase)
        if doc_name:
            content = _build_document(run_card, context, doc_name, buffer,
                                      result.status, result.failed_gate)
            doc = writer(context.destination,
                         f"{run_card.run_id} · {doc_name}",
                         content)
            result.documents[doc_name] = doc
            if phase == 8:
                result.report_url = doc.get("url")
            buffer = []

        previous_card = card
        phase += 1

    if result.status == "PENDING":
        result.status = "COMPLETE"
    return result


def _build_document(run_card: RunCard, context: RunContext, doc_name: str,
                    buffer: list, status: str, failed_gate) -> str:
    """
    One document, covering every phase in the buffer.

    This is the machine-readable form. When a human is the reader — which
    is the usual case when `destination` is None and the run comes back in
    a conversation — render the same content as prose under the same
    headings instead of dumping JSON. The structure is the requirement;
    the JSON is not. What may never change: the header, the phase
    headings, the PARTIAL warning, and the fact that every phase in the
    buffer appears.
    """
    import json

    rule  = "━" * 60
    lines = [
        rule,
        f"{run_card.run_id} · {doc_name}",
        "",
        f"WHAT:  {run_card.angle} — {run_card.subject}",
        f"WHY:   {run_card.question}",
        f"WHO:   SuperBasic™ Research, {run_card.mode} mode",
        f"HOW:   Phases {', '.join(str(p) for p, _, _ in buffer)}",
    ]
    if status == "PARTIAL":
        lines += ["", f"⚠ PARTIAL — gate failed at {failed_gate}. "
                      "Findings below are provisional."]
    lines += [rule, ""]

    for phase_no, phase_name, card in buffer:
        lines += [
            f"## Phase {phase_no} — {phase_name}",
            json.dumps(card.outputs, indent=2, ensure_ascii=False),
            "",
        ]

    lines += [
        rule,
        f"Mode: {run_card.mode} · Status: {status}",
        f"Project: {context.project or '—'}",
        rule,
    ]
    return "\n".join(lines)


# ─────────────────────────────────────────────────────────
# USAGE
# ─────────────────────────────────────────────────────────
#
# card = RunCard({
#     "run_id":   "ACME-01",
#     "subject":  "Acme Logistics GmbH",
#     "category": "Organisation",
#     "angle":    "Company profile for outbound",
#     "question": "What is Acme's current operational pressure, and who "
#                 "owns the decision to fix it?",
#     "mode":     "LIGHT",
# })
#
# ctx = RunContext({
#     "destination": None,              # nowhere to write — return inline
#     "project":     "outbound-research",   # free label, naming only
#     "domain": DomainContext({
#         "domain":  "B2B lead research",
#         "framing": "The reader is about to write one cold email.",
#     }),
# })
#
# result = run_sbr(card, ctx, agent_executor=me, writer=inline_writer)
#
# The same card with mode HEAVY produces eight documents instead of three,
# scores out of 40 instead of 30, and requires three independent sources
# for CONFIRMED instead of two. Nothing else changes.
