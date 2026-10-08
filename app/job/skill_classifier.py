CORE_SECTION_KEYWORDS = [
    "requirements",
    "required",
    "required skills",
    "must have",
    "must-have",
    "mandatory",
    "essential",
    "qualifications",
    "minimum qualifications",
]

PREFERRED_SECTION_KEYWORDS = [
    "preferred",
    "preferred skills",
    "nice to have",
    "nice-to-have",
    "good to have",
    "good-to-have",
    "bonus",
    "additional skills",
    "desired skills",
]

OTHER_SECTION_KEYWORDS = [
    "responsibilities",
    "responsibility",
    "job responsibilities",
    "what you will do",
    "what you'll do",
    "duties",
    "about the role",
    "role",
]


def find_section_position(text: str, keywords: list[str]):
    """
    Find the earliest occurrence of any section keyword.
    """

    positions = []

    for keyword in keywords:
        position = text.find(keyword)

        if position != -1:
            positions.append(position)

    if not positions:
        return None

    return min(positions)


def classify_job_skills(job_text: str, extracted_skills: list[str]) -> dict:
    """
    Classify extracted job skills into core and preferred skills.
    """

    text_lower = job_text.lower()

    core_skills = []
    preferred_skills = []

    preferred_position = find_section_position(
        text_lower,
        PREFERRED_SECTION_KEYWORDS
    )

    # Find where another section begins after Preferred Skills
    other_section_positions = []

    for keyword in OTHER_SECTION_KEYWORDS:
        position = text_lower.find(keyword)

        if (
            position != -1
            and preferred_position is not None
            and position > preferred_position
        ):
            other_section_positions.append(position)

    if other_section_positions:
        preferred_end = min(other_section_positions)
    else:
        preferred_end = len(text_lower)

    # ---------------------------------------------------------
    # Classify every extracted skill
    # ---------------------------------------------------------

    for skill in extracted_skills:

        skill_lower = skill.lower()

        skill_position = text_lower.find(skill_lower)

        if skill_position == -1:
            core_skills.append(skill)
            continue

        # Skill is inside Preferred section
        if (
            preferred_position is not None
            and preferred_position < skill_position < preferred_end
        ):
            preferred_skills.append(skill)

        else:
            core_skills.append(skill)

    # Remove duplicates
    core_skills = list(dict.fromkeys(core_skills))
    preferred_skills = list(dict.fromkeys(preferred_skills))

    # Core always has priority
    preferred_skills = [
        skill
        for skill in preferred_skills
        if skill not in core_skills
    ]

    return {
        "core_skills": core_skills,
        "preferred_skills": preferred_skills,
        "core_count": len(core_skills),
        "preferred_count": len(preferred_skills),
    }