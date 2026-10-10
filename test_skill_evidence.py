from app.extraction.skill_evidence import (
    find_skill_evidence,
    analyze_skill_evidence,
)


def test_project_evidence_is_very_high():
    resume_text = """
    PROJECTS

    Customer Delinquency Risk Analysis
    Built a Python machine learning model for risk prediction.
    """

    result = find_skill_evidence(
        resume_text,
        "Python",
    )

    assert result["status"] == "Evidence Found"
    assert result["confidence"] == "Very High"
    assert result["evidence_strength"] == "Project"
    assert "projects" in result["sections"]
    assert "python" in result["matched_keywords"]


def test_skills_section_evidence_is_medium():
    resume_text = """
    TECHNICAL SKILLS

    Python, SQL, Machine Learning
    """

    result = find_skill_evidence(
        resume_text,
        "Python",
    )

    assert result["status"] == "Evidence Found"
    assert result["confidence"] == "Medium"
    assert result["evidence_strength"] == "Skills Section"
    assert "skills" in result["sections"]


def test_missing_skill():
    resume_text = """
    TECHNICAL SKILLS

    Python, SQL
    """

    result = find_skill_evidence(
        resume_text,
        "TensorFlow",
    )

    assert result["status"] == "Missing"
    assert result["confidence"] == "None"
    assert result["evidence_strength"] == "None"
    assert result["sections"] == []
    assert result["matched_keywords"] == []


def test_multiple_skill_evidence():
    resume_text = """
    TECHNICAL SKILLS

    Python, SQL, Pandas
    """

    results = analyze_skill_evidence(
        resume_text,
        ["Python", "SQL", "TensorFlow"],
    )

    assert len(results) == 3

    assert results[0]["skill"] == "Python"
    assert results[0]["status"] == "Evidence Found"

    assert results[1]["skill"] == "SQL"
    assert results[1]["status"] == "Evidence Found"

    assert results[2]["skill"] == "TensorFlow"
    assert results[2]["status"] == "Missing"


def test_artificial_intelligence_recognizes_ml_ai_in_skills():
    resume_text = """
    TECHNICAL SKILLS

    ML/AI: Scikit-learn, TensorFlow, PyTorch
    """

    result = find_skill_evidence(
        resume_text,
        "Artificial Intelligence",
    )

    assert result["status"] == "Evidence Found"
    assert result["confidence"] == "Medium"
    assert result["evidence_strength"] == "Skills Section"
    assert "skills" in result["sections"]
    assert "ml/ai" in result["matched_keywords"]


def test_data_analysis_recognizes_eda_in_projects():
    resume_text = """
    PROJECTS

    Customer Churn Prediction
    Performed EDA and feature engineering on telecom data.
    """

    result = find_skill_evidence(
        resume_text,
        "Data Analysis",
    )

    assert result["status"] == "Evidence Found"
    assert result["confidence"] == "Very High"
    assert result["evidence_strength"] == "Project"
    assert "projects" in result["sections"]
    assert "eda" in result["matched_keywords"]
