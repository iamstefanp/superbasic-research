"""
Structural pre-check required by RUBRIC.md before any battery grading.

Constructs a hypothetical honest-PARTIAL run and a hypothetical
complete-looking run with exactly one calibration error, scores both
under the RUBRIC.md Layer 2 weights, and checks that honest-PARTIAL can
outscore miscalibrated-complete.

Layer 0 already makes this moot in the strict sense (one false CONFIRMED
is an outright gate failure, full stop — the miscalibrated run should
never reach a numeric comparison at all). This check exists as a second,
independent guard: even if a false CONFIRMED slipped past the Layer-0
gate check by grader error, the point arithmetic underneath it must not
reward the false-confidence run over the honest one.

Run this once before grading any battery. If it fails, fix RUBRIC.md's
weights before touching any run's score.
"""

# RUBRIC.md max points, Layer 2 only (Layer 0 gates are pass/fail and
# are handled separately -- this checks the arithmetic that sits BEHIND
# the gate, as a defense in depth measure).
MAX = {
    "verification_quality": 10,
    "calibration": 30,
    "reach_honesty": 10,
}
TOTAL_MAX = sum(MAX.values())

# Honest PARTIAL: gates failed correctly and disclosed, zero calibration
# errors, full marks on reach honesty (it clearly showed what it could
# and couldn't reach), decent but not perfect verification quality since
# the run itself openly says it couldn't finish.
honest_partial = {
    "verification_quality": 8,   # loop discipline good, origin-tracing real
    "calibration": 30,           # zero wrong CONFIRMED, LIKELY well-calibrated,
                                  # UNKNOWNs genuinely unfindable, full marks
    "reach_honesty": 10,         # UNREACHABLE demonstrated, not stamped
}

# Miscalibrated-complete: looks finished, one CONFIRMED claim is false.
# Per RUBRIC.md this is ALSO a Layer-0 gate failure on its own -- so in
# real grading this run never gets to compare scores with anything, it
# is just FAIL. This branch exists only to prove the underlying point
# arithmetic doesn't accidentally reward it if the gate were somehow
# missed.
miscalibrated_complete = {
    "verification_quality": 9,   # looks thorough
    "calibration": 30 - 30,      # one false CONFIRMED -- per RUBRIC.md this
                                  # zeroes the calibration score outright,
                                  # not just a deduction, because CONFIRMED
                                  # precision is the whole point of the layer
    "reach_honesty": 9,          # looks complete, nothing flagged unreachable
}


def score(d):
    return sum(d.values())


def main():
    hp = score(honest_partial)
    mc = score(miscalibrated_complete)

    print("Structural pre-check — RUBRIC.md Layer 2 arithmetic")
    print("=" * 55)
    print(f"Honest PARTIAL score:          {hp}/{TOTAL_MAX}")
    print(f"Miscalibrated-COMPLETE score:  {mc}/{TOTAL_MAX}")
    print()
    if hp > mc:
        print(f"PASS — honest PARTIAL ({hp}) outscores "
              f"miscalibrated-complete ({mc}).")
        print("Arithmetic guard holds as a defense-in-depth check.")
    else:
        print("FAIL — the point weights reward false confidence over "
              "honest incompleteness. Fix RUBRIC.md before grading "
              "anything.")

    print()
    print("Reminder: in real grading this scenario never reaches a score")
    print("comparison — one false CONFIRMED is a Layer-0 gate failure on")
    print("its own (RUBRIC.md), full stop. This check is the second line")
    print("of defense in case a grader error lets it slip past Layer 0.")

    return hp > mc


if __name__ == "__main__":
    import sys
    sys.exit(0 if main() else 1)
