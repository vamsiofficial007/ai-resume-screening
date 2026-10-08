from app.improvement_plan import generate_improvement_plan


missing_skills = [
    "SQL",
    "NLP",
    "Pandas",
    "NumPy",
    "Scikit-learn",
    "Git",
    "Deep Learning"
]

core_skills = [
    "Python",
    "SQL",
    "Machine Learning",
    "Data Analysis",
    "Exploratory Data Analysis",
    "NLP",
    "Pandas",
    "NumPy",
    "Scikit-learn",
    "Git",
    "GitHub"
]

preferred_skills = [
    "Deep Learning",
    "Artificial Intelligence",
    "Predictive Modeling"
]


plans = generate_improvement_plan(
    missing_skills,
    core_skills,
    preferred_skills
)


print("=" * 60)
print("             RESUME IMPROVEMENT PLAN")
print("=" * 60)

for index, plan in enumerate(plans, start=1):

    print(f"\n{index}. {plan['skill']}")
    print(f"   Priority: {plan['priority']}")
    print(f"   Gap: {plan['gap']}")
    print("   Action Plan:")

    for action in plan["actions"]:
        print(f"   • {action}")
