from app.parser.resume_parser import extract_text
from app.extraction.skills_extractor import extract_skills
from app.extraction.skill_evidence import analyze_skill_evidence
from app.improvement_plan import generate_improvement_plan
from app.job.job_parser import analyze_job_description
from app.matching.weighted_matcher import calculate_weighted_match
from app.recommendations.recommendation_engine import generate_recommendations
from app.recommendations.improvement_engine import generate_improvement_suggestions


RESUME_PATH = "data/resumes/resume.pdf"

JOB_DESCRIPTION_PATH = "data/job_descriptions/ai_ml_intern.txt"


def run_screening():

    print("\n" + "=" * 60)
    print("          AI RESUME SCREENING SYSTEM")
    print("=" * 60)

    # ---------------------------------------------------------
    # 1. RESUME
    # ---------------------------------------------------------

    print("\n[1] READING RESUME")
    print("-" * 60)

    resume_text = extract_text(RESUME_PATH)

    print("Resume processed successfully! ✅")

    # ---------------------------------------------------------
    # 2. RESUME SKILLS
    # ---------------------------------------------------------

    print("\n[2] EXTRACTING RESUME SKILLS")
    print("-" * 60)

    resume_skills = extract_skills(resume_text)

    print(f"Skills detected: {len(resume_skills)}")

    for skill in resume_skills:
        print(f"  • {skill}")

    # ---------------------------------------------------------
    # 2.5 SKILL EVIDENCE ANALYSIS
    # ---------------------------------------------------------

    print("\n[2.5] ANALYZING SKILL EVIDENCE")
    print("-" * 60)

    evidence_results = analyze_skill_evidence(
        resume_text,
        resume_skills
    )

    for evidence in evidence_results:

        print(
            f"  • {evidence['skill']} → "
            f"{evidence['status']} | "
            f"Confidence: {evidence['confidence']} | "
            f"Strength: {evidence['evidence_strength']}"
        )

    # ---------------------------------------------------------
    # CREATE EVIDENCE LOOKUP
    # ---------------------------------------------------------

    evidence_lookup = {
        evidence["skill"]: evidence
        for evidence in evidence_results
    }

    # ---------------------------------------------------------
    # 3. JOB DESCRIPTION
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
    # 4. MATCHING
    # ---------------------------------------------------------

    print("\n[4] CALCULATING WEIGHTED MATCH")
    print("-" * 60)

    result = calculate_weighted_match(
        resume_skills=resume_skills,
        core_skills=core_skills,
        preferred_skills=preferred_skills,
    )

    # ---------------------------------------------------------
    # MATCH RESULT
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
    # EXACT MATCHES WITH EVIDENCE
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

        resume_skill = match["resume_skill"]

        evidence = evidence_lookup.get(
            resume_skill
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

            resume_skill = match["resume_skill"]

            evidence = evidence_lookup.get(
                resume_skill
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

    if core_gaps:

        print("\nHIGH PRIORITY — CORE")

        for skill in core_gaps:
            print(f"  ❌ {skill['job_skill']}")

    else:

        print("\nHIGH PRIORITY — CORE")
        print("  None 🎉")

    # ---------------------------------------------------------
    # MATCH EXPLANATION & RECOMMENDATIONS
    # ---------------------------------------------------------

    recommendations = generate_recommendations(
    result,
    evidence_lookup
)

    print("\nMATCH EXPLANATION & RECOMMENDATIONS")
    print("-" * 60)

    # ---------------------------------------------------------
    # RESUME IMPROVEMENT SUGGESTIONS
    # ---------------------------------------------------------

    improvement_suggestions = generate_improvement_suggestions(
        result["missing_skills"]
    )

    print("\nRESUME IMPROVEMENT SUGGESTIONS")
    print("-" * 60)

    if improvement_suggestions:

        for index, suggestion in enumerate(
            improvement_suggestions,
            start=1
        ):

            print(
                f"\n{index}. {suggestion['skill']}"
            )

            print(
                f"   Priority: "
                f"{suggestion['priority']}"
            )

            print(
                f"   Reason: "
                f"{suggestion['reason']}"
            )

            print(
                f"   Action: "
                f"{suggestion['action']}"
            )

    else:

        print("  No improvement suggestions.")

    # ---------------------------------------------------------
    # RESUME IMPROVEMENT PLAN
    # ---------------------------------------------------------

    improvement_plans = generate_improvement_plan(
    result["missing_skills"]
)

    print("\nRESUME IMPROVEMENT PLAN")
    print("-" * 60)

    for index, plan in enumerate(
        improvement_plans,
        start=1
    ):

        print(
            f"\n{index}. {plan['skill']}"
        )

        print(
            f"   Priority: "
            f"{plan['priority']}"
        )

        print(
            f"   Gap: "
            f"{plan['gap']}"
        )

        print("   Action Plan:")

        for action in plan["actions"]:

            print(
                f"   • {action}"
            )

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

    if preferred_gaps:

        print("\nOPTIONAL — PREFERRED")

        for skill in preferred_gaps:

            print(
                f"  ❌ {skill['job_skill']}"
            )

    else:

        print("\nOPTIONAL — PREFERRED")
        print("  None 🎉")

    # ---------------------------------------------------------
    # COMPLETE
    # ---------------------------------------------------------

    print("\n" + "=" * 60)
    print("                    COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    run_screening()