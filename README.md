# AI Resume Screening System

An AI/ML-based resume screening system that analyzes a candidate's resume against a job description and produces a weighted match score, skill-gap analysis, evidence-based recommendations, and a practical resume improvement plan.

## Overview

Traditional resume screening often relies heavily on keyword matching. This project goes further by considering:

* Resume skill extraction
* Job description skill extraction
* Core vs. preferred skill classification
* Weighted skill matching
* Exact and related skill matching
* Resume evidence analysis
* Evidence confidence levels
* Skill-gap analysis
* Resume improvement suggestions
* Personalized improvement plans
* Overall candidate assessment

The goal is to provide a more meaningful view of how well a resume aligns with a specific job description.

## Key Features

### 1. Resume Parsing

The system extracts text from PDF and DOCX resumes.

Supported formats:

* PDF
* DOCX

### 2. Resume Skill Extraction

The system identifies technical skills present in the resume, including skills such as:

* Python
* Machine Learning
* Artificial Intelligence
* Data Analysis
* Exploratory Data Analysis
* Predictive Modeling
* GitHub

### 3. Job Description Analysis

The job description is analyzed to identify required skills.

Skills are classified into:

* Core skills
* Preferred skills

This allows the system to distinguish essential requirements from optional qualifications.

### 4. Weighted Skill Matching

Not all job requirements have the same importance.

Core skills receive a higher weight than preferred skills.

The system also distinguishes between:

* Exact matches
* Related matches
* Missing skills

This produces a weighted compatibility score instead of a simple keyword percentage.

### 5. Skill Evidence Analysis

The system examines where a skill appears in the resume.

Evidence can come from sections such as:

* Objective
* Education
* Skills
* Projects

Each detected skill receives a confidence level such as:

* Very High
* High
* Medium
* Low

For example, a skill demonstrated through a relevant project can receive stronger evidence than a skill mentioned only in the objective.

### 6. Skill Gap Analysis

The system identifies skills required by the job that are missing from the resume.

Missing skills are separated into:

* High-priority core skills
* Optional preferred skills

### 7. Resume Recommendations

The system generates actionable suggestions for improving the resume.

Recommendations can include:

* Adding missing skills when the candidate genuinely has the experience
* Demonstrating skills through relevant projects
* Strengthening weak evidence
* Highlighting practical experience

### 8. Resume Improvement Plan

For missing skills, the system can generate a structured improvement plan containing:

* What to learn
* What to practice
* Suggested project direction
* When the skill should be added to the resume

## System Workflow

```text
                 RESUME PDF / DOCX
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
                         ▼
                  ┌──────────────┐
                  │              │
                  │ Job          │
                  │ Description  │
                  │              │
                  └──────┬───────┘
                         │
                         ▼
                 Job Skill Parser
                         │
                         ▼
                Skill Classification
                  │               │
                  ▼               ▼
                CORE          PREFERRED
                  │               │
                  └───────┬───────┘
                          ▼
                  Weighted Matching
                          │
                          ▼
                  Match Score
                          │
                          ▼
                  Skill Gap Analysis
                          │
                          ▼
             Evidence-Based Recommendations
                          │
                          ▼
                Improvement Plan
                          │
                          ▼
                  Final Assessment
```

## Project Structure

```text
ai-resume-screening/
│
├── app/
│   ├── extraction/
│   │   ├── contact_extractor.py
│   │   ├── skill_evidence.py
│   │   └── skills_extractor.py
│   │
│   ├── job/
│   │   ├── job_parser.py
│   │   └── skill_classifier.py
│   │
│   ├── matching/
│   │   ├── skill_matcher.py
│   │   └── weighted_matcher.py
│   │
│   ├── parser/
│   │   └── resume_parser.py
│   │
│   ├── recommendations/
│   │   ├── improvement_engine.py
│   │   └── recommendation_engine.py
│   │
│   ├── improvement_plan.py
│   └── main.py
│
├── data/
│   ├── job_descriptions/
│   │   └── ai_ml_intern.txt
│   │
│   └── resumes/
│       └── sample_resume.pdf
│
├── test_improvement_plan.py
├── test_matching.py
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

## Technologies Used

* Python
* PDF text extraction with `pypdf`
* DOCX parsing with `python-docx`
* Regular expressions
* Rule-based skill extraction
* Weighted matching algorithms
* Evidence-based scoring
* Modular Python architecture

## Matching Logic

The system gives greater importance to core job requirements.

Conceptually:

```text
Core Skill Weight      = 2.0
Preferred Skill Weight = 1.0

Exact Match            = 100% credit
Related Match          = 50% credit
Missing Skill          = 0% credit
```

The system also prevents the same resume skill from being incorrectly reused to satisfy multiple job requirements when calculating the final weighted match.

## Example Result

For a sample AI/ML internship job description, the system can produce an output such as:

```text
Weighted Score: 48.0%

Strong Areas:
  - Data Analysis
  - Exploratory Data Analysis

Priority Skills:
  - SQL
  - NLP
  - Pandas
  - NumPy
  - Scikit-learn
  - Git

Optional Improvement:
  - Deep Learning

Overall Assessment:
Your resume demonstrates a good foundation, but several
important job requirements are currently missing.
```

The system also reports the evidence behind detected skills, for example:

```text
Data Analysis
Evidence: Project
Confidence: Very High

Exploratory Data Analysis
Evidence: Project
Confidence: Very High
```

## Installation

Clone the repository:

```bash
git clone <your-github-repository-url>
cd ai-resume-screening
```

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate it on macOS/Linux:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Project

Run the main screening pipeline:

```bash
python -m app.main
```

The system will process the configured resume and job description and display:

* Extracted resume skills
* Skill evidence
* Core and preferred job skills
* Weighted match score
* Exact matches
* Related matches
* Missing skills
* Skill-gap analysis
* Recommendations
* Improvement plan
* Overall assessment

## Testing

Run the available tests individually:

```bash
python test_matching.py
python test_weighted_matcher.py
python test_weighted_edge_cases.py
python test_weighted_pipeline.py
python test_improvement_plan.py
```

## Design Philosophy

The project was designed around a simple principle:

> A resume should not be evaluated only by whether a keyword appears. The system should also consider the importance of the skill and the evidence supporting it.

This led to the combination of:

```text
Skill Matching
      +
Skill Importance
      +
Resume Evidence
      +
Skill Gaps
      +
Actionable Recommendations
```

## Future Improvements

Potential future extensions include:

* Machine-learning-based resume classification
* Semantic skill matching using embeddings
* LLM-powered resume feedback
* Web interface
* Resume ranking across multiple candidates
* Job recommendation based on candidate skills
* Vector database integration
* REST API deployment
* Cloud deployment

## Disclaimer

This project is intended as an educational and portfolio project. Its recommendations should be treated as decision-support rather than as an automated hiring decision.

## Author

**Dola Vamsi**

AI/ML Student | Data Analysis | Predictive Modeling

GitHub: Add your GitHub profile link h
