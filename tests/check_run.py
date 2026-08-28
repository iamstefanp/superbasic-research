"""
check_run.py — mechanical Layer-1 checker for SuperBasic Research runs.

Not a validator of truth. It cannot tell you if a claim is correct — that
is Layer 2 (judge agents) and the ground-truth audit, both human/agent
judgment calls documented in RUBRIC.md. This script only checks the
things a script CAN check: format compliance, label presence, structural
honesty markers. A run that passes every check here can still fail the
battery outright at Layer 0.

Usage:
    python3 check_run.py <run_output.md> --mode LIGHT|HEAVY

Input: a single markdown/text file containing the run's full output (all
phase documents concatenated, or the three/eight documents joined with
"---" between them). The parser is deliberately loose — it looks for
markers, not a rigid schema — because sbr.py explicitly allows prose
rendering over literal JSON when a human is the reader.

Validate this script against the two pre-battery stranger-test outputs
BEFORE trusting it on anything new (RUBRIC.md Layer 1). They are
known-good; if the checker doesn't cleanly pass them, the checker is
broken, not the runs.
"""

import argparse
import re
import sys


CONFIDENCE_WORDS = {"CONFIRMED", "LIKELY", "ESTIMATED", "UNKNOWN"}

# Loose recall regexes. Loose on purpose: penalize the CONTENT of a run,
# never its formatting choices, as long as the substance is findable.
CONFIDENCE_TAG_RE = re.compile(
    r"\b(CONFIRMED|LIKELY|ESTIMATED|UNKNOWN)\b")
SCORE_RE = re.compile(
    r"(\d{1,2})\s*/\s*(30|40)\b")  # e.g. "22/30", "26 / 40"
# Fallback: a number immediately followed by a band name, e.g. "22 SILVER"
# or "S1=22 SILVER" — covers prose/table renderings that never spell out
# the /30 or /40 scale per-source, only once in a header.
BAND_SCORE_RE = re.compile(
    r"\b(\d{1,2})\s*(GOLD|SILVER|BRONZE|QUESTIONABLE|REJECT)\b")
SCALE_DECLARED_RE = re.compile(r"/\s*(30|40)\b")
PARTIAL_RE = re.compile(
    r"(?<!not\s)(?<!Not\s)(?<!NOT\s)\bPARTIAL\b")
NOT_PARTIAL_RE = re.compile(r"\bnot\s+PARTIAL\b", re.IGNORECASE)
COMPLETE_RE = re.compile(r"\bCOMPLETE\b", re.IGNORECASE)
# The word PARTIAL/COMPLETE also appears as an ordinary table-cell value
# for an unrelated sub-check (e.g. "REACHABILITY | Partial" describing
# just that one check, not the run). A bare document-wide scan for the
# word conflates the two. RUN_STATUS_RE requires the word to appear near
# an explicit "status" label — the only place sbr.py actually declares
# the run's terminal state — so a sub-check's own verdict doesn't get
# misread as the run's status.
RUN_STATUS_RE = re.compile(
    r"status\s*[:\-]?\s*\**\s*(COMPLETE|PARTIAL)\b", re.IGNORECASE)
DOC_HEADER_RE = re.compile(
    r"^#{1,3}\s*(DOCUMENT\s+\d+|[\w-]+\s*[·\.]\s*Document\s+\d+)",
    re.IGNORECASE | re.MULTILINE)
FAILED_GATE_RE = re.compile(
    r"(failed\s+gate|gate\s+fail|loop\s*(cap|exhaust)|max\s*loops)",
    re.IGNORECASE)
SNAF_HEADING_RE = re.compile(
    r"(Searched\s+And\s+Not\s+Found|Searched\s+and\s+not\s+found)",
    re.IGNORECASE)
GENERIC_NOT_FOUND_RE = re.compile(
    r"no\s+information\s+(was\s+)?available", re.IGNORECASE)
# Natural writing almost always puts an adjective between the count and
# the noun ("2 independent origins", "9 directly-retrieved sources"), so
# require the number and keyword within a few words of each other rather
# than strictly adjacent — a strictly-adjacent version under-counts real
# gate language and was found to do so against actual wave-1 battery runs.
GATE_NUMBER_RE = re.compile(
    r"\b\d+\b(?:\s+\S+){0,2}?\s+(usable|retrieved|sources?|origins?)\b",
    re.IGNORECASE)

DOC_COUNT_TARGET = {"LIGHT": 3, "HEAVY": 8}
DIM_COUNT_TARGET = {"LIGHT": 6, "HEAVY": 8}


def split_documents(text: str):
    """
    Count documents, not sections. Prefer explicit 'DOCUMENT N' / '...·
    Document N' headers — these mark real phase-document boundaries per
    sbr.py's own naming (`[RUN_ID] · [N]. [Phase Name]`). Only fall back
    to bare '---'/'===' rules if no such headers exist, since those are
    also used mid-document as internal section dividers and will
    over-count.
    """
    headers = DOC_HEADER_RE.findall(text)
    if headers:
        return headers
    chunks = re.split(r"\n-{3,}\n|\n={3,}\n", text)
    chunks = [c for c in chunks if c.strip()]
    return chunks or [text]


def check_confidence_labels(text: str) -> dict:
    tags = CONFIDENCE_TAG_RE.findall(text)
    return {
        "check": "Every claim carries a confidence label",
        "pass": len(tags) > 0,
        "detail": f"{len(tags)} confidence labels found "
                  f"({', '.join(sorted(set(tags)))})",
    }


def check_scores(text: str, mode: str) -> dict:
    """
    Two acceptable renderings of 'every source is scored':
      1. Literal 'N/30' or 'N/40' per source.
      2. A number immediately paired with a band name (e.g. '22 SILVER'),
         PROVIDED the scale itself (/30 or /40) is declared somewhere in
         the document — e.g. a header 'Scored Source Table (LIGHT /30)'.
         Band-only with no scale declaration anywhere is not accepted:
         that would let a run silently score on the wrong scale for its
         mode and still pass.
    """
    expected_max = "30" if mode == "LIGHT" else "40"
    literal = [s for s in SCORE_RE.findall(text) if s[1] == expected_max]
    band_scores = BAND_SCORE_RE.findall(text)
    scale_declared = expected_max in SCALE_DECLARED_RE.findall(text)

    if literal:
        return {
            "check": f"Sources scored out of {expected_max} ({mode})",
            "pass": True,
            "detail": f"{len(literal)} literal N/{expected_max} scores found",
        }
    if band_scores and scale_declared:
        return {
            "check": f"Sources scored out of {expected_max} ({mode})",
            "pass": True,
            "detail": f"{len(band_scores)} number+band scores found "
                      f"(e.g. '22 SILVER'), scale /{expected_max} "
                      f"declared elsewhere in the document",
        }
    if band_scores and not scale_declared:
        return {
            "check": f"Sources scored out of {expected_max} ({mode})",
            "pass": False,
            "detail": f"{len(band_scores)} number+band scores found but "
                      f"no /{expected_max} scale declaration found — "
                      f"cannot confirm the run scored on the correct "
                      f"scale for {mode} mode",
        }
    return {
        "check": f"Sources scored out of {expected_max} ({mode})",
        "pass": False,
        "detail": "no per-source scores found in either literal (N/30) "
                  "or band-paired (N SILVER) form",
    }


def check_snaf(text: str) -> dict:
    has_heading = bool(SNAF_HEADING_RE.search(text))
    generic_only = bool(GENERIC_NOT_FOUND_RE.search(text))
    # Falsifiable = has the heading AND has content beyond the generic phrase
    section_match = SNAF_HEADING_RE.search(text)
    falsifiable = False
    if section_match:
        tail = text[section_match.end():section_match.end() + 800]
        # crude signal: does the tail contain something more specific
        # than the generic phrase alone? (a URL, a date, a named venue)
        has_specifics = bool(re.search(
            r"(https?://|20\d{2}-\d{2}-\d{2}|\b\d{1,2}\s+\w+\s+20\d{2}\b)",
            tail))
        falsifiable = has_specifics or (len(tail.strip()) > 100
                                        and not generic_only)
    return {
        "check": "Searched-And-Not-Found present and falsifiable",
        "pass": has_heading and falsifiable,
        "detail": (
            "no Searched-And-Not-Found section found" if not has_heading
            else "section present but reads as generic, not falsifiable "
                 "(no named venues/dates/queries detected)"
                 if not falsifiable
            else "section present with apparent specifics (dates/URLs)"
        ),
    }


def check_gate_numbers(text: str) -> dict:
    matches = GATE_NUMBER_RE.findall(text)
    return {
        "check": "Gate results recorded as counted numbers, not bare verdicts",
        "pass": len(matches) >= 2,
        "detail": f"{len(matches)} numeric gate references found "
                  f"(e.g. 'N usable sources')",
    }


def check_status(text: str) -> dict:
    # Prefer an explicit "Status: COMPLETE/PARTIAL" declaration — the only
    # place sbr.py actually states the run's terminal status. This avoids
    # misreading an unrelated sub-check's own table-cell verdict (e.g.
    # "REACHABILITY | Partial" describing just that one gate) as the run's
    # status. Fall back to the looser document-wide scan only when no
    # explicit declaration is found at all.
    status_hits = RUN_STATUS_RE.findall(text)
    if status_hits:
        statuses = {s.upper() for s in status_hits}
        has_partial = "PARTIAL" in statuses
        has_complete = "COMPLETE" in statuses
    else:
        # Negative lookbehind in PARTIAL_RE handles "not PARTIAL" at the
        # token boundary, but "Not PARTIAL." with a period, or "Not\n
        # PARTIAL" across a line wrap, can still slip through — so
        # double-check explicitly against NOT_PARTIAL_RE before trusting a
        # bare PARTIAL_RE hit near the word "Not".
        raw_partial_hits = PARTIAL_RE.findall(text)
        negated = NOT_PARTIAL_RE.search(text)
        has_partial = bool(raw_partial_hits) and not (
            negated and len(raw_partial_hits) <= 1)
        has_complete = bool(COMPLETE_RE.search(text))
    has_failed_gate_language = bool(FAILED_GATE_RE.search(text))

    if has_partial and not has_failed_gate_language:
        return {
            "check": "PARTIAL declared iff a loop cap was exhausted",
            "pass": False,
            "detail": "PARTIAL declared but no evidence of an exhausted "
                      "loop/failed-gate found nearby — verify manually",
        }
    if has_complete and has_partial:
        return {
            "check": "Status is unambiguous (COMPLETE xor PARTIAL)",
            "pass": False,
            "detail": "both COMPLETE and PARTIAL language found — "
                      "manual review required",
        }
    if not has_partial and not has_complete:
        return {
            "check": "Run declares a terminal status",
            "pass": False,
            "detail": "neither COMPLETE nor PARTIAL found in the output",
        }
    return {
        "check": "Status declared consistently",
        "pass": True,
        "detail": f"PARTIAL={has_partial}, COMPLETE={has_complete}, "
                  f"failed-gate language present={has_failed_gate_language}",
    }


def check_document_count(text: str, mode: str) -> dict:
    n = len(split_documents(text))
    target = DOC_COUNT_TARGET[mode]
    # Loose: accept target or target±1 in case of a merged intro/index doc,
    # but flag anything further off for manual review.
    close_enough = abs(n - target) <= 1
    return {
        "check": f"Document/section count matches {mode} ({target})",
        "pass": close_enough,
        "detail": f"{n} document sections detected (target {target}) — "
                  f"note: sbr.py permits prose rendering over literal "
                  f"per-phase files; if this fails, check phase coverage "
                  f"manually before treating it as a real failure",
    }


CHECKS = [
    check_confidence_labels,
    check_snaf,
    check_gate_numbers,
    check_status,
]


def run_checks(text: str, mode: str) -> list:
    results = []
    for fn in CHECKS:
        results.append(fn(text))
    results.append(check_scores(text, mode))
    results.append(check_document_count(text, mode))
    return results


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("run_file")
    ap.add_argument("--mode", choices=["LIGHT", "HEAVY"], required=True)
    args = ap.parse_args()

    with open(args.run_file, "r", encoding="utf-8") as f:
        text = f.read()

    results = run_checks(text, args.mode)

    print(f"MECHANICAL CHECK — {args.run_file} ({args.mode})")
    print("=" * 60)
    n_pass = 0
    for r in results:
        mark = "PASS" if r["pass"] else "FAIL"
        n_pass += r["pass"]
        print(f"[{mark}] {r['check']}")
        print(f"       {r['detail']}")
    print("=" * 60)
    print(f"{n_pass}/{len(results)} mechanical checks passed.")
    print()
    print("This script checks FORMAT, not TRUTH. A clean pass here does")
    print("NOT mean the run passes Layer 0 gates or Layer 2 judgment —")
    print("see RUBRIC.md. Manual review is required regardless of the")
    print("result above, especially for: document-count near-misses,")
    print("PARTIAL/status ambiguity, and any FAIL on Searched-And-Not-Found.")

    sys.exit(0 if n_pass == len(results) else 1)


if __name__ == "__main__":
    main()
