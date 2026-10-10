from app.matching.weighted_matcher import calculate_weighted_match


def test_exact_core_match_is_not_reused_for_preferred_skill():
    result = calculate_weighted_match(
        resume_skills=["Machine Learning"],
        core_skills=["Machine Learning"],
        preferred_skills=["Predictive Modeling"],
    )

    assert result["score"] == 66.67
    assert len(result["exact_matches"]) == 1
    assert result["related_matches"] == []
    assert result["missing_skills"] == [
        {
            "job_skill": "Predictive Modeling",
            "category": "preferred",
            "points": 0.0,
        }
    ]


def test_related_skill_can_receive_partial_credit_when_unused():
    result = calculate_weighted_match(
        resume_skills=["Predictive Modeling"],
        core_skills=["Machine Learning"],
        preferred_skills=[],
    )

    assert result["score"] == 50.0
    assert result["related_matches"][0]["job_skill"] == "Machine Learning"
    assert result["related_matches"][0]["resume_skill"] == "Predictive Modeling"
