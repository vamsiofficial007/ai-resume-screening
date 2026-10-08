from app.screening.screening_engine import screen_candidate
from app.reporting import generate_screening_report


RESUME_PATH = "data/resumes/resume.pdf"
JOB_DESCRIPTION_PATH = "data/job_descriptions/ai_ml_intern.txt"


def test_generate_screening_report():

    screening = screen_candidate(
        RESUME_PATH,
        JOB_DESCRIPTION_PATH
    )

    report = generate_screening_report(
        screening
    )

    # ---------------------------------------------------------
    # CANDIDATE
    # ---------------------------------------------------------

    assert report["candidate"]["skills_detected"] == 18

    # ---------------------------------------------------------
    # MATCH
    # ---------------------------------------------------------

    assert report["match"]["score"] == 96.0
    assert report["match"]["earned_points"] == 24.0
    assert report["match"]["total_possible_points"] == 25.0

    # ---------------------------------------------------------
    # CORE REQUIREMENTS
    # ---------------------------------------------------------

    assert report["requirements"]["core"]["total"] == 11
    assert report["requirements"]["core"]["matched"] == 11
    assert report["requirements"]["core"]["missing"] == []

    # ---------------------------------------------------------
    # PREFERRED REQUIREMENTS
    # ---------------------------------------------------------

    assert report["requirements"]["preferred"]["total"] == 3
    assert report["requirements"]["preferred"]["matched"] == 2

    assert (
        "Predictive Modeling"
        in report["requirements"]["preferred"]["missing"]
    )

    # ---------------------------------------------------------
    # STRENGTHS
    # ---------------------------------------------------------

    assert "Python" in report["strengths"]["strong_areas"]
    assert "NumPy" in report["strengths"]["supported_areas"]

    # ---------------------------------------------------------
    # RECOMMENDATIONS
    # ---------------------------------------------------------

    assert (
        "Predictive Modeling"
        in report["recommendations"]["optional_skills"]
    )

    # ---------------------------------------------------------
    # IMPROVEMENT
    # ---------------------------------------------------------

    assert len(
        report["improvement"]["plans"]
    ) == 1

    assert (
        report["improvement"]["plans"][0]["skill"]
        == "Predictive Modeling"
    )

