from app.job.job_parser import analyze_job_description
from app.matching.skill_matcher import calculate_skill_match


# Analyze job description
job_result = analyze_job_description("data/sample_job.txt")

job_skills = job_result["required_skills"]


# Example resume skills
resume_skills = [
    "Python",
    "SQL",
    "Machine Learning",
    "Pandas",
    "NumPy",
    "TensorFlow",
    "Git",
]


# Calculate match
result = calculate_skill_match(
    resume_skills,
    job_skills
)


print("\n==============================")
print("       SKILL MATCH RESULT")
print("==============================")

print("\nMatching Skills:")

for skill in result["matching_skills"]:
    print(f"✅ {skill}")


print("\nMissing Skills:")

for skill in result["missing_skills"]:
    print(f"❌ {skill}")


print(f"\nMatch Score: {result['match_score']}%")