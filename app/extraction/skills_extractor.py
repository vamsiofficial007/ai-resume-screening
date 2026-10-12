import re


SKILLS_DATABASE = {
    "Python": [
        "python",
    ],
    "SQL": [
        "sql",
    ],
    "Machine Learning": [
        "machine learning",
        "machine-learning",
    ],
    "Deep Learning": [
        "deep learning",
        "deep-learning",
    ],
    "Artificial Intelligence": [
        "artificial intelligence",
        "ai/ml",
        "ai ml",
    ],
    "Data Analysis": [
        "data analysis",
        "data analytics",
    ],
    "Exploratory Data Analysis": [
        "exploratory data analysis",
        "eda",
    ],
    "Predictive Modeling": [
        "predictive modeling",
        "predictive modelling",
    ],
    "NLP": [
        "natural language processing",
        "nlp",
    ],
    "Computer Vision": [
        "computer vision",
    ],
    "Pandas": [
        "pandas",
    ],
    "NumPy": [
        "numpy",
    ],
    "Scikit-learn": [
        "scikit-learn",
        "sklearn",
    ],
    "TensorFlow": [
        "tensorflow",
    ],
    "PyTorch": [
        "pytorch",
    ],
    "Flutter": [
        "flutter",
    ],
    "Dart": [
        "dart",
    ],
    "Git": [
        "git",
    ],
    "GitHub": [
        "github",
    ],

    "Mobile App Development": [
        "mobile app development",
        "mobile application development",
    ],
    "Firebase": [
        "firebase",
    ],

    "UI Design": [
        "ui design",
        "user interface design",
        "ui development",
        "user interface development",
    ],

    "Responsive Design": [
        "responsive design",
    ],

    "API Integration": [
        "api integration",
    ],
    "REST API": [
        "rest api",
        "restful api",
    ],
    "REST API Integration": [
        "rest api integration",
        "restful api integration",
    ],
    "Debugging": [
        "debugging",
        "debug",
    ],

    "Android Development": [
        "android development",
        "android app development",
    ],
    "iOS Development": [
        "ios development",
        "ios app development",
    ],
    "State Management": [
        "state management",
    ],

    "FastAPI": [
        "fastapi",
    ],
    "Streamlit": [
        "streamlit",
    ],
    "LangChain": [
        "langchain",
    ],
    "LangGraph": [
        "langgraph",
    ],
    "RAG": [
        "rag",
        "retrieval augmented generation",
    ],
    "Vector Database": [
        "vector database",
        "vector databases",
    ],

    "HTML": [
        "html",
    ],
    "CSS": [
        "css",
    ],
    "JavaScript": [
        "javascript",
    ],
    "React": [
        "react",
    ],
    "Frontend Development": [
        "frontend development",
        "front-end development",
    ],
    "Backend Development": [
        "backend development",
        "back-end development",
    ],
    "Node.js": [
        "node.js",
        "node js",
    ],
    "Express.js": [
        "express.js",
        "express js",
    ],
    "MongoDB": [
        "mongodb",
        "mongo db",
    ],
    "TypeScript": [
        "typescript",
    ],
    "Docker": [
        "docker",
    ],
    "Problem Solving": [
        "problem solving",
        "problem-solving",
    ],
}


def extract_skills(text: str) -> list[str]:
    """
    Extract known technical skills from resume text.
    """

    text_lower = text.lower()

    detected_skills = []

    for skill_name, keywords in SKILLS_DATABASE.items():

        for keyword in keywords:

            pattern = r"\b" + re.escape(keyword) + r"\b"

            if re.search(pattern, text_lower):
                detected_skills.append(skill_name)
                break

    return detected_skills