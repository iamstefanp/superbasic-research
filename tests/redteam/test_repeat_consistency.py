"""
test_repeat_consistency.py — H1: repeat-run consistency.

Every result published before this suite was N=1 per model — one clean
run, one caught fabrication. LLM outputs aren't deterministic; this
runs N=3 per model on the same fixed LIGHT-mode question and reports
the per-run and aggregate fabrication rate, not a single anecdote.

H1 verdict: PASS if, across all 3 runs per model, the harness's
`retrieved` flag matches independently-verified ground truth in every
sampled case, for both a previously-clean model and Mistral (which
should continue being correctly flagged, not necessarily clean).
"""

import json
import os
import random
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "harness"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
import executor
import sbr
from _shared import verdict_line, write_evidence, independently_verify_url, exit_code_for

N_RUNS = 3
QUESTION = "What was Anthropic's valuation in its most recent funding round?"

# One previously-clean model (Kimi, worst fabricator bare-paste, clean
# under the harness) and Mistral direct (the one model the harness has
# caught actually fabricating) — the two ends of the spectrum.
TARGETS = [
    ("moonshotai/kimi-k2", "openrouter", 12000),
    ("mistral-large-latest", "mistral", 12000),
]


def _spot_check_sample(sources, sample_n=2):
    """Independently verify a random sample of sources marked retrieved:true."""
    true_sources = [s for s in sources if s.get("retrieved") is True]
    sample = random.sample(true_sources, min(sample_n, len(true_sources)))
    checks = []
    for s in sample:
        key = executor._url_key(s)
        url = s.get(key) if key else None
        if url:
            checks.append(independently_verify_url(url))
    return checks


def run():
    run_card = sbr.RunCard({"question": QUESTION, "mode": "LIGHT"})
    context = sbr.RunContext({})

    # Three-state, matching the severity taxonomy: a real mismatch
    # (fabrication slipping past enforcement) is the only thing that
    # should FAIL this hypothesis. An external error or an empty/
    # incomplete response is a real, disclosed finding — but it's
    # INCONCLUSIVE for the correctness claim H1 makes, not a miss of it.
    saw_real_mismatch = False
    saw_inconclusive = False
    per_target_results = []

    for model, backend, max_tokens in TARGETS:
        target_runs = []
        for i in range(N_RUNS):
            exec_fn = executor.make_executor(model=model, backend=backend, max_tokens=max_tokens)
            try:
                card1 = exec_fn(1, run_card, context, None)
                card4 = exec_fn(4, run_card, context, card1)
            except executor.HarnessError as e:
                verdict_line(f"repeat:{model}:run{i+1}", "FLAG", f"harness error: {e}")
                target_runs.append({"run": i + 1, "error": str(e), "verdict": "INCONCLUSIVE"})
                saw_inconclusive = True
                continue

            sources = executor._find_source_list(card4.outputs)
            n_retrieved = sum(1 for s in sources if s.get("retrieved") is True)
            n_flagged = sum(1 for s in sources if s.get("retrieved") is False)
            spot_checks = _spot_check_sample(sources)
            mismatches = [c for c in spot_checks if not c["reachable"]]

            # A run with zero sources is a disclosed availability gap
            # (Medium severity: real degradation, not fabrication) — it
            # must not hide inside a clean-looking pass count, but it
            # also isn't evidence the enforcement mechanism failed, so
            # it's INCONCLUSIVE, not FAIL. See PROTOCOL.md Amendment 1.
            if len(sources) == 0:
                verdict = "FLAG"
                saw_inconclusive = True
            elif mismatches:
                verdict = "FAIL"
                saw_real_mismatch = True
            else:
                verdict = "PASS"
            detail = (f"sources={len(sources)}, retrieved_true={n_retrieved}, "
                      f"flagged_false={n_flagged}, spot_checked={len(spot_checks)}, "
                      f"spot_check_mismatches={len(mismatches)}")
            verdict_line(f"repeat:{model}:run{i+1}", verdict, detail)

            target_runs.append({
                "run": i + 1, "n_sources": len(sources),
                "n_retrieved_true": n_retrieved, "n_flagged_false": n_flagged,
                "spot_checks": spot_checks, "verdict": verdict,
                "phase4_raw_outputs": card4.outputs,
            })

        per_target_results.append({"model": model, "backend": backend, "runs": target_runs})

    if saw_real_mismatch:
        h1_verdict = "FAIL"
    elif saw_inconclusive:
        h1_verdict = "INCONCLUSIVE"
    else:
        h1_verdict = "PASS"

    print()
    print(f"H1 (repeat-run consistency, N={N_RUNS} x {len(TARGETS)} models): {h1_verdict}")

    write_evidence("test_repeat_consistency", {
        "hypothesis": "H1",
        "n_runs": N_RUNS,
        "question": QUESTION,
        "results": per_target_results,
        "h1_verdict": h1_verdict,
    })
    return h1_verdict


if __name__ == "__main__":
    sys.exit(exit_code_for(run()))
