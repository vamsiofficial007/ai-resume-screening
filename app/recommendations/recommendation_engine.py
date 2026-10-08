def generate_recommendations(
    match_result: dict,
    evidence_lookup: dict
) -> dict:
    """
    Generate deterministic candidate recommendations
    from weighted matching results.
    """

    exact_matches = match_result.get("exact_matches", [])
    related_matches = match_result.get("related_matches", [])
    missing_skills = match_result.get("missing_skills", [])

    # ---------------------------------------------------------
    # EVIDENCE-AWARE AREAS
    # ---------------------------------------------------------

    strong_areas = []
    supported_areas = []
    weak_areas = []

    for match in exact_matches:

        skill = match["resume_skill"]

        evidence = evidence_lookup.get(skill)

        if not evidence:
            continue

        confidence = evidence["confidence"]

        # Very High / High → Strong Area
        if confidence in ["Very High", "High"]:

            if skill not in strong_areas:
                strong_areas.append(skill)

        # Medium → Supported Area
        elif confidence == "Medium":

            if skill not in supported_areas:
                supported_areas.append(skill)

        # Low → Weak Evidence
        elif confidence == "Low":

            if skill not in weak_areas:
                weak_areas.append(skill)

    # ---------------------------------------------------------
    # RELATED AREAS
    # ---------------------------------------------------------

    related_areas = []

    for match in related_matches:

        skill = match["resume_skill"]

        if skill not in related_areas:
            related_areas.append(skill)

    # ---------------------------------------------------------
    # PRIORITY SKILLS
    # ---------------------------------------------------------

    priority_skills = []

    for skill in missing_skills:

        if skill["category"] == "core":
            priority_skills.append(skill["job_skill"])

    # ---------------------------------------------------------
    # OPTIONAL SKILLS
    # ---------------------------------------------------------

    optional_skills = []

    for skill in missing_skills:

        if skill["category"] == "preferred":
            optional_skills.append(skill["job_skill"])

    # ---------------------------------------------------------
    # OVERALL ASSESSMENT
    # ---------------------------------------------------------

    score = match_result.get("score", 0)

    if score >= 80:

        assessment = (
            "Your resume demonstrates a strong match with "
            "the job requirements. Most important skills "
            "are already covered."
        )

    elif score >= 60:

        assessment = (
            "Your resume demonstrates a good match with "
            "the job requirements, but some skills could "
            "be strengthened to improve your fit."
        )

    elif score >= 40:

        assessment = (
            "Your resume demonstrates a good foundation, "
            "but several important job requirements are "
            "currently missing."
        )

    else:

        assessment = (
            "Your resume currently has a limited match "
            "with the job requirements. Focus on the missing "
            "core skills to improve your profile."
        )

    # ---------------------------------------------------------
    # RETURN RESULTS
    # ---------------------------------------------------------

    return {
        "strong_areas": strong_areas,
        "supported_areas": supported_areas,
        "weak_areas": weak_areas,
        "related_areas": related_areas,
        "priority_skills": priority_skills,
        "optional_skills": optional_skills,
        "overall_assessment": assessment,
    }