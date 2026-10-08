# app/matching/skill_matcher.py


# Skills that are closely related.
# These can receive partial credit instead of being treated
# as completely unrelated.
RELATED_SKILLS = {
    "github": "git",
}


def normalize_skill(skill: str) -> str:
    """
    Normalize a skill name for comparison.
    """

    return skill.strip().lower()


def calculate_skill_match(
    resume_skills: list[str],
    job_skills: list[str]
) -> dict:
    """
    Compare resume skills with job-required skills.

    Returns:
        - exact matches
        - related matches
        - missing skills
        - match score
    """

    # Normalize skills
    resume_normalized = {
        normalize_skill(skill): skill
        for skill in resume_skills
    }

    job_normalized = {
        normalize_skill(skill): skill
        for skill in job_skills
    }

    exact_matches = []
    related_matches = []
    missing_skills = []

    total_score = 0.0

    # Check every required job skill
    for job_skill_normalized, job_skill_display in job_normalized.items():

        # --------------------------------
        # Exact match
        # --------------------------------

        if job_skill_normalized in resume_normalized:

            exact_matches.append(
                resume_normalized[job_skill_normalized]
            )

            total_score += 1.0

            continue

        # --------------------------------
        # Related skill match
        # --------------------------------

        related_match_found = False

        for resume_skill_normalized, resume_skill_display in resume_normalized.items():

            related_target = RELATED_SKILLS.get(
                resume_skill_normalized
            )

            if related_target == job_skill_normalized:

                related_matches.append(
                    {
                        "resume_skill": resume_skill_display,
                        "job_skill": job_skill_display,
                    }
                )

                # Related skills receive 50% credit
                total_score += 0.5

                related_match_found = True

                break

        # --------------------------------
        # Missing skill
        # --------------------------------

        if not related_match_found:
            missing_skills.append(job_skill_display)

    # --------------------------------
    # Calculate percentage
    # --------------------------------

    if job_normalized:

        match_score = (
            total_score / len(job_normalized)
        ) * 100

    else:

        match_score = 0.0

    return {
        "exact_matches": exact_matches,
        "related_matches": related_matches,
        "missing_skills": missing_skills,
        "match_score": round(match_score, 2),
    }