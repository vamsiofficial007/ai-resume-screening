from app.recommendations.recommendation_engine import (
    generate_recommendations,
)


def test_strong_area_from_high_evidence():
    match_result = {
        "exact_matches": [
            {
                "resume_skill": "Python",
                "job_skill": "Python",
                "category": "core",
                "points": 2.0,
            }
        ],
        "related_matches": [],
        "missing_skills": [],
        "score": 100.0,
    }

    evidence_lookup = {
        "Python": {
            "confidence": "Very High",
        }
    }

    result = generate_recommendations(
        match_result,
        evidence_lookup,
    )

    assert result["strong_areas"] == ["Python"]
    assert result["supported_areas"] == []
    assert result["weak_areas"] == []


def test_supported_area_from_medium_evidence():
    match_result = {
        "exact_matches": [
            {
                "resume_skill": "Python",
                "job_skill": "Python",
                "category": "core",
                "points": 2.0,
            }
        ],
        "related_matches": [],
        "missing_skills": [],
        "score": 100.0,
    }

    evidence_lookup = {
        "Python": {
            "confidence": "Medium",
        }
    }

    result = generate_recommendations(
        match_result,
        evidence_lookup,
    )

    assert result["strong_areas"] == []
    assert result["supported_areas"] == ["Python"]
    assert result["weak_areas"] == []


def test_weak_area_from_low_evidence():
    match_result = {
        "exact_matches": [
            {
                "resume_skill": "Python",
                "job_skill": "Python",
                "category": "core",
                "points": 2.0,
            }
        ],
        "related_matches": [],
        "missing_skills": [],
        "score": 100.0,
    }

    evidence_lookup = {
        "Python": {
            "confidence": "Low",
        }
    }

    result = generate_recommendations(
        match_result,
        evidence_lookup,
    )

    assert result["strong_areas"] == []
    assert result["supported_areas"] == []
    assert result["weak_areas"] == ["Python"]


def test_related_area():
    match_result = {
        "exact_matches": [],
        "related_matches": [
            {
                "resume_skill": "Predictive Modeling",
                "job_skill": "Machine Learning",
                "category": "core",
                "points": 1.0,
            }
        ],
        "missing_skills": [],
        "score": 50.0,
    }

    result = generate_recommendations(
        match_result,
        {},
    )

    assert result["related_areas"] == [
        "Predictive Modeling"
    ]


def test_core_and_preferred_missing_skills():
    match_result = {
        "exact_matches": [],
        "related_matches": [],
        "missing_skills": [
            {
                "job_skill": "SQL",
                "category": "core",
            },
            {
                "job_skill": "TensorFlow",
                "category": "preferred",
            },
        ],
        "score": 30.0,
    }

    result = generate_recommendations(
        match_result,
        {},
    )

    assert result["priority_skills"] == ["SQL"]
    assert result["optional_skills"] == ["TensorFlow"]


def test_assessment_for_high_score():
    match_result = {
        "exact_matches": [],
        "related_matches": [],
        "missing_skills": [],
        "score": 85.0,
    }

    result = generate_recommendations(
        match_result,
        {},
    )

    assert "strong match" in result["overall_assessment"]


def test_assessment_for_low_score():
    match_result = {
        "exact_matches": [],
        "related_matches": [],
        "missing_skills": [],
        "score": 30.0,
    }

    result = generate_recommendations(
        match_result,
        {},
    )

    assert "limited match" in result["overall_assessment"]
