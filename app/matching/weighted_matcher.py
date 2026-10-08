from typing import Optional


CORE_WEIGHT = 2.0
PREFERRED_WEIGHT = 1.0

EXACT_CREDIT = 1.0
RELATED_CREDIT = 0.5
MISSING_CREDIT = 0.0


# Known related-skill relationships.
# This is intentionally simple for now.
RELATED_SKILLS = {
    "Git": ["GitHub"],
    "GitHub": ["Git"],

    "Machine Learning": [
        "Predictive Modeling",
    ],

    "Data Analysis": [
        "Exploratory Data Analysis",
    ],

    "Exploratory Data Analysis": [
        "Data Analysis",
    ],

    "Artificial Intelligence": [
        "Machine Learning",
        "Deep Learning",
    ],

    "Deep Learning": [
        "Machine Learning",
    ],
}


def find_related_skill(
    job_skill: str,
    resume_skills: list[str],
    used_resume_skills: set[str] | None = None
) -> Optional[str]:
    """
    Find an unused related resume skill for a job skill.
    """

    if used_resume_skills is None:
        used_resume_skills = set()

    related_skills = RELATED_SKILLS.get(job_skill, [])

    for resume_skill in resume_skills:

        if resume_skill in used_resume_skills:
            continue

        if resume_skill in related_skills:
            return resume_skill

    return None


def calculate_weighted_match(
    resume_skills: list[str],
    core_skills: list[str],
    preferred_skills: list[str],
) -> dict:
    """
    Calculate weighted skill matching between a resume
    and a job description.
    """

    exact_matches = []
    related_matches = []
    missing_skills = []

    earned_points = 0.0
    total_possible_points = 0.0

    # Keep track of resume skills that have already
    # been used for a match.
    used_resume_skills = set()

    # ---------------------------------------------------------
    # RESERVE RESUME SKILLS FOR EXACT MATCHES
    # ---------------------------------------------------------

    exact_resume_skills = set(core_skills) | set(preferred_skills)

    exact_resume_skills = {
        skill
        for skill in exact_resume_skills
        if skill in resume_skills
    }

    # ---------------------------------------------------------
    # CORE SKILLS
    # ---------------------------------------------------------

    for job_skill in core_skills:

        weight = CORE_WEIGHT
        total_possible_points += weight

        # -----------------------------------------------------
        # Exact match
        # -----------------------------------------------------

        if (
            job_skill in resume_skills
            and job_skill not in used_resume_skills
        ):

            exact_matches.append({
                "job_skill": job_skill,
                "resume_skill": job_skill,
                "category": "core",
                "points": weight,
            })

            used_resume_skills.add(job_skill)

            earned_points += weight * EXACT_CREDIT

        else:

            # -------------------------------------------------
            # Related match
            # -------------------------------------------------

            related_skill = find_related_skill(
                job_skill,
                resume_skills,
                used_resume_skills
            )

            if (
                related_skill
                and related_skill not in used_resume_skills
                and related_skill not in exact_resume_skills
            ):

                points = weight * RELATED_CREDIT

                related_matches.append({
                    "job_skill": job_skill,
                    "resume_skill": related_skill,
                    "category": "core",
                    "credit": RELATED_CREDIT,
                    "points": points,
                })

                used_resume_skills.add(related_skill)

                earned_points += points

            else:

                # If the exact skill exists in the resume but
                # was already used for another JD skill, don't
                # report it as missing again.
                if job_skill not in used_resume_skills:

                    missing_skills.append({
                        "job_skill": job_skill,
                        "category": "core",
                        "points": MISSING_CREDIT,
                    })

    # ---------------------------------------------------------
    # PREFERRED SKILLS
    # ---------------------------------------------------------

    for job_skill in preferred_skills:

        weight = PREFERRED_WEIGHT
        total_possible_points += weight

        # -----------------------------------------------------
        # Exact match
        # -----------------------------------------------------

        if (
            job_skill in resume_skills
            and job_skill not in used_resume_skills
        ):

            exact_matches.append({
                "job_skill": job_skill,
                "resume_skill": job_skill,
                "category": "preferred",
                "points": weight,
            })

            used_resume_skills.add(job_skill)

            earned_points += weight * EXACT_CREDIT

        else:

            # -------------------------------------------------
            # Related match
            # -------------------------------------------------

            related_skill = find_related_skill(
                job_skill,
                resume_skills,
                used_resume_skills
            )

            if (
                related_skill
                and related_skill not in used_resume_skills
                and related_skill not in exact_resume_skills
            ):

                points = weight * RELATED_CREDIT

                related_matches.append({
                    "job_skill": job_skill,
                    "resume_skill": related_skill,
                    "category": "preferred",
                    "credit": RELATED_CREDIT,
                    "points": points,
                })

                used_resume_skills.add(related_skill)

                earned_points += points

            else:

                # If the exact skill was already used,
                # don't report it as missing.
                if job_skill not in used_resume_skills:

                    missing_skills.append({
                        "job_skill": job_skill,
                        "category": "preferred",
                        "points": MISSING_CREDIT,
                    })

    # ---------------------------------------------------------
    # FINAL SCORE
    # ---------------------------------------------------------

    if total_possible_points > 0:

        score = (
            earned_points /
            total_possible_points
        ) * 100

    else:

        score = 0.0

    return {
        "score": round(score, 2),

        "earned_points": round(
            earned_points,
            2
        ),

        "total_possible_points": round(
            total_possible_points,
            2
        ),

        "exact_matches": exact_matches,

        "related_matches": related_matches,

        "missing_skills": missing_skills,

        "core_skill_count": len(core_skills),

        "preferred_skill_count": len(preferred_skills),
        "used_resume_skills": sorted(used_resume_skills),
    }
