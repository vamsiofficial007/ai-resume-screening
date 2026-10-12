
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

st.title("📄 AI Resume Screening System")
st.write(
    "Upload a resume and a job description to analyze "
    "skill compatibility, identify gaps, and get recommendations."
)

st.divider()

resume_file = st.file_uploader(
    "Upload your resume",
    type=["pdf", "docx"],
)

job_description = st.text_area(
    "Paste the job description",
    height=250,
    placeholder=(
        "Paste the job title, required skills, "
        "preferred skills, and responsibilities here..."
    ),
)

if st.button("Analyze Resume", type="primary"):
    if resume_file is None:
        st.error("Please upload a PDF or DOCX resume.")
    elif not job_description.strip():
        st.error("Please paste a job description.")
    else:
        try:
            with st.spinner("Analyzing your resume..."):
                suffix = Path(resume_file.name).suffix.lower()

                with tempfile.TemporaryDirectory() as temp_dir:
                    resume_path = Path(temp_dir) / (
                        "resume" + suffix
                    )
                    job_path = Path(temp_dir) / "job_description.txt"

                    resume_path.write_bytes(
                        resume_file.getvalue()
                    )
                    job_path.write_text(
                        job_description,
                        encoding="utf-8",
                    )

                    screening = screen_candidate(
                        str(resume_path),
                        str(job_path),
                    )

                    report = generate_screening_report(
                        screening
                    )

            st.success("Screening completed successfully!")

            st.header("Screening Results")

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
                f'{core["matched"]} / {core["total"]}',
            )
            col4.metric(
                "Preferred Skills Matched",
                f'{preferred["matched"]} / {preferred["total"]}',
            )

            st.progress(
                max(0.0, min(1.0, float(score) / 100))
            )

            st.subheader("Skill Gaps")

            gap_col1, gap_col2 = st.columns(2)

            with gap_col1:
                st.markdown("**Missing Core Skills**")
                if core["missing"]:
                    for skill in core["missing"]:
                        st.write(f"❌ {skill}")
                else:
                    st.success("No missing core skills!")

            with gap_col2:
                st.markdown("**Missing Preferred Skills**")
                if preferred["missing"]:
                    for skill in preferred["missing"]:
                        st.write(f"▫️ {skill}")
                else:
                    st.success("No missing preferred skills!")

            st.subheader("Strengths")

            strengths = report["strengths"]

            st.markdown("**Strong Areas**")
            if strengths["strong_areas"]:
                st.write(", ".join(strengths["strong_areas"]))
            else:
                st.write("No strong areas identified yet.")

            st.markdown("**Supported Areas**")
            if strengths["supported_areas"]:
                st.write(", ".join(strengths["supported_areas"]))
            else:
                st.write("No additional supported areas identified.")

            st.markdown("**Related Areas**")
            if strengths["related_areas"]:
                st.write(", ".join(strengths["related_areas"]))
            else:
                st.write("No related areas identified.")

            st.subheader("Evidence Confidence")

            evidence = report["evidence"]

            for level, skills in evidence.items():
                with st.expander(
                    f"{level.replace('_', ' ').title()} ({len(skills)})"
                ):
                    if skills:
                        st.write(", ".join(skills))
                    else:
                        st.write("No skills in this category.")

            st.subheader("Recommendations")

            recommendations = report["recommendations"]

            st.markdown("**Priority Skills**")
            if recommendations["priority_skills"]:
                for skill in recommendations["priority_skills"]:
                    st.write(f"🔴 {skill}")
            else:
                st.success("No priority skills identified.")

            st.markdown("**Optional Skills**")
            if recommendations["optional_skills"]:
                for skill in recommendations["optional_skills"]:
                    st.write(f"▫️ {skill}")
            else:
                st.write("No optional skill recommendations.")

            st.info(recommendations["overall_assessment"])

            st.subheader("Improvement Plan")

            plans = report["improvement"]["plans"]

            if plans:
                for index, plan in enumerate(plans, start=1):
                    with st.expander(
                        f'{index}. {plan["skill"]} — {plan["priority"]}'
                    ):
                        st.write(f'**Gap:** {plan["gap"]}')
                        st.write("**Action Plan**")
                        for action in plan["actions"]:
                            st.write(f"- {action}")
            else:
                st.success("No improvement plan required.")

            with st.expander("View detected resume skills"):
                st.write(", ".join(screening["resume_skills"]))

        except Exception as exc:
            st.error(
                "Screening failed. Please check the uploaded "
                "resume and job description."
            )
            st.exception(exc)
