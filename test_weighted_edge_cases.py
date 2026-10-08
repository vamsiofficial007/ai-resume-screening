from app.matching.weighted_matcher import calculate_weighted_match


def test_exact_match():
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


def test_related_match():
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


def test_missing_skill():
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


def test_core_skill_has_more_weight():
    result = calculate_weighted_match(
        resume_skills=["Python"],
        core_skills=["Python"],
        preferred_skills=["Git"],
    )

    assert result["score"] == 66.67
    assert result["earned_points"] == 2.0
    assert result["total_possible_points"] == 3.0


def test_resume_skill_cannot_be_used_twice():
    result = calculate_weighted_match(
        resume_skills=["GitHub"],
        core_skills=[],
        preferred_skills=["GitHub", "Git"],
    )

    assert result["earned_points"] == 1.0
    assert len(result["exact_matches"]) == 1
    assert len(result["related_matches"]) == 0
    assert len(result["missing_skills"]) == 1
