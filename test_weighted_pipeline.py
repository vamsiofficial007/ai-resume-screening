from app.parser.resume_parser import extract_text
from app.extraction.skills_extractor import extract_skills

from app.job.job_parser import analyze_job_description
from app.matching.weighted_matcher import calculate_weighted_match


RESUME_PATH = "data/resumes/resume.pdf"

JOB_DESCRIPTION_PATH = "data/job_descriptions/ai_ml_intern.txt"


from app.job.job_parser import analyze_job_description
from app.matching.weighted_matcher import calculate_weighted_match


RESUME_PATH = "data/resumes/resume.pdf"

JOB_DESCRIPTION_PATH = "data/job_descriptions/ai_ml_intern.txt"


def main():

    print("\n" + "=" * 60)
    print("          AI RESUME WEIGHTED MATCHING")
    print("=" * 60)

    # ---------------------------------------------------------
    # 1. EXTRACT RESUME
    # ---------------------------------------------------------

    print("\n[1] READING RESUME")
    print("-" * 60)

    resume_text = extract_text(RESUME_PATH)

    print("Resume processed successfully! ✅")

    # ---------------------------------------------------------
    # 2. EXTRACT RESUME SKILLS
    # ---------------------------------------------------------

    print("\n[2] EXTRACTING RESUME SKILLS")
    print("-" * 60)

    resume_skills = extract_skills(resume_text)

    print(f"Skills detected: {len(resume_skills)}")

    for skill in resume_skills:
        print(f"  • {skill}")

    # ---------------------------------------------------------
    # 3. ANALYZE JOB DESCRIPTION
    # ---------------------------------------------------------

    print("\n[3] ANALYZING JOB DESCRIPTION")
    print("-" * 60)

    job_result = analyze_job_description(
        JOB_DESCRIPTION_PATH
    )

    core_skills = job_result["core_skills"]
    preferred_skills = job_result["preferred_skills"]

    print("\nCore Skills:")

    for skill in core_skills:
        print(f"  • {skill}")

    print("\nPreferred Skills:")

    for skill in preferred_skills:
        print(f"  • {skill}")

    # ---------------------------------------------------------
    # 4. WEIGHTED MATCH
    # ---------------------------------------------------------

    print("\n[4] CALCULATING WEIGHTED MATCH")
    print("-" * 60)

    result = calculate_weighted_match(
        resume_skills=resume_skills,
        core_skills=core_skills,
        preferred_skills=preferred_skills,
    )

    # ---------------------------------------------------------
    # 5. DISPLAY FINAL RESULT
    # ---------------------------------------------------------

    print("\n" + "=" * 60)
    print("                 MATCH RESULT")
    print("=" * 60)

    print(f"\nWeighted Score: {result['score']}%")

    print(
        f"Earned Points: "
        f"{result['earned_points']} / "
        f"{result['total_possible_points']}"
    )

    # ---------------------------------------------------------
    # USED RESUME SKILLS
    # ---------------------------------------------------------

    print("\nUSED RESUME SKILLS")
    print("-" * 60)

    for skill in result["used_resume_skills"]:
        print(f"  • {skill}")

    # ---------------------------------------------------------
    # EXACT MATCHES
    # ---------------------------------------------------------

    print("\nEXACT MATCHES")
    print("-" * 60)

    if result["exact_matches"]:

        for match in result["exact_matches"]:

            print(
                f"✅ {match['job_skill']} → "
                f"{match['resume_skill']} "
                f"({match['category']}) "
                f"+{match['points']} points"
            )

    else:

        print("No exact matches.")

    # ---------------------------------------------------------
    # RELATED MATCHES
    # ---------------------------------------------------------

    print("\nRELATED MATCHES")
    print("-" * 60)

    if result["related_matches"]:

        for match in result["related_matches"]:

            print(
                f"🔗 {match['job_skill']} → "
                f"{match['resume_skill']} "
                f"({match['category']}) "
                f"+{match['points']} points"
            )

    else:

        print("No related matches.")

    # ---------------------------------------------------------
    # MISSING SKILLS
    # ---------------------------------------------------------

    print("\nMISSING SKILLS")
    print("-" * 60)

    if result["missing_skills"]:

        for skill in result["missing_skills"]:

            print(
                f"❌ {skill['job_skill']} "
                f"({skill['category']})"
            )

    else:

        print("No missing skills! 🎉")

    print("\n" + "=" * 60)
    print("                    COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    main()




