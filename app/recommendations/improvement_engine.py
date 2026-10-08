# Skill-specific resume improvement suggestions

SKILL_IMPROVEMENTS = {

    "SQL": {
        "priority": "HIGH",
        "reason": "SQL is a core requirement in the job description.",
        "action": (
            "If you have SQL experience, add it to your "
            "technical skills or relevant projects."
        ),
    },

    "NLP": {
        "priority": "HIGH",
        "reason": "NLP is a core requirement in the job description.",
        "action": (
            "If you have NLP experience, highlight it through "
            "a project, coursework, or practical experience."
        ),
    },

    "Pandas": {
        "priority": "HIGH",
        "reason": "Pandas is a core requirement in the job description.",
        "action": (
            "If you have used Pandas, demonstrate it through "
            "a data-analysis project or relevant experience."
        ),
    },

    "NumPy": {
        "priority": "HIGH",
        "reason": "NumPy is a core requirement in the job description.",
        "action": (
            "If you have NumPy experience, mention it in your "
            "technical skills or a relevant project."
        ),
    },

    "Scikit-learn": {
        "priority": "HIGH",
        "reason": "Scikit-learn is a core requirement in the job description.",
        "action": (
            "If you have used Scikit-learn, highlight it through "
            "a machine-learning project or relevant experience."
        ),
    },

    "Git": {
        "priority": "HIGH",
        "reason": "Git is a core requirement in the job description.",
        "action": (
            "If you have Git experience, mention your Git workflow "
            "or repository-based projects."
        ),
    },

    "Deep Learning": {
        "priority": "OPTIONAL",
        "reason": "Deep Learning is a preferred requirement.",
        "action": (
            "If you have Deep Learning experience, consider "
            "highlighting it through a relevant project."
        ),
    },
}


def generate_improvement_suggestions(missing_skills: list[dict]) -> list[dict]:
    """
    Generate resume improvement suggestions from missing skills.
    """

    suggestions = []

    for skill in missing_skills:

        skill_name = skill["job_skill"]

        improvement = SKILL_IMPROVEMENTS.get(skill_name)

        if improvement is None:
            continue

        suggestions.append({
            "skill": skill_name,
            "category": skill["category"],
            "priority": improvement["priority"],
            "reason": improvement["reason"],
            "action": improvement["action"],
        })

    return suggestions
