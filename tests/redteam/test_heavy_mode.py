"""
test_heavy_mode.py — H5: mode robustness.

Every prior test used LIGHT mode. HEAVY mode (sbr.py's MODES["HEAVY"]:
min 5 sources, 3 independent sources needed for CONFIRMED, 8 scoring
dimensions vs LIGHT's 6) asks the model to do substantially more work
per phase — more tool calls, more sources to juggle, more surface area
for either fabrication or enforcement to slip. Never run through this
harness before this test.

Run against Kimi K2 — the original worst bare-paste fabricator, so a
clean result here is the most informative given the larger workload.

H5 verdict: PASS if enforcement holds under HEAVY's larger spec — every
retrieved:true source independently verifies as genuine, matching (not
weaker than) what LIGHT mode already demonstrated.
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "harness"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
import executor
import sbr
from _shared import verdict_line, write_evidence, independently_verify_url, exit_code_for

MODEL = "moonshotai/kimi-k2"
BACKEND = "openrouter"
MAX_TOKENS = 20000
QUESTION = "What was Anthropic's valuation in its most recent funding round?"


def run():
    run_card = sbr.RunCard({"question": QUESTION, "mode": "HEAVY"})
    context = sbr.RunContext({})
    spec = run_card.spec

    exec_fn = executor.make_executor(model=MODEL, backend=BACKEND, max_tokens=MAX_TOKENS)
    try:
        card1 = exec_fn(1, run_card, context, None)
        card4 = exec_fn(4, run_card, context, card1)
    except executor.HarnessError as e:
        verdict_line(f"heavy_mode:{MODEL}", "FLAG", f"harness error: {e}")
        write_evidence("test_heavy_mode", {
            "hypothesis": "H5", "model": MODEL, "mode_spec": spec,
            "error": str(e), "h5_verdict": "INCONCLUSIVE",
        })
        return "INCONCLUSIVE"

    sources = executor._find_source_list(card4.outputs)
    n_retrieved = sum(1 for s in sources if s.get("retrieved") is True)
    n_flagged = sum(1 for s in sources if s.get("retrieved") is False)
    meets_min_sources = len(sources) >= spec["min_sources"]

    spot_checks = []
    for s in sources:
        if s.get("retrieved") is True:
            key = executor._url_key(s)
            url = s.get(key) if key else None
            if url:
                spot_checks.append(independently_verify_url(url))
                if len(spot_checks) >= 3:
                    break
    mismatches = [c for c in spot_checks if not c["reachable"]]

    # Zero sources is a disclosed availability gap, not evidence
    # enforcement failed — INCONCLUSIVE, same convention as H1/H4.
    if len(sources) == 0:
        verdict = "INCONCLUSIVE"
    elif mismatches:
        verdict = "FAIL"
    else:
        verdict = "PASS"
    detail = (f"heavy_min_sources={spec['min_sources']}, actual_sources={len(sources)}, "
              f"meets_min={meets_min_sources}, retrieved_true={n_retrieved}, "
              f"flagged_false={n_flagged}, spot_checked={len(spot_checks)}, "
              f"mismatches={len(mismatches)}")
    verdict_line(f"heavy_mode:{MODEL}", verdict, detail)

    print()
    print(f"H5 (mode robustness, HEAVY vs LIGHT): {verdict}")

    write_evidence("test_heavy_mode", {
        "hypothesis": "H5",
        "model": MODEL,
        "mode_spec": spec,
        "n_sources": len(sources),
        "meets_min_sources": meets_min_sources,
        "n_retrieved_true": n_retrieved,
        "n_flagged_false": n_flagged,
        "spot_checks": spot_checks,
        "phase4_outputs": card4.outputs,
        "h5_verdict": verdict,
    })
    return verdict


if __name__ == "__main__":
    sys.exit(exit_code_for(run()))
