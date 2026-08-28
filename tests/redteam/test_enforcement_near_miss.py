"""
test_enforcement_near_miss.py — H3: enforcement precision.

Attacks _enforce_real_urls directly: can a fabricated or meaningfully-
different URL be smuggled past it by looking almost like a real one?
Pure function test, no live model call — the fast, always-run layer.

Verdict for H3: zero false negatives (no fabricated/near-miss URL ever
accepted as real). False positives on purely cosmetic variants of a
genuinely-retrieved URL are an accepted, documented tradeoff, not a
failure — see PROTOCOL.md.
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "harness"))
import executor
from _shared import verdict_line, write_evidence

REAL_URLS_SEEN = {
    "https://www.example.com/article",
    "https://www.cnbc.com/2026/story.html",
    "https://www.reuters.com/business/real-piece",
}

# Each case: (label, cited_url, expect_accepted, is_attack)
# expect_accepted=True means the harness SHOULD mark retrieved:true.
# is_attack=True means a fabricated/near-miss URL trying to pass as real
# — these MUST be rejected (false negative = Critical/High finding).
# is_attack=False + expect_accepted=False is a known false-positive
# tradeoff (Low severity, not a hypothesis failure).
CASES = [
    ("exact_match_control",       "https://www.example.com/article",              True,  False),
    ("trailing_slash",            "https://www.example.com/article/",             False, False),
    ("tracking_query_param",      "https://www.cnbc.com/2026/story.html?utm_source=x", False, False),
    ("domain_case_difference",    "https://www.CNBC.com/2026/story.html",         False, False),
    ("url_fragment",              "https://www.reuters.com/business/real-piece#section-2", False, False),
    ("wholly_fabricated",         "https://www.reuters.com/business/invented-piece-that-never-existed", False, True),
    ("plausible_lookalike_domain","https://www.reuters-news.com/business/real-piece", False, True),
    # Redirect case: the tool call resolved a real short/pre-redirect URL
    # to REAL_URLS_SEEN's canonical form; the model cites the
    # pre-redirect URL it originally searched. Current policy: exact
    # match only, so this is REJECTED — a real, legitimate source flagged
    # as unretrieved. Documented here as a known false-positive tradeoff
    # (Low severity), not a hypothesis failure, since the alternative
    # (fuzzy/redirect-aware matching) reopens the door to exactly the
    # near-miss attacks the other cases above are designed to catch.
    ("redirect_pre_redirect_url",  "https://reut.rs/short-link-that-redirects", False, False),
]


def _build_outputs(url):
    return {"Intel Items": [{"URL": url, "facts": "test fixture"}]}


def run():
    results = []
    false_negative_found = False

    for label, url, expect_accepted, is_attack in CASES:
        outputs = executor._enforce_real_urls(_build_outputs(url), set(REAL_URLS_SEEN))
        actual = outputs["Intel Items"][0]["retrieved"]

        if is_attack and actual is True:
            false_negative_found = True
            verdict = "FAIL"
            detail = f"ATTACK URL ACCEPTED AS REAL — url={url!r}"
        elif actual == expect_accepted:
            verdict = "PASS"
            detail = f"retrieved={actual} as expected"
        else:
            verdict = "FLAG" if not is_attack else "FAIL"
            detail = f"retrieved={actual}, expected={expect_accepted} (documented false-positive tradeoff)" if not is_attack else f"unexpected: retrieved={actual}"

        verdict_line(label, verdict, detail)
        results.append({"label": label, "url": url, "expected": expect_accepted,
                         "actual": actual, "is_attack": is_attack, "verdict": verdict})

    h3_pass = not false_negative_found
    print()
    print(f"H3 (enforcement precision — zero false negatives): {'PASS' if h3_pass else 'FAIL'}")

    write_evidence("test_enforcement_near_miss", {
        "hypothesis": "H3",
        "real_urls_seen": sorted(REAL_URLS_SEEN),
        "cases": results,
        "h3_verdict": "PASS" if h3_pass else "FAIL",
    })
    return h3_pass


if __name__ == "__main__":
    ok = run()
    sys.exit(0 if ok else 1)
