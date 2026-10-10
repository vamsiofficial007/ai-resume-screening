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

def test_missing_skill_is_reported_when_related_resume_skill_is_already_used():
    result = calculate_weighted_match(
        resume_skills=["Machine Learning"],
        core_skills=["Artificial Intelligence", "Deep Learning"],
        preferred_skills=[],
    )

    assert len(result["related_matches"]) == 1
    assert result["related_matches"][0]["resume_skill"] == "Machine Learning"

    assert result["missing_skills"] == [
        {
            "job_skill": "Deep Learning",
            "category": "core",
            "points": 0.0,
        }
    ]

    assert result["score"] == 25.0

def test_duplicate_core_requirement_does_not_hide_another_missing_skill():
    result = calculate_weighted_match(
        resume_skills=["Python"],
        core_skills=["Python", "Python", "SQL"],
        preferred_skills=[],
    )

    assert result["missing_skills"] == [
        {
            "job_skill": "SQL",
            "category": "core",
            "points": 0.0,
        }
    ]

    assert result["score"] == 50.0

def test_case_insensitive_duplicate_core_requirements_count_once():
    result = calculate_weighted_match(
        resume_skills=["Python"],
        core_skills=["Python", "PYTHON", "SQL"],
        preferred_skills=[],
    )

    assert result["missing_skills"] == [
        {
            "job_skill": "SQL",
            "category": "core",
            "points": 0.0,
        }
    ]

    assert result["score"] == 50.0


def test_core_skill_takes_priority_over_case_insensitive_preferred_duplicate():
    result = calculate_weighted_match(
        resume_skills=["Python"],
        core_skills=["Python"],
        preferred_skills=["PYTHON"],
    )

    assert result["score"] == 100.0
    assert len(result["exact_matches"]) == 1
    assert result["related_matches"] == []
    assert result["missing_skills"] == []
