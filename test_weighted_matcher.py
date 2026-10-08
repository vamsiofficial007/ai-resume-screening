from app.matching.weighted_matcher import calculate_weighted_match


resume_skills = [
    "Python",
    "Data Analysis",
    "Exploratory Data Analysis",
    "Predictive Modeling",
    "GitHub",
]


core_skills = [
    "Python",
    "SQL",
    "Machine Learning",
    "Artificial Intelligence",
    "Data Analysis",
    "Exploratory Data Analysis",
    "Pandas",
    "NumPy",
]


preferred_skills = [
    "NLP",
    "TensorFlow",
    "Git",
    "GitHub",
]


result = calculate_weighted_match(
    resume_skills,
    core_skills,
    preferred_skills,
)


print("=" * 60)
print("             WEIGHTED SKILL MATCH")
print("=" * 60)

print(f"\nWeighted Score: {result['score']}%")

print(
    f"Earned Points: "
    f"{result['earned_points']} / "
    f"{result['total_possible_points']}"
)


print("\nEXACT MATCHES")
print("-" * 60)

for match in result["exact_matches"]:

    print(
        f"✅ {match['resume_skill']} → "
        f"{match['job_skill']} "
        f"({match['category']}) "
        f"+{match['points']} points"
    )


print("\nRELATED MATCHES")
print("-" * 60)

for match in result["related_matches"]:

    print(
        f"🟡 {match['resume_skill']} → "
        f"{match['job_skill']} "
        f"({match['category']}) "
        f"+{match['points']} points"
    )


print("\nMISSING SKILLS")
print("-" * 60)

for skill in result["missing_skills"]:

    print(
        f"❌ {skill['job_skill']} "
        f"({skill['category']})"
    )


print("\n" + "=" * 60)