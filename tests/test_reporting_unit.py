
from app.reporting import generate_screening_report


def make_screening():
    """Create a small, predictable screening result for tests."""
    return {
        "match_result": {
            "score": 50.0,
            "earned_points": 3.0,
            "total_possible_points": 6.0,
            "missing_skills": [
                {"job_skill": "SQL", "category": "core"},
                {"job_skill": "NLP", "category": "preferred"},
            ],
        },
        "job_result": {
            "core_skills": ["Python", "SQL"],
            "preferred_skills": ["NLP", "Git"],
        },
        "recommendations": {
            "strong_areas": ["Python"],
            "supported_areas": ["Pandas"],
            "related_areas": ["Machine Learning"],
            "priority_skills": ["SQL"],
            "optional_skills": ["NLP"],
            "overall_assessment": "Some skill gaps remain.",
        },
        "resume_skills": ["Python", "Pandas"],
        "evidence_results": [
            {"skill": "Python", "confidence": "VERY_HIGH"},
            {"skill": "Pandas", "confidence": "medium"},
            {"skill": "SQL", "confidence": "low"},
            {"skill": "Git", "confidence": "unknown"},
        ],
        "improvement_suggestions": ["Practice SQL."],
        "improvement_plans": [
            {"skill": "SQL", "priority": "HIGH"}
        ],
    }


def test_report_groups_evidence_by_confidence():
    report = generate_screening_report(make_screening())

    assert report["evidence"]["very_high"] == ["Python"]
    assert report["evidence"]["medium"] == ["Pandas"]
    assert report["evidence"]["low"] == ["SQL"]

    # Unknown confidence values should not enter known categories.
    assert "Git" not in report["evidence"]["low"]


def test_report_counts_core_and_preferred_requirements():
    report = generate_screening_report(make_screening())

    assert report["requirements"]["core"]["total"] == 2
    assert report["requirements"]["core"]["matched"] == 1
    assert report["requirements"]["core"]["missing"] == ["SQL"]

    assert report["requirements"]["preferred"]["total"] == 2
    assert report["requirements"]["preferred"]["matched"] == 1
    assert report["requirements"]["preferred"]["missing"] == ["NLP"]


def test_report_preserves_match_score_and_recommendations():
    report = generate_screening_report(make_screening())

    assert report["match"]["score"] == 50.0
    assert report["match"]["earned_points"] == 3.0
    assert report["match"]["total_possible_points"] == 6.0

    assert report["recommendations"]["priority_skills"] == ["SQL"]
    assert report["recommendations"]["optional_skills"] == ["NLP"]
    assert report["improvement"]["plans"][0]["skill"] == "SQL"