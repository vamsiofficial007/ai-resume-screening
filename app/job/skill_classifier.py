import re


CORE_SECTION_KEYWORDS = [
    "requirements",
    "required",
    "required skills",
    "must have",
    "must-have",
    "mandatory",
    "essential",
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
    "qualifications",
    "minimum qualifications",
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
    """Find the earliest occurrence of any section keyword."""
    positions = []

    for keyword in keywords:
        position = text.find(keyword.casefold())

        if position != -1:
            positions.append(position)

    return min(positions) if positions else None

def remove_duplicates_case_insensitive(skills: list[str]) -> list[str]:
    """
    Remove duplicate skills without considering letter case.
    Preserve the spelling and order of the first occurrence.
    """
    unique_skills = []
    seen = set()

    for skill in skills:
        normalized_skill = skill.casefold()

        if normalized_skill not in seen:
            unique_skills.append(skill)
            seen.add(normalized_skill)

    return unique_skills

def classify_job_skills(job_text: str, extracted_skills: list[str]) -> dict:
    """
    Classify extracted job skills into core or preferred categories.
    Skills in core sections take priority over preferred sections.
    Skills in responsibility sections are not automatically core.
    Duplicate skills are removed case-insensitively.
    """
    text_lower = job_text.casefold()

    core_skills = []
    preferred_skills = []

    # Find section headings.
    core_position = find_section_position(
        text_lower, CORE_SECTION_KEYWORDS
    )
    preferred_position = find_section_position(
        text_lower, PREFERRED_SECTION_KEYWORDS
    )

    # Find the beginning of the first responsibilities/other section.
    other_positions = [
        text_lower.find(keyword)
        for keyword in OTHER_SECTION_KEYWORDS
        if text_lower.find(keyword) != -1
    ]
    other_position = min(other_positions) if other_positions else None

    # Return the end of a section at the next recognized heading.
    def section_end(start, keywords):
        if start is None:
            return None

        positions = [
            text_lower.find(keyword, start + 1)
            for keyword in keywords
        ]
        positions = [p for p in positions if p != -1]

        return min(positions) if positions else len(text_lower)

    core_end = section_end(
        core_position,
        PREFERRED_SECTION_KEYWORDS + OTHER_SECTION_KEYWORDS,
    )
    preferred_end = section_end(
        preferred_position,
        CORE_SECTION_KEYWORDS + OTHER_SECTION_KEYWORDS,
    )

    # Locate every occurrence of each extracted skill.
    for skill in extracted_skills:
        skill_lower = skill.casefold()

        positions = [
            match.start()
            for match in re.finditer(
                re.escape(skill_lower),
                text_lower,
            )
        ]

        # If the skill isn't mentioned in the job description,
        # preserve the existing default: classify it as core.
        if not positions:
            core_skills.append(skill)
            continue

        in_core = (
            core_position is not None
            and core_end is not None
            and any(
                core_position <= pos < core_end
                for pos in positions
            )
        )

        in_preferred = (
            preferred_position is not None
            and preferred_end is not None
            and any(
                preferred_position <= pos < preferred_end
                for pos in positions
            )
        )

        if in_core:
            core_skills.append(skill)
        elif in_preferred:
            preferred_skills.append(skill)
        elif (
            other_position is not None
            and all(pos >= other_position for pos in positions)
        ):
            # Skills appearing only in responsibilities are not
            # automatically treated as required skills.
            continue
        else:
            # Preserve the default for skills outside recognized sections.
            core_skills.append(skill)

    # Remove duplicates case-insensitively.
    core_skills = remove_duplicates_case_insensitive(core_skills)
    preferred_skills = remove_duplicates_case_insensitive(
        preferred_skills
    )

    # Core takes priority if a skill occurs in both categories.
    core_names = {skill.casefold() for skill in core_skills}

    preferred_skills = [
        skill
        for skill in preferred_skills
        if skill.casefold() not in core_names
    ]

    return {
        "core_skills": core_skills,
        "preferred_skills": preferred_skills,
        "core_count": len(core_skills),
        "preferred_count": len(preferred_skills),
    }
