from app.job.skill_classifier import classify_job_skills


def test_duplicate_core_skills_are_removed():
    result = classify_job_skills(
        "Requirements: Python SQL",
        ["Python", "SQL", "Python"]
    )

    assert result["core_skills"] == ["Python", "SQL"]
    assert result["core_count"] == 2


def test_duplicate_preferred_skills_are_removed():
    result = classify_job_skills(
        "Preferred Skills: Python TensorFlow",
        ["Python", "TensorFlow", "TensorFlow"]
    )

    assert result["preferred_skills"] == ["Python", "TensorFlow"]
    assert result["preferred_count"] == 2


def test_core_skill_takes_priority_over_preferred():
    result = classify_job_skills(
        "Requirements: Python SQL\n"
        "Preferred Skills: Python TensorFlow",
        ["Python", "SQL", "TensorFlow"]
    )

    assert result["core_skills"] == ["Python", "SQL"]
    assert result["preferred_skills"] == ["TensorFlow"]
    assert result["core_count"] == 2
    assert result["preferred_count"] == 1


def test_category_counts_match_final_skill_lists():
    result = classify_job_skills(
        "Requirements: Python SQL\n"
        "Preferred Skills: TensorFlow Git",
        ["Python", "SQL", "TensorFlow", "Git"]
    )

    assert result["core_count"] == len(result["core_skills"])
    assert result["preferred_count"] == len(result["preferred_skills"])

def test_core_skill_takes_priority_over_preferred_case_insensitively():
    result = classify_job_skills(
        "Requirements: Python\n"
        "Preferred Skills: TensorFlow",
        ["Python", "python", "TensorFlow"]
    )

    assert len(result["core_skills"]) == 1
    assert result["core_skills"][0].lower() == "python"
    assert all(
        skill.lower() != "python"
        for skill in result["preferred_skills"]
    )
    assert result["core_count"] == 1
