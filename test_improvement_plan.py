from app.improvement_plan import generate_improvement_plan


missing_skills = [
    {
        "job_skill": "Predictive Modeling",
        "category": "preferred"
    }
]


plans = generate_improvement_plan(missing_skills)


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
