from app.job.job_parser import analyze_job_description
from app.matching.skill_matcher import calculate_skill_match


def test_skill_matching():
    # Analyze job description
    job_result = analyze_job_description(
        "data/sample_job.txt"
    )

    job_skills = job_result["required_skills"]

    # Example resume skills
    resume_skills = [
        "Python",
        "SQL",
        "Machine Learning",
        "Pandas",
        "NumPy",
        "TensorFlow",
        "Git",
    ]

    # Calculate match
    result = calculate_skill_match(
        resume_skills,
        job_skills
    )

    # Current matcher API
    assert "exact_matches" in result
    assert "related_matches" in result
    assert "missing_skills" in result
    assert "match_score" in result

    # Basic validity checks
    assert isinstance(result["exact_matches"], list)
    assert isinstance(result["related_matches"], list)
    assert isinstance(result["missing_skills"], list)

    assert 0 <= result["match_score"] <= 100
