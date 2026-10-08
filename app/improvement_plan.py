def generate_improvement_plan(missing_skills):
    """
    Generate an actionable improvement plan
    from the structured missing-skill data.
    """

    plans = []

    for skill_data in missing_skills:

        skill = skill_data["job_skill"]
        category = skill_data["category"]

        if category == "core":

            priority = "HIGH"
            gap = "Missing core skill"

            actions = [
                f"Learn {skill} fundamentals",
                f"Practice {skill} through hands-on exercises",
                f"Build a small project using {skill}",
                f"Add {skill} to the resume after gaining practical experience"
            ]

        else:

            priority = "OPTIONAL"
            gap = "Missing preferred skill"

            actions = [
                f"Learn the fundamentals of {skill}",
                f"Practice {skill} through a small project",
                f"Build practical experience with {skill}",
                f"Add {skill} to the resume after gaining experience"
            ]

        plans.append({
            "skill": skill,
            "priority": priority,
            "gap": gap,
            "actions": actions
        })

    return plans
