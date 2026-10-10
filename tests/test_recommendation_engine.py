from app.recommendations.recommendation_engine import (
    generate_recommendations,
)


def test_missing_core_skill_becomes_priority():
    match_result = {
        "score": 50.0,
        "exact_matches": [],
        "related_matches": [],
        "missing_skills": [
            {"job_skill": "SQL", "category": "core", "points": 0.0},
        ],
    }

    result = generate_recommendations(match_result, {})

    assert result["priority_skills"] == ["SQL"]
    assert result["optional_skills"] == []


def test_missing_preferred_skill_becomes_optional():
    match_result = {
        "score": 80.0,
        "exact_matches": [],
        "related_matches": [],
        "missing_skills": [
            {
                "job_skill": "Predictive Modeling",
                "category": "preferred",
                "points": 0.0,
            },
        ],
    }

    result = generate_recommendations(match_result, {})

    assert result["priority_skills"] == []
    assert result["optional_skills"] == ["Predictive Modeling"]


def test_no_missing_skills_produces_empty_recommendation_lists():
    match_result = {
        "score": 100.0,
        "exact_matches": [],
        "related_matches": [],
        "missing_skills": [],
    }

    result = generate_recommendations(match_result, {})

    assert result["priority_skills"] == []
    assert result["optional_skills"] == []
