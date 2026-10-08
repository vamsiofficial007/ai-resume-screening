from app.job.job_parser import analyze_job_description


job_description_file = "data/sample_job.txt"

result = analyze_job_description(job_description_file)

print("\nExtracted Skills:")

for skill in result["required_skills"]:
    print(f"- {skill}")

print(f"\nTotal Skills: {result['skill_count']}")