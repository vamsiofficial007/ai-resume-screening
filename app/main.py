from app.screening.screening_engine import screen_candidate


RESUME_PATH = "data/resumes/resume.pdf"

JOB_DESCRIPTION_PATH = "data/job_descriptions/ai_ml_intern.txt"


def run_screening():

    print("\n" + "=" * 60)
    print("          AI RESUME SCREENING SYSTEM")
    print("=" * 60)

    # ---------------------------------------------------------
    # RUN SCREENING ENGINE
    # ---------------------------------------------------------

    screening = screen_candidate(
        RESUME_PATH,
        JOB_DESCRIPTION_PATH
    )

    resume_skills = screening["resume_skills"]
    evidence_results = screening["evidence_results"]
    job_result = screening["job_result"]
    result = screening["match_result"]
    recommendations = screening["recommendations"]
    improvement_suggestions = screening["improvement_suggestions"]
    improvement_plans = screening["improvement_plans"]

    # ---------------------------------------------------------
    # RESUME
    # ---------------------------------------------------------

    print("\n[1] READING RESUME")
    print("-" * 60)

    print("Resume processed successfully! ✅")

    # ---------------------------------------------------------
    # RESUME SKILLS
    # ---------------------------------------------------------

    print("\n[2] EXTRACTING RESUME SKILLS")
    print("-" * 60)

    print(f"Skills detected: {len(resume_skills)}")

    for skill in resume_skills:
        print(f"  • {skill}")

    # ---------------------------------------------------------
    # SKILL EVIDENCE
    # ---------------------------------------------------------

    print("\n[2.5] ANALYZING SKILL EVIDENCE")
    print("-" * 60)

    for evidence in evidence_results:

        print(
            f"  • {evidence['skill']} → "
            f"{evidence['status']} | "
            f"Confidence: {evidence['confidence']} | "
            f"Strength: {evidence['evidence_strength']}"
        )

    # ---------------------------------------------------------
    # JOB DESCRIPTION
    # ---------------------------------------------------------

    print("\n[3] ANALYZING JOB DESCRIPTION")
    print("-" * 60)

    print("\nCore Skills:")

    for skill in job_result["core_skills"]:
        print(f"  • {skill}")

    print("\nPreferred Skills:")

    for skill in job_result["preferred_skills"]:
        print(f"  • {skill}")

    # ---------------------------------------------------------
    # MATCH RESULT
    # ---------------------------------------------------------

    print("\n[4] CALCULATING WEIGHTED MATCH")
    print("-" * 60)

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

    for match in result["exact_matches"]:

        print(
            f"✅ {match['job_skill']} → "
            f"{match['resume_skill']} "
            f"({match['category']}) "
            f"+{match['points']} points"
        )

        evidence = screening["evidence_lookup"].get(
            match["resume_skill"]
        )

        if evidence:

            sections = ", ".join(
                evidence["sections"]
            )

            print(
                f"   Evidence: "
                f"{evidence['evidence_strength']} | "
                f"Confidence: "
                f"{evidence['confidence']}"
            )

            print(
                f"   Sections: {sections}"
            )

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

    # ---------------------------------------------------------
    # SKILL GAP ANALYSIS
    # ---------------------------------------------------------

    print("\nSKILL GAP ANALYSIS")
    print("-" * 60)

    core_gaps = [
        skill
        for skill in result["missing_skills"]
        if skill["category"] == "core"
    ]

    preferred_gaps = [
        skill
        for skill in result["missing_skills"]
        if skill["category"] == "preferred"
    ]

    print("\nHIGH PRIORITY — CORE")

    if core_gaps:

        for skill in core_gaps:
            print(f"  ❌ {skill['job_skill']}")

    else:

        print("  None 🎉")

    # ---------------------------------------------------------
    # RESUME IMPROVEMENT SUGGESTIONS
    # ---------------------------------------------------------

    print("\nRESUME IMPROVEMENT SUGGESTIONS")
    print("-" * 60)

    if improvement_suggestions:

        for index, suggestion in enumerate(
            improvement_suggestions,
            start=1
        ):

            print(f"\n{index}. {suggestion['skill']}")
            print(f"   Priority: {suggestion['priority']}")
            print(f"   Reason: {suggestion['reason']}")
            print(f"   Action: {suggestion['action']}")

    else:

        print("  No improvement suggestions.")

    # ---------------------------------------------------------
    # RESUME IMPROVEMENT PLAN
    # ---------------------------------------------------------

    print("\nRESUME IMPROVEMENT PLAN")
    print("-" * 60)

    for index, plan in enumerate(
        improvement_plans,
        start=1
    ):

        print(f"\n{index}. {plan['skill']}")
        print(f"   Priority: {plan['priority']}")
        print(f"   Gap: {plan['gap']}")
        print("   Action Plan:")

        for action in plan["actions"]:
            print(f"   • {action}")

    # ---------------------------------------------------------
    # STRONG AREAS
    # ---------------------------------------------------------

    print("\nSTRONG AREAS")

    if recommendations["strong_areas"]:

        for skill in recommendations["strong_areas"]:
            print(f"  ✅ {skill}")

    else:

        print("  None")

    # ---------------------------------------------------------
    # RELATED AREAS
    # ---------------------------------------------------------

    if recommendations["related_areas"]:

        print("\nRELATED STRENGTHS")

        for skill in recommendations["related_areas"]:
            print(f"  🔗 {skill}")

    # ---------------------------------------------------------
    # PRIORITY SKILLS
    # ---------------------------------------------------------

    print("\nPRIORITY SKILLS TO IMPROVE")

    if recommendations["priority_skills"]:

        for index, skill in enumerate(
            recommendations["priority_skills"],
            start=1
        ):

            print(f"  {index}. {skill}")

    else:

        print("  None 🎉")

    # ---------------------------------------------------------
    # OPTIONAL SKILLS
    # ---------------------------------------------------------

    print("\nOPTIONAL IMPROVEMENT")

    if recommendations["optional_skills"]:

        for skill in recommendations["optional_skills"]:
            print(f"  • {skill}")

    else:

        print("  None 🎉")

    # ---------------------------------------------------------
    # OVERALL ASSESSMENT
    # ---------------------------------------------------------

    print("\nOVERALL ASSESSMENT")

    print(
        f"  {recommendations['overall_assessment']}"
    )

    # ---------------------------------------------------------
    # PREFERRED GAPS
    # ---------------------------------------------------------

    print("\nOPTIONAL — PREFERRED")

    if preferred_gaps:

        for skill in preferred_gaps:
            print(f"  ❌ {skill['job_skill']}")

    else:

        print("  None 🎉")

    # ---------------------------------------------------------
    # COMPLETE
    # ---------------------------------------------------------

    print("\n" + "=" * 60)
    print("                    COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    run_screening()
