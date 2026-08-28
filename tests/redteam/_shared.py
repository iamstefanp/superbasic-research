"""
_shared.py — the independent-verification layer every redteam test uses.

The one rule this file exists to enforce mechanically: a harness claim
of `retrieved: true` is never treated as proof on its own. Every test
that asserts a source is genuine re-checks it here, outside the
harness, with a plain HTTP request that owes nothing to Tavily, the
model, or executor.py's own bookkeeping.
"""

import json
import os
import sys
import time

import requests

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "harness"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

EVIDENCE_DIR = os.path.join(os.path.dirname(__file__), "evidence")
USER_AGENT = "Mozilla/5.0 (SuperBasicResearch-RedTeam/1.0)"


def independently_verify_url(url: str) -> dict:
    """
    Re-check a URL with a plain HTTP request, entirely outside the
    harness's own tool-calling/enforcement path. Returns
    {"url": str, "reachable": bool, "status": int|None, "error": str|None}.
    """
    try:
        resp = requests.get(url, timeout=15, headers={"User-Agent": USER_AGENT})
        return {
            "url": url,
            "reachable": resp.status_code == 200,
            "status": resp.status_code,
            "error": None,
        }
    except requests.RequestException as e:
        return {"url": url, "reachable": False, "status": None, "error": str(e)}


def write_evidence(test_name: str, payload: dict) -> str:
    """
    Commit-worthy raw evidence for one test run. Filename is a UTC
    timestamp so ordering is unambiguous; payload should include enough
    raw data (full or truncated model output, tool-call results, the
    independent-verification result) for a stranger to audit the claim
    without re-running anything.
    """
    out_dir = os.path.join(EVIDENCE_DIR, test_name)
    os.makedirs(out_dir, exist_ok=True)
    ts = time.strftime("%Y-%m-%dT%H-%M-%SZ", time.gmtime())
    path = os.path.join(out_dir, f"{ts}.json")
    with open(path, "w") as f:
        json.dump(payload, f, indent=2, default=str)
    return path


def verdict_line(case: str, verdict: str, detail: str = "") -> None:
    """Uniform stdout line: every test file reports this way."""
    tag = {"PASS": "PASS", "FAIL": "FAIL", "FLAG": "FLAG"}.get(verdict, verdict)
    line = f"[{tag}] {case}"
    if detail:
        line += f" — {detail}"
    print(line)
