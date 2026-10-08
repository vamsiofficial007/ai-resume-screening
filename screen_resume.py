from app.parser.resume_parser import extract_text
from app.extraction.skills_extractor import extract_skills
from app.job.job_parser import analyze_job_description
from app.matching.skill_matcher import calculate_skill_match


RESUME_PATH = "data/resumes/Dola_Vamsi_AI_ML_Internship_Resume.pdf"
JOB_DESCRIPTION_PATH = "data/sample_job.txt"


def main():

    print("\n" + "=" * 60)
    print("             AI RESUME SCREENING")
    print("=" * 60)

    # --------------------------------
    # STEP 1: Extract resume text
    # --------------------------------

    print("\nReading resume...")

    resume_text = extract_text(RESUME_PATH)

    print("Resume processed successfully! ✅")


    # --------------------------------
    # STEP 2: Extract resume skills
    # --------------------------------

    resume_skills = extract_skills(resume_text)

    print("\nCandidate Skills:")

    if resume_skills:
        for skill in resume_skills:
            print(f"  • {skill}")
    else:
        print("  No skills detected.")


    # --------------------------------
    # STEP 3: Analyze job description
    # --------------------------------

    print("\nReading job description...")

    job_result = analyze_job_description(
        JOB_DESCRIPTION_PATH
    )

    job_skills = job_result["required_skills"]

    print("Job description processed successfully! ✅")

    print("\nRequired Skills:")

    if job_skills:
        for skill in job_skills:
            print(f"  • {skill}")
    else:
        print("  No required skills detected.")


    # --------------------------------
    # STEP 4: Calculate skill match
    # --------------------------------

    result = calculate_skill_match(
        resume_skills,
        job_skills
    )


    # --------------------------------
    # STEP 5: Display screening result
    # --------------------------------

    print("\n" + "=" * 60)
    print("                 SCREENING RESULT")
    print("=" * 60)

    print(f"\nMatch Score: {result['match_score']}%")


    # --------------------------------
    # Exact matches
    # --------------------------------

    print("\nExact Matching Skills:")

    if result["exact_matches"]:

        for skill in result["exact_matches"]:
            print(f"  ✅ {skill}")

    else:

        print("  None")


    # --------------------------------
    # Related matches
    # --------------------------------

    print("\nRelated Skills:")

    if result["related_matches"]:

        for match in result["related_matches"]:

            print(
                f"  🟡 {match['resume_skill']} "
                f"→ {match['job_skill']} "
                f"(partial match)"
            )

    else:

        print("  None")


    # --------------------------------
    # Missing skills
    # --------------------------------

    print("\nMissing Skills:")

    if result["missing_skills"]:

        for skill in result["missing_skills"]:
            print(f"  ❌ {skill}")

    else:

        print("  None")


    # --------------------------------
    # Complete
    # --------------------------------

    print("\n" + "=" * 60)
    print("                    COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    main()