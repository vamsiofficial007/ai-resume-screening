
import streamlit as st
import tempfile
from pathlib import Path

from app.screening.screening_engine import screen_candidate
from app.reporting import generate_screening_report


st.set_page_config(
    page_title="AI Resume Screening System",
    page_icon="📄",
    layout="wide",
)


def save_uploaded_file(uploaded_file, suffix):
    """Save an uploaded file temporarily and return its path."""
    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=suffix,
    ) as temp_file:
        temp_file.write(uploaded_file.getvalue())
        return temp_file.name


def show_skill_list(title, skills):
    st.subheader(title)

    if skills:
        for skill in skills:
            st.write(f"• {skill}")
    else:
        st.caption("None")


st.title("📄 AI Resume Screening System")
st.caption(
    "Analyze resume relevance, identify skill gaps, "
    "and generate personalized improvement recommendations."
)

st.divider()

left, right = st.columns(2)

with left:
    st.subheader("1. Upload Resume")

    resume_file = st.file_uploader(
        "Choose a PDF or DOCX resume",
        type=["pdf", "docx"],
    )

with right:
    st.subheader("2. Job Description")

    job_description = st.text_area(
        "Paste the complete job description",
        height=220,
        placeholder=(
            "Paste the job responsibilities, required skills, "
            "preferred skills, and qualifications here..."
        ),
    )

analyze_clicked = st.button(
    "Analyze Resume",
    type="primary",
    use_container_width=True,
)

if analyze_clicked:
    if resume_file is None:
        st.error("Please upload a PDF or DOCX resume.")

    elif not job_description.strip():
        st.error("Please enter a job description.")

    else:
        resume_path = None
        job_path = None

        try:
            with st.spinner("Analyzing resume and job requirements..."):
                resume_path = save_uploaded_file(
                    resume_file,
                    Path(resume_file.name).suffix.lower(),
                )

                with tempfile.NamedTemporaryFile(
                    mode="w",
                    encoding="utf-8",
                    suffix=".txt",
                    delete=False,
                ) as job_file:
                    job_file.write(job_description)
                    job_path = job_file.name

                screening = screen_candidate(
                    resume_path,
                    job_path,
                )

                report = generate_screening_report(screening)

            st.success("Resume screening completed!")

            st.divider()
            st.header("Screening Dashboard")

            score = report["match"]["score"]
            core = report["requirements"]["core"]
            preferred = report["requirements"]["preferred"]

            col1, col2, col3, col4 = st.columns(4)

            col1.metric("Weighted Match", f"{score}%")
            col2.metric(
                "Skills Detected",
                report["candidate"]["skills_detected"],
            )
            col3.metric(
                "Core Skills Matched",
                f"{core['matched']} / {core['total']}",
            )
            col4.metric(
                "Preferred Skills Matched",
                f"{preferred['matched']} / {preferred['total']}",
            )

            st.progress(
                max(0.0, min(1.0, float(score) / 100))
            )

            st.caption(
                f"Weighted points: "
                f"{report['match']['earned_points']} / "
                f"{report['match']['total_possible_points']}"
            )

            st.divider()

            gaps_tab, strengths_tab, evidence_tab, plan_tab = st.tabs(
                [
                    "Skill Gaps",
                    "Strengths",
                    "Evidence",
                    "Improvement Plan",
                ]
            )

            with gaps_tab:
                gap_col1, gap_col2 = st.columns(2)

                with gap_col1:
                    show_skill_list(
                        "Missing Core Skills",
                        core["missing"],
                    )

                with gap_col2:
                    show_skill_list(
                        "Missing Preferred Skills",
                        preferred["missing"],
                    )

            with strengths_tab:
                show_skill_list(
                    "Strong Areas",
                    report["strengths"]["strong_areas"],
                )

                show_skill_list(
                    "Supported Areas",
                    report["strengths"]["supported_areas"],
                )

                show_skill_list(
                    "Related Areas",
                    report["strengths"]["related_areas"],
                )

            with evidence_tab:
                confidence_labels = {
                    "very_high": "Very High Confidence",
                    "high": "High Confidence",
                    "medium": "Medium Confidence",
                    "low": "Low Confidence",
                }

                for level, label in confidence_labels.items():
                    with st.expander(label):
                        show_skill_list(
                            label,
                            report["evidence"][level],
                        )

            with plan_tab:
                st.subheader("Overall Assessment")
                st.write(
                    report["recommendations"]["overall_assessment"]
                )

                show_skill_list(
                    "Priority Skills",
                    report["recommendations"]["priority_skills"],
                )

                show_skill_list(
                    "Optional Skills",
                    report["recommendations"]["optional_skills"],
                )

                st.subheader("Improvement Suggestions")

                suggestions = report["improvement"]["suggestions"]

                if suggestions:
                    for suggestion in suggestions:
                        st.write(f"• {suggestion}")
                else:
                    st.write("No additional suggestions.")

                st.subheader("Personalized Learning Plans")

                plans = report["improvement"]["plans"]

                if plans:
                    for plan in plans:
                        with st.expander(plan["skill"]):
                            st.write(f"**Priority:** {plan['priority']}")
                            st.write(f"**Gap:** {plan['gap']}")

                            for action in plan["actions"]:
                                st.write(f"• {action}")
                else:
                    st.write("No improvement plan required.")

        except Exception as error:
            st.error(
                "Screening could not be completed. "
                "Check the input files and terminal error details."
            )
            st.exception(error)

        finally:
            for temp_path in (resume_path, job_path):
                if temp_path:
                    try:
                        Path(temp_path).unlink(missing_ok=True)
                    except OSError:
                        pass
