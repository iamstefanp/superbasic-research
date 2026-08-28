"""
verify_sources.py — a post-hoc spot-audit for a finished Report.

Stage 3 of the fix in ../tests/CROSS-MODEL.md. This is the backstop for
the case the harness (../harness/) can't reach: someone ran SuperBasic
Research in bare-paste mode — no real tools wired in — and now has a
Report they didn't generate under governed conditions. This script
can't prevent a fabrication; the Report already exists. What it can do
is fetch every cited URL for real and tell a human, plainly, which
sources hold up and which don't.

This never auto-approves a report. It prints a table. A human reads it.
Fuzzy text matching has real false-negative and false-positive rates —
trusting it to silently pass or fail a report would just move the
"blindly trust the machine" problem one step downstream instead of
solving it.

Usage:
    python3 verify_sources.py sources.json

Where sources.json is a list of dicts, each with at minimum a "url" key
and ideally "facts" (the claim attributed to it) and "published"/
"accessed" (dates to sanity-check). This is deliberately decoupled from
sbr.py's exact schema — point it at any list of {url, facts, ...} you
want spot-checked, whether it came from a SuperBasic run or not.
"""

import difflib
import json
import re
import sys

import requests
from bs4 import BeautifulSoup


def resolve(url: str) -> dict:
    """Real fetch. Returns {"ok": bool, "status": int|None,
    "text": str, "error": str|None}."""
    try:
        resp = requests.get(
            url, timeout=15,
            headers={"User-Agent": "Mozilla/5.0 (SuperBasicResearch/1.0)"},
        )
    except requests.RequestException as e:
        return {"ok": False, "status": None, "text": "", "error": str(e)}
    if resp.status_code != 200:
        return {"ok": False, "status": resp.status_code, "text": "",
                 "error": f"HTTP {resp.status_code}"}
    soup = BeautifulSoup(resp.text, "html.parser")
    for tag in soup(["script", "style", "nav", "footer", "header"]):
        tag.decompose()
    text = " ".join(soup.get_text(separator=" ").split())
    return {"ok": True, "status": 200, "text": text, "error": None}


def fuzzy_claim_match(claim: str, page_text: str) -> float:
    """
    A rough, honestly-labeled-as-rough similarity score (0.0-1.0)
    between a claimed fact and the actual page text. This is a spot
    check, not a proof — it looks for the best-matching window of page
    text against the claim using difflib, which catches obvious
    fabrications (the claim's key terms appear nowhere on the page) but
    will miss a subtly wrong number dressed in otherwise-real language.
    Treat a low score as "investigate further," a high score as
    "plausible," never as a verdict on its own.
    """
    if not claim or not page_text:
        return 0.0
    claim_words = set(re.findall(r"[a-z0-9]{4,}", claim.lower()))
    if not claim_words:
        return 0.0
    page_words = set(re.findall(r"[a-z0-9]{4,}", page_text.lower()))
    overlap = claim_words & page_words
    word_overlap_score = len(overlap) / len(claim_words)

    seq_score = difflib.SequenceMatcher(
        None, claim.lower()[:200], page_text.lower()[:5000]
    ).ratio()

    return round(max(word_overlap_score, seq_score), 2)


def audit(sources: list) -> list:
    """Returns a list of per-source result dicts. Prints nothing —
    presentation is the caller's job, kept separate so this is testable
    without a terminal."""
    results = []
    for s in sources:
        url = s.get("url", "")
        claim = s.get("facts", "") or s.get("claim", "")

        if not url:
            results.append({"url": "(none)", "verdict": "FAIL",
                             "reason": "no URL to check"})
            continue

        fetch = resolve(url)
        if not fetch["ok"]:
            results.append({"url": url, "verdict": "FAIL",
                             "reason": f"does not resolve: {fetch['error']}"})
            continue

        score = fuzzy_claim_match(claim, fetch["text"]) if claim else None
        if score is None:
            verdict = "UNVERIFIABLE"
            reason = "resolves, but no claim text was given to check against"
        elif score >= 0.5:
            verdict = "PASS"
            reason = f"resolves, claim text plausibly present (score {score})"
        elif score >= 0.2:
            verdict = "UNVERIFIABLE"
            reason = (f"resolves, but claim match is weak (score {score}) "
                       "— read it yourself before trusting this one")
        else:
            verdict = "FAIL"
            reason = (f"resolves, but claim text essentially absent "
                       f"(score {score}) — likely wrong page or fabricated "
                       "claim attached to a real URL")

        results.append({"url": url, "verdict": verdict, "reason": reason})
    return results


def print_table(results: list):
    print(f"{'VERDICT':<14} {'URL':<60} REASON")
    print("-" * 100)
    for r in results:
        print(f"{r['verdict']:<14} {r['url'][:58]:<60} {r['reason']}")
    counts = {}
    for r in results:
        counts[r["verdict"]] = counts.get(r["verdict"], 0) + 1
    print()
    print("Summary:", ", ".join(f"{k}={v}" for k, v in counts.items()))
    print()
    print("This table is a spot check, not a verdict on the whole report.")
    print("PASS means the URL resolves and the claim text is plausibly")
    print("present — it does not mean the claim is true, only that it's")
    print("not an obvious fabrication attached to a working link.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 verify_sources.py sources.json")
        sys.exit(1)
    with open(sys.argv[1]) as f:
        sources = json.load(f)
    results = audit(sources)
    print_table(results)
