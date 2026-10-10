import re


# ---------------------------------------------------------
# SKILL EVIDENCE ANALYZER
# ---------------------------------------------------------

SKILL_KEYWORDS = {
    "Python": [
        "python",
    ],

    "SQL": [
        "sql",
        "mysql",
        "postgresql",
        "postgres",
        "sqlite",
    ],

    "Machine Learning": [
        "machine learning",
        "machine-learning",
        "ml",
    ],

    "Deep Learning": [
        "deep learning",
        "deep-learning",
        "neural network",
        "neural networks",
    ],

    "Artificial Intelligence": [
        "artificial intelligence",
        "ai/ml",
        "ml/ai",
        "ai & ml",
        "ai fundamentals",
        "ai engineer",
        "ai engineering",
        "ai model",
        "ai models",
        "ai project",
        "ai projects",
    ],

    "Data Analysis": [
        "data analysis",
        "data analytics",
        "data analysis project",
        "exploratory data analysis",
        "eda",
    ],

    "Exploratory Data Analysis": [
        "exploratory data analysis",
        "eda",
    ],

    "NLP": [
        "natural language processing",
        "nlp",
    ],

    "Pandas": [
        "pandas",
    ],

    "NumPy": [
        "numpy",
        "numpy library",
    ],

    "Scikit-learn": [
        "scikit-learn",
        "scikit learn",
        "sklearn",
    ],

    "Git": [
        "git",
        "git version control",
        "git repository",
        "git workflow",
    ],

    "GitHub": [
        "github",
        "github repository",
        "github desktop",
    ],

    "Predictive Modeling": [
        "predictive modeling",
        "predictive modelling",
    ],

    "Flutter": [
        "flutter",
    ],
}


# ---------------------------------------------------------
# RESUME SECTION HEADINGS
# ---------------------------------------------------------

SECTION_HEADINGS = {
    "objective": [
        "objective",
        "career objective",
    ],

    "education": [
        "education",
    ],

    "skills": [
        "technical skills",
        "technical skills & tools",
        "skills",
        "skills & technologies",
    ],

    "projects": [
        "projects",
        "project",
        "academic projects",
        "personal projects",
    ],

    "experience": [
        "experience",
        "internship experience",
        "work experience",
        "professional experience",
    ],

    "certifications": [
        "certifications",
        "certificates",
    ],

    "achievements": [
        "achievements",
    ],

    "leadership": [
        "leadership & content creation",
        "leadership",
        "content creation",
    ],

    "extracurriculars": [
        "extracurriculars",
        "extracurricular activities",
    ],

    "languages": [
        "languages",
    ],

    "additional_strengths": [
        "additional strengths",
    ],
}


def detect_sections(resume_text):
    """
    Detect actual resume sections using section headings.
    """

    text = resume_text.lower()

    section_positions = []

    # -----------------------------------------------------
    # FIND SECTION HEADINGS
    # -----------------------------------------------------

    for section_name, headings in SECTION_HEADINGS.items():

        for heading in headings:

            pattern = (
                r"(?m)^"
                + r"\s*"
                + re.escape(heading)
                + r"\s*$"
            )

            match = re.search(
                pattern,
                text
            )

            if match:

                section_positions.append(
                    (
                        match.start(),
                        section_name
                    )
                )

                break

    # -----------------------------------------------------
    # SORT BY POSITION
    # -----------------------------------------------------

    section_positions.sort(
        key=lambda item: item[0]
    )

    # -----------------------------------------------------
    # EXTRACT SECTION CONTENT
    # -----------------------------------------------------

    sections = {}

    for index, (start, section_name) in enumerate(
        section_positions
    ):

        if index + 1 < len(section_positions):

            end = section_positions[index + 1][0]

        else:

            end = len(text)

        sections[section_name] = text[start:end]

    return sections


def find_skill_evidence(resume_text, skill):
    """
    Find evidence for a skill and determine
    which resume section contains it.
    """

    text = resume_text.lower()

    keywords = SKILL_KEYWORDS.get(
        skill,
        [skill.lower()]
    )

    matched_keywords = []

    # -----------------------------------------------------
    # FIND KEYWORDS
    # -----------------------------------------------------

    for keyword in keywords:

        pattern = (
            r"\b"
            + re.escape(keyword.lower())
            + r"\b"
        )

        if re.search(pattern, text):

            matched_keywords.append(keyword)

    # -----------------------------------------------------
    # NO EVIDENCE
    # -----------------------------------------------------

    if not matched_keywords:

        return {
            "skill": skill,
            "status": "Missing",
            "confidence": "None",
            "evidence_strength": "None",
            "sections": [],
            "matched_keywords": [],
        }

    # -----------------------------------------------------
    # DETECT SECTIONS
    # -----------------------------------------------------

    sections = detect_sections(
        resume_text
    )

    matched_sections = []

    for section_name, section_text in sections.items():

        for keyword in matched_keywords:

            pattern = (
                r"\b"
                + re.escape(keyword.lower())
                + r"\b"
            )

            if re.search(
                pattern,
                section_text
            ):

                matched_sections.append(
                    section_name
                )

                break

    # -----------------------------------------------------
    # REMOVE DUPLICATES
    # -----------------------------------------------------

    matched_sections = list(
        dict.fromkeys(matched_sections)
    )

    # -----------------------------------------------------
    # DETERMINE EVIDENCE STRENGTH
    # -----------------------------------------------------

    # Evidence priority:
    # Project       → Very High
    # Experience    → Very High
    # Leadership    → High
    # Skills        → Medium
    # Objective     → Low
    # Education     → Low
    # General       → Low

    if "projects" in matched_sections:

        confidence = "Very High"
        evidence_strength = "Project"

    elif "experience" in matched_sections:

        confidence = "Very High"
        evidence_strength = "Experience"

    elif "leadership" in matched_sections:

        confidence = "High"
        evidence_strength = "Leadership"

    elif "skills" in matched_sections:

        confidence = "Medium"
        evidence_strength = "Skills Section"

    elif "objective" in matched_sections:

        confidence = "Low"
        evidence_strength = "Objective"

    elif "education" in matched_sections:

        confidence = "Low"
        evidence_strength = "Education"

    else:

        confidence = "Low"
        evidence_strength = "General Mention"

    # -----------------------------------------------------
    # RETURN RESULT
    # -----------------------------------------------------

    return {
        "skill": skill,
        "status": "Evidence Found",
        "confidence": confidence,
        "evidence_strength": evidence_strength,
        "sections": matched_sections,
        "matched_keywords": matched_keywords,
    }


def analyze_skill_evidence(resume_text, skills):
    """
    Analyze evidence for multiple skills.

    Args:
        resume_text: Full resume text.
        skills: List of skills to analyze.

    Returns:
        List of evidence dictionaries.
    """

    results = []

    for skill in skills:

        evidence = find_skill_evidence(
            resume_text,
            skill
        )

        results.append(evidence)

    return results
