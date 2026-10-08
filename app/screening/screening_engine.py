from app.parser.resume_parser import extract_text
from app.extraction.skills_extractor import extract_skills
from app.extraction.skill_evidence import analyze_skill_evidence
from app.improvement_plan import generate_improvement_plan
from app.job.job_parser import analyze_job_description
from app.matching.weighted_matcher import calculate_weighted_match
from app.recommendations.recommendation_engine import generate_recommendations
from app.recommendations.improvement_engine import generate_improvement_suggestions


def screen_candidate(
    resume_path: str,
    job_description_path: str
) -> dict:
    """
    Run the complete resume screening pipeline.

    Returns:
        A structured dictionary containing the screening results.
    """

    # ---------------------------------------------------------
    # 1. READ RESUME
    # ---------------------------------------------------------

    resume_text = extract_text(resume_path)

    # ---------------------------------------------------------
    # 2. EXTRACT RESUME SKILLS
    # ---------------------------------------------------------

    resume_skills = extract_skills(resume_text)

    # ---------------------------------------------------------
    # 3. ANALYZE SKILL EVIDENCE
    # ---------------------------------------------------------

    evidence_results = analyze_skill_evidence(
        resume_text,
        resume_skills
    )

    evidence_lookup = {
        evidence["skill"]: evidence
        for evidence in evidence_results
    }

    # ---------------------------------------------------------
    # 4. ANALYZE JOB DESCRIPTION
    # ---------------------------------------------------------

    job_result = analyze_job_description(
        job_description_path
    )

    core_skills = job_result["core_skills"]
    preferred_skills = job_result["preferred_skills"]

    # ---------------------------------------------------------
    # 5. CALCULATE WEIGHTED MATCH
    # ---------------------------------------------------------

    match_result = calculate_weighted_match(
        resume_skills=resume_skills,
        core_skills=core_skills,
        preferred_skills=preferred_skills,
    )

    # ---------------------------------------------------------
    # 6. GENERATE RECOMMENDATIONS
    # ---------------------------------------------------------

    recommendations = generate_recommendations(
        match_result,
        evidence_lookup
    )

    # ---------------------------------------------------------
    # 7. GENERATE IMPROVEMENT SUGGESTIONS
    # ---------------------------------------------------------

    improvement_suggestions = generate_improvement_suggestions(
        match_result["missing_skills"]
    )

    # ---------------------------------------------------------
    # 8. GENERATE IMPROVEMENT PLAN
    # ---------------------------------------------------------

    improvement_plans = generate_improvement_plan(
        match_result["missing_skills"]
    )

    # ---------------------------------------------------------
    # 9. RETURN STRUCTURED RESULT
    # ---------------------------------------------------------

    return {
        "resume_text": resume_text,
        "resume_skills": resume_skills,
        "evidence_results": evidence_results,
        "evidence_lookup": evidence_lookup,
        "job_result": job_result,
        "match_result": match_result,
        "recommendations": recommendations,
        "improvement_suggestions": improvement_suggestions,
        "improvement_plans": improvement_plans,
    }
