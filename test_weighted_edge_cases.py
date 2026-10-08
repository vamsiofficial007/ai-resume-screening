from app.matching.weighted_matcher import calculate_weighted_match


def print_result(title, result):
    print("=" * 60)
    print(title)
    print("=" * 60)

    print(f"Score: {result['score']}%")
    print(
        f"Points: {result['earned_points']} "
        f"/ {result['total_possible_points']}"
    )

    print("\nExact matches:")
    for item in result["exact_matches"]:
        print(
            f"  ✅ {item['resume_skill']} → "
            f"{item['job_skill']} "
            f"+{item['points']}"
        )

    print("\nRelated matches:")
    for item in result["related_matches"]:
        print(
            f"  🟡 {item['resume_skill']} → "
            f"{item['job_skill']} "
            f"+{item['points']}"
        )

    print("\nMissing:")
    for item in result["missing_skills"]:
        print(
            f"  ❌ {item['job_skill']} "
            f"({item['category']})"
        )

    print()


# ---------------------------------------------------------
# TEST 1 — Exact match
# ---------------------------------------------------------

result = calculate_weighted_match(
    resume_skills=["Python"],
    core_skills=["Python"],
    preferred_skills=[],
)

assert result["score"] == 100.0
assert result["earned_points"] == 2.0
assert len(result["exact_matches"]) == 1
assert len(result["related_matches"]) == 0
assert len(result["missing_skills"]) == 0

print_result("TEST 1 — EXACT MATCH", result)

print("✅ TEST 1 PASSED")


# ---------------------------------------------------------
# TEST 2 — Related match
# ---------------------------------------------------------

result = calculate_weighted_match(
    resume_skills=["Predictive Modeling"],
    core_skills=["Machine Learning"],
    preferred_skills=[],
)

assert result["score"] == 50.0
assert result["earned_points"] == 1.0
assert len(result["exact_matches"]) == 0
assert len(result["related_matches"]) == 1
assert len(result["missing_skills"]) == 0

print_result("TEST 2 — RELATED MATCH", result)

print("✅ TEST 2 PASSED")


# ---------------------------------------------------------
# TEST 3 — Missing skill
# ---------------------------------------------------------

result = calculate_weighted_match(
    resume_skills=[],
    core_skills=["Python"],
    preferred_skills=[],
)

assert result["score"] == 0.0
assert result["earned_points"] == 0.0
assert len(result["exact_matches"]) == 0
assert len(result["related_matches"]) == 0
assert len(result["missing_skills"]) == 1

print_result("TEST 3 — MISSING SKILL", result)

print("✅ TEST 3 PASSED")


# ---------------------------------------------------------
# TEST 4 — Core skill has more weight
# ---------------------------------------------------------

result = calculate_weighted_match(
    resume_skills=["Python"],
    core_skills=["Python"],
    preferred_skills=["Git"],
)

assert result["score"] == 66.67
assert result["earned_points"] == 2.0
assert result["total_possible_points"] == 3.0

print_result("TEST 4 — CORE WEIGHT", result)

print("✅ TEST 4 PASSED")


# ---------------------------------------------------------
# TEST 5 — Same resume skill cannot be used twice
# ---------------------------------------------------------

result = calculate_weighted_match(
    resume_skills=["GitHub"],
    core_skills=[],
    preferred_skills=["GitHub", "Git"],
)

assert result["earned_points"] == 1.0
assert len(result["exact_matches"]) == 1
assert len(result["related_matches"]) == 0
assert len(result["missing_skills"]) == 1

print_result("TEST 5 — DUPLICATE PREVENTION", result)

print("✅ TEST 5 PASSED")


# ---------------------------------------------------------
# FINAL RESULT
# ---------------------------------------------------------

print("=" * 60)
print("🎉 ALL WEIGHTED MATCH TESTS PASSED")
print("=" * 60)
