from app.screening.screening_engine import screen_candidate
from app.reporting import generate_screening_report


RESUME_PATH = "data/resumes/resume.pdf"
JOB_DESCRIPTION_PATH = "data/job_descriptions/ai_ml_intern.txt"


def print_screening_report(report: dict):
    """
    Display the recruiter-friendly screening report.
    """

    print("\n" + "=" * 60)
    print("              SCREENING REPORT")
    print("=" * 60)

    print("\nCANDIDATE")
    print("-" * 60)

    print(
        f"Skills Detected: "
        f"{report['candidate']['skills_detected']}"
    )

    print("\nMATCH SCORE")
    print("-" * 60)

    print(
        f"Weighted Match: "
        f"{report['match']['score']}%"
    )

    print(
        f"Points: "
        f"{report['match']['earned_points']} / "
        f"{report['match']['total_possible_points']}"
    )

    print("\nREQUIREMENTS")
    print("-" * 60)

    core = report["requirements"]["core"]
    preferred = report["requirements"]["preferred"]

    print(
        f"Core: "
        f"{core['matched']} / "
        f"{core['total']} matched"
    )

    print(
        f"Preferred: "
        f"{preferred['matched']} / "
        f"{preferred['total']} matched"
    )

    print("\nSKILL GAPS")
    print("-" * 60)

    all_missing = (
        core["missing"]
        + preferred["missing"]
    )

    if all_missing:
        for skill in all_missing:
            print(f"  ❌ {skill}")
    else:
        print("  None 🎉")

    print("\nSTRENGTHS")
    print("-" * 60)

    strong_areas = report["strengths"]["strong_areas"]

    if strong_areas:
        for skill in strong_areas:
            print(f"  ✅ {skill}")
    else:
        print("  None")

    supported_areas = report["strengths"]["supported_areas"]

    if supported_areas:
        print("\nSupported Areas:")

        for skill in supported_areas:
            print(f"  • {skill}")

    related_areas = report["strengths"]["related_areas"]

    if related_areas:
        print("\nRelated Areas:")

        for skill in related_areas:
            print(f"  🔗 {skill}")

    print("\nEVIDENCE CONFIDENCE")
    print("-" * 60)

    evidence = report["evidence"]

    confidence_levels = [
        "very_high",
        "high",
        "medium",
        "low",
    ]

    for confidence in confidence_levels:
        if evidence[confidence]:

            print(
                f"\n{confidence.replace('_', ' ').title()}:"
            )

            for skill in evidence[confidence]:
                print(f"  • {skill}")

    print("\nRECOMMENDATIONS")
    print("-" * 60)

    priority_skills = (
        report["recommendations"]["priority_skills"]
    )

    if priority_skills:
        print("Priority Skills:")

        for skill in priority_skills:
            print(f"  • {skill}")
    else:
        print("Priority Skills: None 🎉")

    optional_skills = (
        report["recommendations"]["optional_skills"]
    )

    if optional_skills:
        print("\nOptional Skills:")

        for skill in optional_skills:
            print(f"  • {skill}")

    print("\nOverall Assessment:")

    print(
        f"  {report['recommendations']['overall_assessment']}"
    )

    print("\nIMPROVEMENT PLAN")
    print("-" * 60)

    plans = report["improvement"]["plans"]

    if plans:

        for index, plan in enumerate(
            plans,
            start=1
        ):

            print(
                f"\n{index}. {plan['skill']}"
            )

            print(
                f"   Priority: {plan['priority']}"
            )

            print(
                f"   Gap: {plan['gap']}"
            )

            print("   Action Plan:")

            for action in plan["actions"]:
                print(f"   • {action}")

    else:
        print("  No improvement plan required.")

    print("\n" + "=" * 60)
    print("                 SCREENING COMPLETE")
    print("=" * 60)


def run_screening():

    print("\n" + "=" * 60)
    print("          AI RESUME SCREENING SYSTEM")
    print("=" * 60)

    screening = screen_candidate(
        RESUME_PATH,
        JOB_DESCRIPTION_PATH
    )

    report = generate_screening_report(
        screening
    )

    print_screening_report(
        report
    )


if __name__ == "__main__":
    run_screening()
