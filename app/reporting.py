def generate_screening_report(screening: dict) -> dict:
    """
    Convert the complete screening result into a
    clean recruiter-friendly report.
    """

    match_result = screening["match_result"]
    job_result = screening["job_result"]
    recommendations = screening["recommendations"]

    core_skills = job_result["core_skills"]
    preferred_skills = job_result["preferred_skills"]

    missing_skills = match_result["missing_skills"]

    core_gaps = [
        skill["job_skill"]
        for skill in missing_skills
        if skill["category"] == "core"
    ]

    preferred_gaps = [
        skill["job_skill"]
        for skill in missing_skills
        if skill["category"] == "preferred"
    ]

    core_matched = len(core_skills) - len(core_gaps)

    preferred_matched = (
        len(preferred_skills) - len(preferred_gaps)
    )

    evidence_summary = {
        "very_high": [],
        "high": [],
        "medium": [],
        "low": [],
    }

    for evidence in screening["evidence_results"]:
        confidence = (
            evidence["confidence"]
            .strip()
            .lower()
            .replace(" ", "_")
        )

        if confidence in evidence_summary:
            evidence_summary[confidence].append(
                evidence["skill"]
            )

    return {
        "candidate": {
            "skills_detected": len(
                screening["resume_skills"]
            ),
        },

        "match": {
            "score": match_result["score"],
            "earned_points": match_result["earned_points"],
            "total_possible_points": match_result[
                "total_possible_points"
            ],
        },

        "requirements": {
            "core": {
                "total": len(core_skills),
                "matched": core_matched,
                "missing": core_gaps,
            },

            "preferred": {
                "total": len(preferred_skills),
                "matched": preferred_matched,
                "missing": preferred_gaps,
            },
        },

        "strengths": {
            "strong_areas": recommendations[
                "strong_areas"
            ],
            "supported_areas": recommendations[
                "supported_areas"
            ],
            "related_areas": recommendations[
                "related_areas"
            ],
        },

        "evidence": evidence_summary,

        "recommendations": {
            "priority_skills": recommendations[
                "priority_skills"
            ],
            "optional_skills": recommendations[
                "optional_skills"
            ],
            "overall_assessment": recommendations[
                "overall_assessment"
            ],
        },

        "improvement": {
            "suggestions": screening[
                "improvement_suggestions"
            ],
            "plans": screening[
                "improvement_plans"
            ],
        },
    }
