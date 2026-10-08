from app.extraction.skills_extractor import extract_skills
from app.job.skill_classifier import classify_job_skills


def analyze_job_description(job_description_file: str) -> dict:
    """
    Read a job description from a file, extract skills,
    and classify them as core or preferred.
    """

    with open(job_description_file, "r", encoding="utf-8") as file:
        job_description = file.read()

    skills = extract_skills(job_description)

    classified_skills = classify_job_skills(
        job_description,
        skills
    )

    return {
        "required_skills": skills,
        "skill_count": len(skills),
        "core_skills": classified_skills["core_skills"],
        "preferred_skills": classified_skills["preferred_skills"],
        "core_count": classified_skills["core_count"],
        "preferred_count": classified_skills["preferred_count"],
    }