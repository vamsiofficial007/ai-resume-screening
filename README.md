# AI Resume Screening System

An AI/ML-based resume screening system that evaluates how well a candidate's resume matches a specific job description.

The system goes beyond simple keyword matching by combining **skill extraction, core/preferred requirement classification, weighted matching, exact and related skill matching, resume evidence analysis, confidence scoring, skill-gap analysis, recommendations, and improvement planning**.

---

## Overview

Resume screening is often reduced to checking whether certain keywords appear in a resume.

This project takes a more structured approach.

It analyzes:

* Resume content
* Technical skills
* Job description requirements
* Core vs. preferred skills
* Exact skill matches
* Related skill matches
* Missing requirements
* Evidence supporting each resume skill
* Evidence confidence
* Candidate strengths
* Skill gaps
* Resume improvement opportunities
* Practical improvement plans
* Overall candidate assessment

The result is a structured screening report designed to make resume-to-job analysis easier to understand.

---

## Key Features

### 1. Resume Parsing

The system extracts text from supported resume formats.

Supported formats:

* PDF
* DOCX

The parser converts resume documents into text that can be analyzed by the rest of the pipeline.

---

### 2. Resume Skill Extraction

The system identifies technical skills present in the resume.

Examples include:

* Python
* SQL
* Machine Learning
* Deep Learning
* Artificial Intelligence
* Data Analysis
* Exploratory Data Analysis
* NLP
* Computer Vision
* Pandas
* NumPy
* Scikit-learn
* TensorFlow
* PyTorch
* Git
* GitHub
* FastAPI
* Streamlit

The extracted skills become the foundation for the matching and evidence-analysis stages.

---

### 3. Job Description Analysis

The job description is parsed to identify relevant technical requirements.

Requirements are classified into:

* **Core skills** — important or required qualifications
* **Preferred skills** — useful but optional qualifications

This distinction allows the system to assign different importance to different requirements.

---

### 4. Weighted Skill Matching

The system does not treat every requirement equally.

The current scoring model uses:

```text
Core Skill Weight      = 2.0
Preferred Skill Weight = 1.0
```

Matching credit:

```text
Exact Match   = 100%
Related Match = 50%
Missing       = 0%
```

The system also tracks which resume skills have already been used so that the same resume skill is not incorrectly reused to satisfy multiple job requirements.

---

### 5. Exact and Related Matching

The matcher distinguishes between:

#### Exact Match

The resume contains the same skill required by the job description.

Example:

```text
Job Skill: Python
Resume Skill: Python
Result: Exact Match
```

#### Related Match

The resume contains a skill that is considered related to the job requirement.

Example:

```text
Job Skill: Machine Learning
Resume Skill: Predictive Modeling
Result: Related Match
```

Related matches receive partial credit rather than full credit.

---

### 6. Skill Evidence Analysis

The system analyzes where each detected skill appears in the resume.

Evidence can come from sections such as:

* Objective
* Education
* Skills
* Projects
* Experience
* Certifications
* Achievements

The system also classifies the strength of the evidence.

Examples:

```text
Project
Experience
Skills Section
Objective
```

A skill demonstrated through a project or professional experience can provide stronger evidence than a skill mentioned only in an objective or skills list.

---

### 7. Evidence Confidence

Each detected skill receives a confidence level.

Possible levels include:

* Very High
* High
* Medium
* Low

Example:

```text
Python
Evidence: Project
Confidence: Very High

GitHub
Evidence: Skills Section
Confidence: Medium

Artificial Intelligence
Evidence: Objective
Confidence: Low
```

This helps distinguish between skills that are strongly demonstrated and skills that are merely mentioned.

---

### 8. Skill Gap Analysis

The system identifies job requirements that are not sufficiently matched by the resume.

Gaps are separated into:

```text
Core Gaps
Preferred Gaps
```

Core gaps receive higher priority because they represent more important job requirements.

Preferred gaps are treated as optional improvements.

---

### 9. Candidate Recommendations

The recommendation engine analyzes the screening results and produces actionable recommendations.

Recommendations can include:

* Skills that should be strengthened
* Skills that are already strong
* Related areas
* Optional skills worth developing
* Overall candidate assessment

The system is designed to avoid recommending that candidates add skills they do not genuinely possess.

---

### 10. Resume Improvement Plan

For missing skills, the system can generate a practical improvement plan.

A plan can include:

1. Learn the fundamentals
2. Practice the skill
3. Build a small project
4. Gain practical experience
5. Add the skill to the resume after gaining evidence

For example:

```text
Predictive Modeling

Priority: OPTIONAL
Gap: Missing preferred skill

Action Plan:
- Learn the fundamentals of Predictive Modeling
- Practice Predictive Modeling through a small project
- Build practical experience with Predictive Modeling
- Add Predictive Modeling to the resume after gaining experience
```

---

### 11. Recruiter-Friendly Screening Report

The reporting layer converts the complete screening-engine output into a cleaner structured report.

The report contains:

```text
Candidate
Match Score
Requirements
Skill Gaps
Strengths
Evidence Confidence
Recommendations
Improvement Plan
```

This separates the **screening logic** from the **presentation layer**, making the architecture easier to maintain and extend.

---

## System Architecture

```text
                         RESUME
                           │
                           ▼
                    Resume Parser
                           │
                           ▼
                   Skill Extraction
                           │
                           ▼
                   Evidence Analysis
                           │
                           │
                           │
                    JOB DESCRIPTION
                           │
                           ▼
                   Job Description
                       Parser
                           │
                           ▼
                 Skill Classification
                    │             │
                    ▼             ▼
                  CORE        PREFERRED
                    │             │
                    └──────┬──────┘
                           ▼
                  Weighted Matcher
                           │
                           ▼
                    Match Results
                           │
                           ▼
                  Recommendation
                       Engine
                           │
                           ▼
                  Improvement Plan
                           │
                           ▼
                   Screening Engine
                           │
                           ▼
                   Report Generator
                           │
                           ▼
                 Recruiter-Friendly
                      Report
```

---

## Project Workflow

The main screening pipeline follows this sequence:

```text
1. Read Resume
       ↓
2. Extract Resume Skills
       ↓
3. Analyze Skill Evidence
       ↓
4. Parse Job Description
       ↓
5. Classify Core / Preferred Skills
       ↓
6. Calculate Weighted Match
       ↓
7. Identify Exact / Related / Missing Skills
       ↓
8. Generate Recommendations
       ↓
9. Generate Improvement Plans
       ↓
10. Generate Screening Report
       ↓
11. Present Final Report
```

---

## Project Structure

```text
ai-resume-screening/
│
├── app/
│   ├── extraction/
│   │   ├── __init__.py
│   │   ├── contact_extractor.py
│   │   ├── skill_evidence.py
│   │   └── skills_extractor.py
│   │
│   ├── job/
│   │   ├── __init__.py
│   │   ├── job_parser.py
│   │   └── skill_classifier.py
│   │
│   ├── matching/
│   │   ├── skill_matcher.py
│   │   └── weighted_matcher.py
│   │
│   ├── parser/
│   │   ├── __init__.py
│   │   └── resume_parser.py
│   │
│   ├── recommendations/
│   │   ├── __init__.py
│   │   ├── improvement_engine.py
│   │   └── recommendation_engine.py
│   │
│   ├── screening/
│   │   ├── __init__.py
│   │   └── screening_engine.py
│   │
│   ├── improvement_plan.py
│   ├── reporting.py
│   └── main.py
│
├── data/
│   ├── job_descriptions/
│   │   └── ai_ml_intern.txt
│   │
│   ├── resumes/
│   │   └── resume.pdf
│   │
│   └── sample_job.txt
│
│
├── test_improvement_plan.py
├── test_matching.py
├── test_recommendations.py
├── test_reporting.py
├── test_skill_evidence.py
├── test_weighted_edge_cases.py
├── test_weighted_matcher.py
├── test_weighted_pipeline.py
│
├── analyze_job.py
├── analyze_resume.py
├── screen_resume.py
├── requirements.txt
├── .gitignore
└── README.md
```

> Generated files such as `venv/`, `__pycache__/`, `.pytest_cache/`, `.pyc`, `.env`, and `.DS_Store` are excluded from version control through `.gitignore`.

---

## Technologies Used

* Python 3.12
* `pypdf`
* `python-docx`
* Regular expressions
* Rule-based skill extraction
* Weighted matching algorithms
* Evidence analysis
* Modular Python architecture
* Pytest

---

## Matching Logic

The current weighted scoring model is:

```text
Core Skill Weight      = 2.0
Preferred Skill Weight = 1.0

Exact Match            = 100% credit
Related Match          = 50% credit
Missing Skill          = 0% credit
```

Conceptually:

```text
Weighted Score =
Earned Weighted Points
──────────────────────────── × 100
Total Possible Points
```

Example:

```text
Earned Points: 24.0
Total Possible: 25.0

Weighted Score:
24 / 25 × 100 = 96%
```

---

## Example Screening Result

Using the current sample resume and AI/ML internship job description, the screening pipeline produces:

```text
Skills Detected: 18

Weighted Match: 96.0%

Points:
24.0 / 25.0

Core Requirements:
11 / 11 matched

Preferred Requirements:
2 / 3 matched

Missing Skill:
Predictive Modeling
```

The result also identifies strong areas and supporting evidence.

Example:

```text
STRONG AREAS

Python
SQL
Machine Learning
Exploratory Data Analysis
NLP
Pandas
Scikit-learn
Git
```

Example evidence:

```text
Python
Evidence: Project
Confidence: Very High

SQL
Evidence: Experience
Confidence: Very High

Machine Learning
Evidence: Experience
Confidence: Very High

Deep Learning
Evidence: Skills Section
Confidence: Medium
```

The system identifies `Predictive Modeling` as a preferred-skill gap and produces an optional improvement plan.

---

## Running the Project

### 1. Create a virtual environment

```bash
python3 -m venv venv
```

### 2. Activate the environment

macOS/Linux:

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the screening system

```bash
python -m app.main
```

The system will analyze the configured resume and job description and display the final screening report.

---

## Running Tests

The project uses `pytest`.

Run the complete test suite:

```bash
pytest
```

The current test suite contains:

```text
18 tests
```

A successful run should report:

```text
18 passed
```

The tests cover areas including:

* Skill matching
* Weighted matching
* Edge cases
* Skill evidence
* Recommendations
* Improvement planning
* Screening report generation

---

## Design Philosophy

The project follows a simple principle:

> A resume should not be evaluated only by whether a keyword appears. The importance of the skill and the evidence supporting it should also matter.

This led to the combination of:

```text
Skill Matching
       +
Skill Importance
       +
Resume Evidence
       +
Confidence
       +
Skill Gaps
       +
Recommendations
       +
Improvement Planning
```

This makes the system more informative than a basic keyword counter.

---

## Engineering Principles

The project is designed around modular components.

Each major responsibility is separated:

```text
Parsing
Extraction
Classification
Matching
Evidence
Recommendations
Improvement Planning
Reporting
Presentation
```

This makes individual components easier to test, modify, and extend.

The screening engine acts as the central orchestration layer, while the reporting module converts its output into a structured recruiter-friendly format.

---

## Current Project Status

The current implementation includes:

* Resume parsing
* PDF/DOCX support
* Technical skill extraction
* Job description parsing
* Core/preferred classification
* Weighted matching
* Exact matching
* Related matching
* Missing-skill detection
* Duplicate resume-skill prevention
* Skill evidence analysis
* Confidence classification
* Recommendation engine
* Improvement suggestions
* Improvement plans
* Screening engine
* Structured reporting
* Recruiter-friendly terminal presentation
* Automated test coverage

Current validation:

```text
18 tests passed
```

---

## Future Improvements

Potential future extensions include:

* Semantic skill matching using embeddings
* Machine-learning-based resume classification
* LLM-powered resume feedback
* Web interface
* Streamlit dashboard
* Resume ranking across multiple candidates
* Job recommendation based on candidate skills
* Vector database integration
* REST API deployment
* Cloud deployment
* Multi-resume batch screening
* Candidate comparison
* Exportable screening reports
* Recruiter dashboard

---

## Disclaimer

This project is intended as an educational and portfolio project.

Its recommendations are designed as decision-support information and should not be treated as an automated hiring decision.

---

## Author

**Dola Vamsi**

AI/ML Student | Data Analysis | Predictive Modeling

GitHub: Add your GitHub profile link

