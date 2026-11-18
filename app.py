import streamlit as st
import joblib
import re
import html
import pandas as pd
import io

from pathlib import Path
from sklearn.metrics.pairwise import cosine_similarity

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Paragraph,
    Spacer,
    KeepTogether
)


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Intelligent Resume Screening System",
    page_icon="📄",
    layout="wide"
)

st.markdown(
    """
    <style>
    :root {
        --page: #0b1120;
        --surface: #111b2e;
        --surface-raised: #17243a;
        --border: #263650;
        --text: #e8eef8;
        --muted: #9aa9bf;
        --accent: #6ea8fe;
        --accent-strong: #4387f5;
    }

    .stApp {
        color: var(--text);
        background:
            radial-gradient(ellipse at 50% -18%, rgba(52, 105, 190, 0.22), transparent 46%),
            var(--page);
    }

    [data-testid="stHeader"] {
        background: rgba(11, 17, 32, 0.78);
    }

    [data-testid="stMain"] {
        background: transparent;
    }

    .block-container {
        max-width: 1440px;
        padding: 3rem 3rem 5rem;
    }

    h1, h2, h3 {
        color: var(--text) !important;
        letter-spacing: -0.025em;
    }

    h1 {
        font-size: clamp(2rem, 3.5vw, 2.8rem) !important;
        font-weight: 750 !important;
        padding-bottom: 0.35rem;
    }

    h2 {
        margin-top: 1.25rem !important;
        font-size: 1.55rem !important;
        font-weight: 680 !important;
    }

    h3 {
        font-size: 1.15rem !important;
        font-weight: 650 !important;
    }

    p, label, [data-testid="stMarkdownContainer"] {
        color: var(--text);
    }

    .stCaption, [data-testid="stCaptionContainer"] {
        color: var(--muted) !important;
    }

    .hero-shell {
        display: flex;
        align-items: center;
        gap: 1.25rem;
        margin: 0.5rem 0 2.25rem;
        padding: 1.75rem;
        border: 1px solid #2a3d5b;
        border-radius: 1.2rem;
        background:
            radial-gradient(ellipse at 90% 0%, rgba(68, 125, 219, 0.2), transparent 42%),
            linear-gradient(135deg, #14223a, #10192b 72%);
        box-shadow: 0 14px 36px rgba(0, 0, 0, 0.18);
    }

    .hero-icon {
        display: grid;
        flex: 0 0 3.6rem;
        width: 3.6rem;
        height: 3.6rem;
        place-items: center;
        border: 1px solid rgba(133, 177, 255, 0.26);
        border-radius: 1.1rem;
        background: rgba(86, 142, 235, 0.15);
        font-size: 1.8rem;
    }

    .hero-kicker, .role-eyebrow {
        color: #8db7ff;
        font-size: 0.72rem;
        font-weight: 750;
        letter-spacing: 0.12em;
        text-transform: uppercase;
    }

    .hero-title {
        margin: 0.2rem 0 0.3rem;
        color: #f3f7ff;
        font-size: clamp(1.65rem, 3vw, 2.3rem);
        font-weight: 760;
        letter-spacing: -0.035em;
        line-height: 1.2;
    }

    .hero-description {
        margin: 0;
        color: #aab9cf;
        font-size: 0.98rem;
    }

    .role-overview, .facts-grid {
        display: grid;
        grid-template-columns: repeat(2, minmax(0, 1fr));
        gap: 1rem;
    }

    .role-card, .detail-card, .fact-card {
        border: 1px solid var(--border);
        border-radius: 0.95rem;
        background: linear-gradient(145deg, var(--surface-raised), var(--surface));
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
    }

    .role-card {
        min-height: 7rem;
        padding: 1.2rem 1.35rem;
    }

    .role-value {
        margin-top: 0.55rem;
        color: #f3f7ff;
        font-size: 1.35rem;
        font-weight: 700;
    }

    .confidence-row {
        display: flex;
        align-items: baseline;
        justify-content: space-between;
        gap: 1rem;
        margin: 0.35rem 0 0.7rem;
        color: #f3f7ff;
        font-size: 1.25rem;
        font-weight: 700;
    }

    .confidence-track {
        height: 0.42rem;
        overflow: hidden;
        border-radius: 999px;
        background: #25344d;
    }

    .confidence-fill {
        height: 100%;
        border-radius: inherit;
        background: linear-gradient(90deg, #4387f5, #72c6ff);
    }

    .detail-grid {
        display: grid;
        grid-template-columns: repeat(2, minmax(0, 1fr));
        gap: 1rem;
        margin: 0.3rem 0 1.4rem;
    }

    .detail-card {
        min-height: 9rem;
        padding: 1.15rem 1.25rem;
    }

    .detail-card.suggestion {
        border-left: 3px solid #6ea8fe;
    }

    .detail-card-title {
        display: flex;
        align-items: center;
        gap: 0.55rem;
        margin-bottom: 0.95rem;
        color: #eaf1fc;
        font-size: 1rem;
        font-weight: 680;
    }

    .skill-chips {
        display: flex;
        flex-wrap: wrap;
        gap: 0.55rem;
    }

    .skill-chip {
        display: inline-flex;
        align-items: center;
        min-height: 1.8rem;
        padding: 0.3rem 0.7rem;
        border: 1px solid #344763;
        border-radius: 999px;
        background: #1b2a40;
        color: #d7e4f7;
        font-size: 0.83rem;
        line-height: 1.2;
    }

    .skill-match {
        border-color: rgba(60, 190, 145, 0.3);
        background: rgba(29, 130, 102, 0.16);
        color: #8ce0bd;
    }

    .skill-missing {
        border-color: rgba(238, 114, 139, 0.28);
        background: rgba(155, 57, 78, 0.14);
        color: #ffabb8;
    }

    .skill-suggestion {
        border-color: rgba(110, 168, 254, 0.3);
        background: rgba(63, 117, 200, 0.16);
        color: #a9cbff;
    }

    .empty-note {
        color: var(--muted);
        font-size: 0.9rem;
    }

    .fact-card {
        padding: 1.15rem 1.25rem;
    }

    .fact-card-title {
        margin-bottom: 0.8rem;
        color: #c5d5ed;
        font-size: 0.82rem;
        font-weight: 700;
        letter-spacing: 0.06em;
        text-transform: uppercase;
    }

    .fact-line {
        display: flex;
        align-items: flex-start;
        justify-content: space-between;
        gap: 1rem;
        padding: 0.5rem 0;
        border-top: 1px solid rgba(148, 166, 194, 0.12);
    }

    .fact-label {
        color: var(--muted);
        font-size: 0.88rem;
    }

    .fact-value {
        color: #e8eef8;
        font-size: 0.92rem;
        font-weight: 620;
        text-align: right;
    }

    [data-testid="stTextArea"] textarea,
    [data-testid="stTextInput"] input,
    [data-testid="stSelectbox"] [role="combobox"],
    [data-testid="stMultiSelect"] [role="combobox"] {
        color: var(--text);
        background-color: var(--surface);
        border-color: var(--border);
        border-radius: 0.7rem;
    }

    [data-testid="stTextArea"] textarea:focus,
    [data-testid="stTextInput"] input:focus {
        border-color: var(--accent);
        box-shadow: 0 0 0 1px var(--accent);
    }

    [data-testid="stFileUploader"] section {
        background: var(--surface);
        border: 1px dashed #3b5273;
        border-radius: 1rem;
        transition: border-color 160ms ease, background 160ms ease;
    }

    [data-testid="stFileUploader"] section:hover {
        background: var(--surface-raised);
        border-color: var(--accent);
    }

    [data-testid="stButton"] button,
    [data-testid="stDownloadButton"] button,
    [data-testid="stFormSubmitButton"] button {
        min-height: 2.8rem;
        border: 1px solid #3c78d8;
        border-radius: 0.7rem;
        color: #fff;
        background: linear-gradient(135deg, var(--accent-strong), #356ed0);
        font-weight: 650;
        box-shadow: 0 5px 16px rgba(34, 91, 177, 0.2);
        transition: transform 160ms ease, filter 160ms ease, box-shadow 160ms ease;
    }

    [data-testid="stButton"] button:hover,
    [data-testid="stDownloadButton"] button:hover,
    [data-testid="stFormSubmitButton"] button:hover {
        transform: translateY(-1px);
        filter: brightness(1.1);
        box-shadow: 0 8px 22px rgba(34, 91, 177, 0.3);
    }

    [data-testid="stMetric"] {
        min-height: 7rem;
        padding: 1.1rem 1.25rem;
        border: 1px solid var(--border);
        border-radius: 0.9rem;
        background: linear-gradient(145deg, var(--surface-raised), var(--surface));
    }

    [data-testid="stMetricLabel"] {
        color: var(--muted) !important;
        font-weight: 550;
    }

    [data-testid="stMetricValue"] {
        color: #f4f7fc !important;
        font-weight: 720;
    }

    [data-testid="stDataFrame"],
    [data-testid="stTable"] {
        overflow: hidden;
        border: 1px solid var(--border);
        border-radius: 0.85rem;
    }

    [data-testid="stAlert"] {
        border-radius: 0.8rem;
    }

    hr {
        border-color: var(--border);
        margin: 2rem 0;
    }

    @media (max-width: 768px) {
        .block-container {
            padding: 1.75rem 1rem 3rem;
        }

        .hero-shell {
            align-items: flex-start;
            padding: 1.25rem;
        }

        .hero-icon {
            flex-basis: 3rem;
            width: 3rem;
            height: 3rem;
        }

        .detail-grid, .role-overview, .facts-grid {
            grid-template-columns: 1fr;
        }

        .fact-line {
            flex-direction: column;
            gap: 0.2rem;
        }

        .fact-value {
            text-align: left;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# LOAD MODEL AND TF-IDF VECTORIZER
# =========================================================

BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR / "notebooks"

model_path = MODEL_DIR / "resume_role_model.pkl"
tfidf_path = MODEL_DIR / "tfidf_vectorizer.pkl"

model = joblib.load(model_path)
tfidf = joblib.load(tfidf_path)


# =========================================================
# SESSION STATE
# =========================================================

if "results" not in st.session_state:
    st.session_state.results = []

if "job_description" not in st.session_state:
    st.session_state.job_description = ""

if "uploaded_resumes" not in st.session_state:
    st.session_state.uploaded_resumes = []

if "evaluation_done" not in st.session_state:
    st.session_state.evaluation_done = False

if "actual_roles" not in st.session_state:
    st.session_state.actual_roles = {}


# =========================================================
# TEXT CLEANING
# =========================================================

def clean_text(text):

    text = text.lower()

    text = re.sub(
        r"[^a-zA-Z0-9\s]",
        " ",
        text
    )

    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()


# =========================================================
# ROLE PREDICTION
# =========================================================

def predict_role(resume):

    cleaned_resume = clean_text(resume)

    resume_vector = tfidf.transform(
        [cleaned_resume]
    )

    prediction = model.predict(
        resume_vector
    )

    return prediction[0]


# =========================================================
# ROLE PREDICTION + CONFIDENCE + ALTERNATIVES
# =========================================================

def predict_role_confidence(resume):

    cleaned_resume = clean_text(resume)

    resume_vector = tfidf.transform(
        [cleaned_resume]
    )

    prediction = model.predict(
        resume_vector
    )

    predicted_role = prediction[0]

    confidence = 0.0

    alternatives = []

    if hasattr(model, "predict_proba"):

        probabilities = model.predict_proba(
            resume_vector
        )[0]

        classes = model.classes_

        probability_data = []

        for role, probability in zip(
            classes,
            probabilities
        ):

            probability_data.append(
                (
                    role,
                    float(probability)
                )
            )

        probability_data.sort(
            key=lambda x: x[1],
            reverse=True
        )

        confidence = (
            probability_data[0][1] * 100
        )

        for role, probability in (
            probability_data[1:4]
        ):

            alternatives.append(
                {
                    "role": role,
                    "confidence": round(
                        probability * 100,
                        2
                    )
                }
            )

    else:

        confidence = 100.0

    return (
        predicted_role,
        round(confidence, 2),
        alternatives
    )


# =========================================================
# SKILLS LIST
# =========================================================

SKILLS = [
    "python", "java", "c++", "c#",
    "c",
    ".net", "asp.net", "asp.net mvc",
    ".net core", ".net 8",
    "entity framework",
    "entity framework core",
    "sql", "mysql", "mongodb",
    "postgresql", "oracle",
    "html", "css", "javascript",
    "jquery", "ajax",
    "react", "next.js",
    "node.js", "node", "express",
    "django", "flask", "fastapi",
    "spring boot",
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "tensorflow", "keras", "pytorch",
    "scikit-learn", "pandas", "numpy",
    "nlp", "tf-idf",
    "word embeddings", "glove",
    "nltk",
    "data analysis", "data science",
    "matplotlib", "seaborn",
    "cnn", "rnn", "lstm",
    "git", "github", "docker",
    "aws", "jupyter notebook",
    "vs code", "postman",
    "pl/sql", "php", "excel"
    

    # ---------------- DATABASE ----------------
    "sql",
    "mysql",
    "mongodb",
    "postgresql",
    "oracle",
    "pl/sql",

    # ---------------- WEB ----------------
    "html",
    "css",
    "javascript",
    "jquery",
    "ajax",
    "react",
    "next.js",
    "node.js",
    "node",
    "express",
    "django",
    "flask",
    "fastapi",
    "spring boot",

    # ---------------- AI / DATA ----------------
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "tensorflow",
    "keras",
    "pytorch",
    "scikit-learn",
    "pandas",
    "numpy",
    "nlp",
    "tf-idf",
    "word embeddings",
    "glove",
    "nltk",
    "data analysis",
    "data science",
    "matplotlib",
    "seaborn",
    "cnn",
    "rnn",
    "lstm",

    # ---------------- TOOLS ----------------
    "git",
    "github",
    "docker",
    "aws",
    "jupyter notebook",
    "vs code",
    "postman",
    "excel",

    # ---------------- MECHANICAL ENGINEERING ----------------
    "mechanical engineering",
    "mechanical design",
    "mechanical systems",
    "mechanical component design",
    "machine design",
    "autocad",
    "solidworks",
    "cad",
    "3d modeling",
    "manufacturing",
    "manufacturing processes",
    "production engineering",
    "production",
    "cnc",
    "thermodynamics",
    "maintenance",
    "mechanical equipment",
    "engineering drawings",
    "engineering design",

    # ---------------- MANUFACTURING / QUALITY ----------------
    "quality inspection",
    "quality control",
    "quality assurance",
    "defect identification",
    "defect analysis",
    "production documentation",
    "shopfloor operations",
    "fabrication",
    "pneumatic systems",
    "additive manufacturing",
    "3d printing",

    # ---------------- AUTOMATION / INDUSTRIAL ----------------
    "process control",
    "process automation",
    "industrial automation",
    "plc",
    "scada",
    "instrumentation",

    # ---------------- ELECTRICAL ----------------
    "electrical engineering",
    "electrical systems",
    "electrical circuits",
    "power systems",
    "power distribution",
    "power electronics",
    "circuit design",
    "circuit analysis",
    "electrical maintenance",

    # ---------------- FINANCE ----------------
    "accounting",
    "bookkeeping",
    "tally",
    "gst",
    "tds",
    "accounts payable",
    "accounts receivable",
    "financial reporting",
    "financial analysis",
    "financial modeling",
    "budgeting",
    "forecasting",
    "investment analysis",
    "valuation",

    # ---------------- HR ----------------
    "recruitment",
    "talent acquisition",
    "employee relations",
    "employee engagement",
    "payroll",
    "onboarding",
    "performance management",
    "human resources",

    # ---------------- MARKETING ----------------
    "digital marketing",
    "social media marketing",
    "seo",
    "sem",
    "content marketing",
    "email marketing",
    "google ads",
    "market research",
    "brand management",

    # ---------------- SALES ----------------
    "sales",
    "lead generation",
    "customer acquisition",
    "business development",
    "negotiation",
    "cold calling",
    "b2b sales",
    "account management",

    # ---------------- BUSINESS ANALYSIS ----------------
    "business analysis",
    "requirements gathering",
    "requirements analysis",
    "stakeholder management",
    "process improvement",
    "process mapping",
    "user stories",
    "agile",

    # ---------------- CRM ----------------
    "crm",
    "salesforce",
    "customer relationship management",
    "customer support",
    "customer retention",
    "lead management",
    "customer engagement",

    # ---------------- DIGITAL ASSOCIATE ----------------
    "data annotation",
    "data labeling",
    "image annotation",
    "audio annotation",
    "audio transcription",
    "content review",
    "content classification",
    "data validation",
    "data processing",
    "quality checking",
    "standard operating procedures",
    "sop",
    "content moderation",

    # ---------------- TESTING / QUALITY ANALYST ----------------
    "software testing",
    "manual testing",
    "automation testing",
    "test automation",
    "test cases",
    "test plans",
    "regression testing",
    "functional testing",
    "bug reporting",
    "defect tracking",
    "selenium",

    # ---------------- HEALTHCARE ----------------
    "healthcare administration",
    "hospital administration",
    "hospital operations",
    "patient coordination",
    "medical records",
    "patient services",
    "appointment scheduling",

    # ---------------- EDUCATION ----------------
    "teaching",
    "lesson planning",
    "classroom management",
    "curriculum development",
    "student assessment",
    "student mentoring",

    # ---------------- OTHER ----------------
    "php",
    "sap"

]


# =========================================================
# SKILL EXTRACTION
# =========================================================

def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in SKILLS:

        pattern = (
            r"(?<![a-zA-Z0-9])"
            + re.escape(skill.lower())
            + r"(?![a-zA-Z0-9])"
        )

        if re.search(
            pattern,
            text
        ):

            found_skills.append(skill)

    return sorted(
        list(set(found_skills))
    )


# =========================================================
# EXPERIENCE EXTRACTION
# =========================================================

def extract_experience(text):

    text = text.lower()

    patterns = [
        r"(\d+(?:\.\d+)?)\+?\s*(?:years?|yrs?)\s+(?:of\s+)?experience",
        r"experience\s*(?:of)?\s*[:\-]?\s*(\d+(?:\.\d+)?)\+?\s*(?:years?|yrs?)",
        r"experience\s*[:\-]\s*(\d+(?:\.\d+)?)\+?\s*(?:years?|yrs?)",
        r"(\d+(?:\.\d+)?)\+?\s*(?:years?|yrs?)"
    ]

    experience = 0.0

    for pattern in patterns:

        matches = re.findall(
            pattern,
            text
        )

        for match in matches:

            try:

                value = float(match)

                experience = max(
                    experience,
                    value
                )

            except:
                pass

    return experience


# =========================================================
# EDUCATION EXTRACTION
# =========================================================

def extract_education(text):

    text = text.lower()

    education_patterns = {

        "bca": [
            r"\bbca\b",
            r"\bbachelor\s+of\s+computer\s+applications?\b"
        ],

        "btech": [
            r"\bb\.?\s*tech\b",
            r"\bbtech\b",
            r"\bbachelor\s+of\s+technology\b"
        ],

        "be": [
            r"\bb\.?\s*e\.?\b",
            r"\bbachelor\s+of\s+engineering\b"
        ],

        "mca": [
            r"\bmca\b",
            r"\bmaster\s+of\s+computer\s+applications?\b"
        ],

        "mtech": [
            r"\bm\.?\s*tech\b",
            r"\bmtech\b",
            r"\bmaster\s+of\s+technology\b"
        ],

        "me": [
            r"\bm\.?\s*e\.?\b",
            r"\bmaster\s+of\s+engineering\b"
        ],

        "bsc": [
            r"\bb\.?\s*sc\.?\b",
            r"\bbsc\b",
            r"\bbachelor\s+of\s+science\b"
        ],

        "msc": [
            r"\bm\.?\s*sc\.?\b",
            r"\bmsc\b",
            r"\bmaster\s+of\s+science\b"
        ],

        "bachelor": [
            r"\bbachelor(?:'s)?\b"
        ],

        "master": [
            r"\bmaster(?:'s)?\b"
        ],

        "phd": [
            r"\bph\.?\s*d\.?\b",
            r"\bphd\b",
            r"\bdoctorate\b"
        ]
    }

    found = []

    for education, patterns in (
        education_patterns.items()
    ):

        for pattern in patterns:

            if re.search(
                pattern,
                text
            ):

                found.append(
                    education
                )

                break

    return sorted(
        list(set(found))
    )


# =========================================================
# REQUIRED EDUCATION / EXPERIENCE
# =========================================================

def extract_required_education(
    job_description
):

    return extract_education(
        job_description
    )


def extract_required_experience(
    job_description
):

    return extract_experience(
        job_description
    )


# =========================================================
# RESUME SECTION ANALYSIS
# =========================================================

def analyze_resume_sections(text):

    text_lower = text.lower()

    sections = {

        "Contact Information": bool(
            re.search(
                r"email|phone|mobile|contact",
                text_lower
            )
        ),

        "Summary / Objective": bool(
            re.search(
                r"summary|objective|profile",
                text_lower
            )
        ),

        "Education": bool(
            re.search(
                r"education|btech|bca|bachelor|master|degree|university|college",
                text_lower
            )
        ),

        "Skills": bool(
            re.search(
                r"skills|technical skills|technologies",
                text_lower
            )
        ),

        "Experience": bool(
            re.search(
                r"experience|work experience|employment",
                text_lower
            )
        ),

        "Projects": bool(
            re.search(
                r"projects|project",
                text_lower
            )
        ),

        "Certifications": bool(
            re.search(
                r"certification|certifications|certificate",
                text_lower
            )
        )
    }

    return sections


# =========================================================
# EXPERIENCE SCORE
# =========================================================

def calculate_experience_score(
    candidate_experience,
    required_experience
):

    if required_experience <= 0:

        return 100

    if candidate_experience >= required_experience:

        return 100

    if candidate_experience > 0:

        score = (
            candidate_experience
            / required_experience
        ) * 100

        return round(
            score,
            2
        )

    return 0


# =========================================================
# EDUCATION SCORE
# =========================================================

def calculate_education_score(
    candidate_education,
    required_education
):

    if not required_education:

        return 100

    matched = set(
        candidate_education
    ).intersection(
        set(required_education)
    )

    if matched:

        return 100

    return 0


# =========================================================
# TF-IDF SIMILARITY
# =========================================================

def calculate_tfidf_score(
    resume_text,
    job_description
):

    resume_cleaned = clean_text(
        resume_text
    )

    job_cleaned = clean_text(
        job_description
    )

    vectors = tfidf.transform(
        [
            resume_cleaned,
            job_cleaned
        ]
    )

    similarity = cosine_similarity(
        vectors[0],
        vectors[1]
    )[0][0]

    return round(
        similarity * 100,
        2
    )


# =========================================================
# SKILL SCORE
# =========================================================

def calculate_skill_score(
    resume_skills,
    job_skills
):

    if not job_skills:

        return 100

    matched_skills = set(
        resume_skills
    ).intersection(
        set(job_skills)
    )

    score = (
        len(matched_skills)
        / len(job_skills)
    ) * 100

    return round(
        score,
        2
    )


# =========================================================
# READ RESUME
# =========================================================

def read_resume(
    file_data,
    file_type
):

    try:

        if file_type == "application/pdf":

            from PyPDF2 import PdfReader

            pdf_file = io.BytesIO(
                file_data
            )

            reader = PdfReader(
                pdf_file
            )

            text = ""

            for page in reader.pages:

                page_text = page.extract_text()

                if page_text:

                    text += (
                        page_text
                        + "\n"
                    )

            return text

        elif file_type == (
            "application/vnd.openxmlformats-officedocument."
            "wordprocessingml.document"
        ):

            from docx import Document

            doc_file = io.BytesIO(
                file_data
            )

            document = Document(
                doc_file
            )

            text = "\n".join(
                paragraph.text
                for paragraph in document.paragraphs
            )

            return text

        else:

            return file_data.decode(
                "utf-8",
                errors="ignore"
            )

    except Exception:

        return ""


# =========================================================
# SCORE EXPLANATION
# =========================================================

def create_score_explanation(result):

    matched_count = len(
        result["matched_skills"]
    )

    required_skill_count = len(
        result["job_skills"]
    )

    candidate_exp = (
        result["candidate_experience"]
    )

    required_exp = (
        result["required_experience"]
    )

    candidate_education = (
        result["candidate_education"]
    )

    required_education = (
        result["required_education"]
    )


    # Skill explanation

    if required_skill_count > 0:

        skill_explanation = (
            f"Skills: {matched_count} of "
            f"{required_skill_count} required skills matched."
        )

    else:

        skill_explanation = (
            "Skills: No specific skills were "
            "detected from the job description."
        )


    # Experience explanation

    if required_exp > 0:

        if candidate_exp >= required_exp:

            experience_explanation = (
                f"Experience: {candidate_exp} years "
                f"meets the required {required_exp} years."
            )

        else:

            experience_explanation = (
                f"Experience: {candidate_exp} years "
                f"against the required {required_exp} years."
            )

    else:

        experience_explanation = (
            "Experience: No specific experience "
            "requirement was detected."
        )


    # Education explanation

    if required_education:

        education_match = set(
            candidate_education
        ).intersection(
            set(required_education)
        )

        if education_match:

            education_explanation = (
                "Education: Candidate has an "
                "education qualification matching "
                "the job requirement."
            )

        else:

            education_explanation = (
                "Education: Candidate's detected "
                "education does not match the "
                "job requirement."
            )

    else:

        education_explanation = (
            "Education: No specific education "
            "requirement was detected."
        )


    # TF-IDF explanation

    tfidf_explanation = (
        f'TF-IDF: {result["tfidf_score"]}% '
        f'similarity between the resume and '
        f'job description.'
    )


    # Overall explanation

    overall_explanation = (
        f'Overall Score: {result["final_score"]}%. '
        f'The score combines TF-IDF similarity '
        f'(50%), skill matching (30%), experience '
        f'(10%), and education (10%).'
    )


    return [
        skill_explanation,
        experience_explanation,
        education_explanation,
        tfidf_explanation,
        overall_explanation
    ]


# =========================================================
# CREATE PDF REPORT
# =========================================================

def create_pdf_report(results):

    pdf_buffer = io.BytesIO()

    document = SimpleDocTemplate(
        pdf_buffer,
        pagesize=landscape(A4),
        rightMargin=25,
        leftMargin=25,
        topMargin=22,
        bottomMargin=22
    )

    styles = getSampleStyleSheet()


    # -----------------------------------------------------
    # PDF STYLES
    # -----------------------------------------------------

    title_style = ParagraphStyle(
        "PDFTitle",
        parent=styles["Title"],
        fontSize=17,
        leading=20,
        spaceAfter=8
    )

    heading_style = ParagraphStyle(
        "PDFHeading",
        parent=styles["Heading2"],
        fontSize=11,
        leading=13,
        spaceBefore=5,
        spaceAfter=4
    )

    candidate_heading_style = ParagraphStyle(
        "CandidateHeading",
        parent=styles["Heading2"],
        fontSize=10,
        leading=12,
        spaceBefore=4,
        spaceAfter=3
    )

    normal_style = ParagraphStyle(
        "PDFNormal",
        parent=styles["BodyText"],
        fontSize=8,
        leading=10,
        alignment=TA_LEFT,
        spaceAfter=2
    )

    bullet_style = ParagraphStyle(
        "PDFBullet",
        parent=styles["BodyText"],
        fontSize=7.7,
        leading=9.5,
        leftIndent=8,
        firstLineIndent=-6,
        spaceAfter=1
    )

    small_style = ParagraphStyle(
        "PDFSmall",
        parent=styles["BodyText"],
        fontSize=7.2,
        leading=8.5
    )


    story = []


    # =====================================================
    # REPORT TITLE
    # =====================================================

    story.append(
        Paragraph(
            "Intelligent Resume Screening Report",
            title_style
        )
    )

    story.append(
        Paragraph(
            f"Total Candidates Screened: {len(results)}",
            normal_style
        )
    )

    story.append(
        Spacer(1, 7)
    )


    # =====================================================
    # SUMMARY TABLE
    # =====================================================

    table_data = [

        [
            Paragraph(
                "<b>Rank</b>",
                small_style
            ),

            Paragraph(
                "<b>Resume</b>",
                small_style
            ),

            Paragraph(
                "<b>Match Score</b>",
                small_style
            ),

            Paragraph(
                "<b>Skill Match</b>",
                small_style
            ),

            Paragraph(
                "<b>Experience</b>",
                small_style
            ),

            Paragraph(
                "<b>Education</b>",
                small_style
            ),

            Paragraph(
                "<b>Recommendation</b>",
                small_style
            )
        ]
    ]


    for index, result in enumerate(
        results,
        start=1
    ):

        recommendation = result[
            "recommendation"
        ]


        if "Strong Candidate" in recommendation:

            recommendation_text = (
                "Strong Candidate"
            )

        elif "Moderate Candidate" in recommendation:

            recommendation_text = (
                "Moderate Candidate"
            )

        else:

            recommendation_text = (
                "Needs Improvement"
            )


        table_data.append(
            [

                Paragraph(
                    str(index),
                    small_style
                ),

                Paragraph(
                    result["resume_name"],
                    small_style
                ),

                Paragraph(
                    f'{result["final_score"]}%',
                    small_style
                ),

                Paragraph(
                    f'{result["skill_score"]}%',
                    small_style
                ),

                Paragraph(
                    f'{result["experience_score"]}%',
                    small_style
                ),

                Paragraph(
                    f'{result["education_score"]}%',
                    small_style
                ),

                Paragraph(
                    recommendation_text,
                    small_style
                )
            ]
        )


    summary_table = Table(
        table_data,
        colWidths=[
            35,
            150,
            70,
            70,
            70,
            70,
            110
        ],
        repeatRows=1
    )


    # =====================================================
    # LIGHT COLUMN HEADER
    # =====================================================

    summary_table.setStyle(
        TableStyle(
            [

                # Light header background
                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, 0),
                    colors.HexColor(
                        "#D9EAF7"
                    )
                ),

                # Dark text for header
                (
                    "TEXTCOLOR",
                    (0, 0),
                    (-1, 0),
                    colors.HexColor(
                        "#1F2937"
                    )
                ),

                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    0.4,
                    colors.HexColor(
                        "#B8C4CE"
                    )
                ),

                (
                    "VALIGN",
                    (0, 0),
                    (-1, -1),
                    "MIDDLE"
                ),

                (
                    "ALIGN",
                    (0, 0),
                    (0, -1),
                    "CENTER"
                ),

                (
                    "ALIGN",
                    (2, 1),
                    (5, -1),
                    "CENTER"
                ),

                (
                    "ROWBACKGROUNDS",
                    (0, 1),
                    (-1, -1),
                    [
                        colors.white,
                        colors.HexColor(
                            "#F7FAFC"
                        )
                    ]
                ),

                (
                    "TOPPADDING",
                    (0, 0),
                    (-1, -1),
                    4
                ),

                (
                    "BOTTOMPADDING",
                    (0, 0),
                    (-1, -1),
                    4
                ),

                (
                    "LEFTPADDING",
                    (0, 0),
                    (-1, -1),
                    5
                ),

                (
                    "RIGHTPADDING",
                    (0, 0),
                    (-1, -1),
                    5
                )
            ]
        )
    )


    story.append(
        summary_table
    )

    story.append(
        Spacer(1, 8)
    )


    # =====================================================
    # CANDIDATE DETAILS
    # =====================================================

    story.append(
        Paragraph(
            "Candidate Details",
            heading_style
        )
    )


    for index, result in enumerate(
        results,
        start=1
    ):

        candidate_content = []


        # -------------------------------------------------
        # Candidate heading
        # -------------------------------------------------

        candidate_content.append(
            Paragraph(
                f'{index}. {result["resume_name"]}',
                candidate_heading_style
            )
        )


        # -------------------------------------------------
        # Why score heading
        # -------------------------------------------------

        candidate_content.append(
            Paragraph(
                "<b>Why This Candidate Received This Score</b>",
                normal_style
            )
        )


        # -------------------------------------------------
        # Individual explanation points
        # -------------------------------------------------

        explanations = result[
            "score_explanation"
        ]

        for explanation in explanations:

            candidate_content.append(
                Paragraph(
                    f"• {explanation}",
                    bullet_style
                )
            )


        # -------------------------------------------------
        # Missing skills
        # -------------------------------------------------

        candidate_content.append(
            Spacer(1, 2)
        )

        candidate_content.append(
            Paragraph(
                "<b>Missing Skills:</b>",
                normal_style
            )
        )


        if result["missing_skills"]:

            missing_skills_text = ", ".join(
                result["missing_skills"]
            )

        else:

            missing_skills_text = (
                "No missing skills"
            )


        candidate_content.append(
            Paragraph(
                missing_skills_text,
                normal_style
            )
        )


        # -------------------------------------------------
        # Actual role
        # -------------------------------------------------

        if (
            st.session_state.evaluation_done
            and result["resume_name"]
            in st.session_state.actual_roles
        ):

            actual_role = (
                st.session_state.actual_roles[
                    result["resume_name"]
                ]
            )

        else:

            actual_role = (
                "Not Evaluated"
            )


        candidate_content.append(
            Paragraph(
                f"<b>Actual Role:</b> {actual_role}",
                normal_style
            )
        )


        # -------------------------------------------------
        # Predicted role
        # -------------------------------------------------

        candidate_content.append(
            Paragraph(
                f'<b>Predicted Role:</b> '
                f'{result["predicted_role"]}',
                normal_style
            )
        )


        # -------------------------------------------------
        # Separator
        # -------------------------------------------------

        candidate_content.append(
            Spacer(1, 3)
        )

        candidate_content.append(
            Paragraph(
                "____________________________________________________________",
                small_style
            )
        )


        # -------------------------------------------------
        # Keep candidate details together
        # -------------------------------------------------

        story.append(
            KeepTogether(
                candidate_content
            )
        )

        story.append(
            Spacer(1, 4)
        )


    # =====================================================
    # BUILD PDF
    # =====================================================

    document.build(
        story
    )

    pdf_buffer.seek(0)

    return pdf_buffer.getvalue()


def render_skill_panel(title, skills, empty_message, chip_class):

    safe_title = html.escape(title)
    panel_modifier = (
        " suggestion"
        if chip_class == "skill-suggestion"
        else ""
    )

    if skills:

        skill_chips = "".join(
            f'<span class="skill-chip {chip_class}">'
            f'{html.escape(str(skill))}</span>'
            for skill in skills
        )

        panel_content = (
            f'<div class="skill-chips">{skill_chips}</div>'
        )

    else:

        panel_content = (
            f'<div class="empty-note">'
            f'{html.escape(empty_message)}</div>'
        )

    st.markdown(
        f"""
        <section class="detail-card{panel_modifier}">
            <div class="detail-card-title">{safe_title}</div>
            {panel_content}
        </section>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# APPLICATION TITLE
# =========================================================

st.markdown(
    """
    <header class="hero-shell">
        <div class="hero-icon">📄</div>
        <div>
            <div class="hero-kicker">Talent intelligence workspace</div>
            <div class="hero-title">Intelligent Resume Screening</div>
            <p class="hero-description">
                Compare resumes, surface relevant skills, and make candidate reviews easier.
            </p>
        </div>
    </header>
    """,
    unsafe_allow_html=True
)


# =========================================================
# JOB DESCRIPTION
# =========================================================

st.header(
    "💼 Job Description"
)

job_description = st.text_area(
    "Paste the job description here",
    value=st.session_state.job_description,
    height=220
)

st.session_state.job_description = (
    job_description
)


# =========================================================
# RESUME UPLOAD
# =========================================================

st.header(
    "📂 Upload Resumes"
)

uploaded_files = st.file_uploader(
    "Upload one or more resumes",
    type=[
        "pdf",
        "docx",
        "txt"
    ],
    accept_multiple_files=True
)


# =========================================================
# STORE UPLOADED RESUMES
# =========================================================

if uploaded_files:

    st.session_state.uploaded_resumes = []

    for uploaded_file in uploaded_files:

        st.session_state.uploaded_resumes.append(
            {
                "name": uploaded_file.name,
                "type": uploaded_file.type,
                "data": uploaded_file.getvalue()
            }
        )


if st.session_state.uploaded_resumes:

    st.success(
        f"{len(st.session_state.uploaded_resumes)} "
        f"resume(s) ready for screening."
    )


# =========================================================
# SCREEN BUTTON
# =========================================================

screen_button = st.button(
    "🔍 Screen Resumes",
    type="primary",
    use_container_width=True
)


# =========================================================
# SCREEN RESUMES
# =========================================================

if screen_button:

    if not job_description.strip():

        st.error(
            "Please enter a job description."
        )

    elif not st.session_state.uploaded_resumes:

        st.error(
            "Please upload at least one resume."
        )

    else:

        with st.spinner(
            "Analyzing resumes..."
        ):

            results = []

            job_skills = extract_skills(
                job_description
            )

            required_education = (
                extract_required_education(
                    job_description
                )
            )

            required_experience = (
                extract_required_experience(
                    job_description
                )
            )


            for resume in (
                st.session_state.uploaded_resumes
            ):

                resume_text = read_resume(
                    resume["data"],
                    resume["type"]
                )

                if not resume_text.strip():

                    continue


                # -----------------------------------------
                # ROLE PREDICTION
                # -----------------------------------------

                (
                    predicted_role,
                    confidence,
                    alternatives
                ) = predict_role_confidence(
                    resume_text
                )


                # -----------------------------------------
                # SKILLS
                # -----------------------------------------

                resume_skills = extract_skills(
                    resume_text
                )

                matched_skills = sorted(
                    list(
                        set(resume_skills)
                        .intersection(
                            set(job_skills)
                        )
                    )
                )

                missing_skills = sorted(
                    list(
                        set(job_skills)
                        - set(resume_skills)
                    )
                )


                # -----------------------------------------
                # SCORES
                # -----------------------------------------

                tfidf_score = (
                    calculate_tfidf_score(
                        resume_text,
                        job_description
                    )
                )

                skill_score = (
                    calculate_skill_score(
                        resume_skills,
                        job_skills
                    )
                )

                candidate_experience = (
                    extract_experience(
                        resume_text
                    )
                )

                experience_score = (
                    calculate_experience_score(
                        candidate_experience,
                        required_experience
                    )
                )

                candidate_education = (
                    extract_education(
                        resume_text
                    )
                )

                education_score = (
                    calculate_education_score(
                        candidate_education,
                        required_education
                    )
                )


                # -----------------------------------------
                # FINAL SCORE
                # -----------------------------------------

                final_score = (

                    (tfidf_score * 0.50)

                    + (skill_score * 0.30)

                    + (experience_score * 0.10)

                    + (education_score * 0.10)
                )

                final_score = round(
                    final_score,
                    2
                )


                # -----------------------------------------
                # RECOMMENDATION
                # -----------------------------------------

                if final_score >= 75:

                    recommendation = (
                        "⭐ Strong Candidate"
                    )

                elif final_score >= 50:

                    recommendation = (
                        "👍 Moderate Candidate"
                    )

                else:

                    recommendation = (
                        "⚠️ Needs Improvement"
                    )


                # -----------------------------------------
                # RESUME QUALITY
                # -----------------------------------------

                sections = (
                    analyze_resume_sections(
                        resume_text
                    )
                )

                sections_present = sum(
                    sections.values()
                )

                total_sections = len(
                    sections
                )

                resume_quality = round(
                    (
                        sections_present
                        / total_sections
                    ) * 100,
                    2
                )


                # -----------------------------------------
                # IMPROVEMENT SUGGESTIONS
                # -----------------------------------------

                improvement_suggestions = (
                    missing_skills.copy()
                )


                # -----------------------------------------
                # STORE RESULT
                # -----------------------------------------

                result = {

                    "resume_name":
                        resume["name"],

                    "predicted_role":
                        predicted_role,

                    "confidence":
                        confidence,

                    "alternatives":
                        alternatives,

                    "resume_skills":
                        resume_skills,

                    "job_skills":
                        job_skills,

                    "matched_skills":
                        matched_skills,

                    "missing_skills":
                        missing_skills,

                    "tfidf_score":
                        tfidf_score,

                    "skill_score":
                        skill_score,

                    "candidate_experience":
                        candidate_experience,

                    "required_experience":
                        required_experience,

                    "experience_score":
                        experience_score,

                    "candidate_education":
                        candidate_education,

                    "required_education":
                        required_education,

                    "education_score":
                        education_score,

                    "final_score":
                        final_score,

                    "sections":
                        sections,

                    "resume_quality":
                        resume_quality,

                    "improvement_suggestions":
                        improvement_suggestions,

                    "recommendation":
                        recommendation
                }


                # -----------------------------------------
                # SCORE EXPLANATION
                # -----------------------------------------

                result[
                    "score_explanation"
                ] = create_score_explanation(
                    result
                )


                results.append(
                    result
                )


            # -----------------------------------------
            # SORT RESULTS
            # -----------------------------------------

            results.sort(
                key=lambda x: x["final_score"],
                reverse=True
            )

            st.session_state.results = (
                results
            )

            st.session_state.evaluation_done = (
                False
            )

            st.session_state.actual_roles = {}


        st.success(
            f"Successfully screened "
            f"{len(results)} resume(s)."
        )


# =========================================================
# RESULTS
# =========================================================

results = st.session_state.results


if results:

    # =====================================================
    # CANDIDATE RANKING
    # =====================================================

    st.divider()

    st.header(
        "🏆 Candidate Ranking"
    )

    ranking_rows = []

    for index, result in enumerate(
        results,
        start=1
    ):

        ranking_rows.append(
            {
                "Rank":
                    index,

                "Resume":
                    result["resume_name"],

                "Predicted Role":
                    result["predicted_role"],

                "Match Score":
                    f'{result["final_score"]}%',

                "Skill Match":
                    f'{result["skill_score"]}%',

                "Experience":
                    f'{result["experience_score"]}%',

                "Education":
                    f'{result["education_score"]}%'
            }
        )

    ranking_df = pd.DataFrame(
        ranking_rows
    )

    st.dataframe(
        ranking_df,
        use_container_width=True,
        hide_index=True
    )


    # =====================================================
    # EXPORT SCREENING RESULTS
    # =====================================================

    st.subheader(
        "📥 Export Screening Results"
    )

    pdf_data = create_pdf_report(
        results
    )

    st.download_button(
        label="📥 Download Screening Report (PDF)",
        data=pdf_data,
        file_name="candidate_screening_report.pdf",
        mime="application/pdf",
        use_container_width=True
    )


    # =====================================================
    # BEST CANDIDATE
    # =====================================================

    st.divider()

    st.header(
        "🥇 Best Candidate"
    )

    best_candidate = results[0]

    st.success(
        f'{best_candidate["resume_name"]} is the '
        f'highest-ranked candidate with a '
        f'{best_candidate["final_score"]}% match.'
    )


    # =====================================================
    # DETAILED CANDIDATE ANALYSIS
    # =====================================================

    st.divider()

    st.header(
        "🔎 Detailed Candidate Analysis"
    )

    candidate_names = [
        result["resume_name"]
        for result in results
    ]

    selected_candidate = st.selectbox(
        "Select a candidate",
        candidate_names
    )

    selected_result = next(
        result
        for result in results
        if result["resume_name"]
        == selected_candidate
    )


    # =====================================================
    # ROLE PREDICTION
    # =====================================================

    st.subheader(
        "🎯 Role Prediction"
    )

    role_value = html.escape(
        str(selected_result["predicted_role"])
    )
    confidence_value = float(
        selected_result["confidence"]
    )
    confidence_width = min(
        max(confidence_value, 0),
        100
    )

    st.markdown(
        f"""
        <div class="role-overview">
            <section class="role-card">
                <div class="role-eyebrow">AI predicted role</div>
                <div class="role-value">{role_value}</div>
            </section>
            <section class="role-card">
                <div class="role-eyebrow">Prediction confidence</div>
                <div class="confidence-row">
                    <span>{confidence_value:g}%</span>
                </div>
                <div class="confidence-track">
                    <div class="confidence-fill" style="width: {confidence_width}%"></div>
                </div>
            </section>
        </div>
        """,
        unsafe_allow_html=True
    )


    # =====================================================
    # ALTERNATIVE ROLES
    # =====================================================

    if selected_result["alternatives"]:

        st.subheader(
            "🔄 Alternative Roles"
        )

        alternative_rows = []

        for alternative in (
            selected_result["alternatives"]
        ):

            alternative_rows.append(
                {
                    "Role":
                        alternative["role"],

                    "Confidence":
                        f'{alternative["confidence"]}%'
                }
            )

        alternative_df = pd.DataFrame(
            alternative_rows
        )

        st.dataframe(
            alternative_df,
            use_container_width=True,
            hide_index=True
        )


    # =====================================================
    # SCORE SUMMARY
    # =====================================================

    st.subheader(
        "📊 Score Summary"
    )

    score_col1, score_col2, score_col3, score_col4, score_col5 = st.columns(5)

    with score_col1:

        st.metric(
            "Overall Match",
            f'{selected_result["final_score"]}%'
        )

    with score_col2:

        st.metric(
            "TF-IDF",
            f'{selected_result["tfidf_score"]}%'
        )

    with score_col3:

        st.metric(
            "Skills",
            f'{selected_result["skill_score"]}%'
        )

    with score_col4:

        st.metric(
            "Experience",
            f'{selected_result["experience_score"]}%'
        )

    with score_col5:

        st.metric(
            "Education",
            f'{selected_result["education_score"]}%'
        )


    # =====================================================
    # SKILLS & RESUME SIGNALS
    # =====================================================

    st.subheader(
        "🧩 Skills & Resume Signals"
    )

    matched_col, missing_col = st.columns(2)

    with matched_col:
        render_skill_panel(
            "✅ Matched Skills",
            selected_result["matched_skills"],
            "No matching skills found.",
            "skill-match"
        )

    with missing_col:
        render_skill_panel(
            "❌ Missing Skills",
            selected_result["missing_skills"],
            "No missing skills.",
            "skill-missing"
        )

    suggestion_col, detected_col = st.columns(2)

    with suggestion_col:
        render_skill_panel(
            "💡 Improvement Suggestions",
            selected_result["improvement_suggestions"],
            "No specific improvement suggestions.",
            "skill-suggestion"
        )

    with detected_col:
        render_skill_panel(
            "🛠️ Skills Detected in Resume",
            selected_result["resume_skills"],
            "No skills detected.",
            ""
        )


    # =====================================================
    # EXPERIENCE & EDUCATION
    # =====================================================

    st.subheader(
        "🎓 Experience & Education"
    )

    candidate_education = (
        ", ".join(selected_result["candidate_education"])
        if selected_result["candidate_education"]
        else "Not detected"
    )
    required_education = (
        ", ".join(selected_result["required_education"])
        if selected_result["required_education"]
        else "Not specified"
    )

    experience_col, education_col = st.columns(2)

    with experience_col:
        st.markdown(
            f"""
            <section class="fact-card">
                <div class="fact-card-title">💼 Experience</div>
                <div class="fact-line">
                    <span class="fact-label">Candidate</span>
                    <span class="fact-value">{html.escape(str(selected_result["candidate_experience"]))} years</span>
                </div>
                <div class="fact-line">
                    <span class="fact-label">Required</span>
                    <span class="fact-value">{html.escape(str(selected_result["required_experience"]))} years</span>
                </div>
            </section>
            """,
            unsafe_allow_html=True
        )

    with education_col:
        st.markdown(
            f"""
            <section class="fact-card">
                <div class="fact-card-title">🎓 Education</div>
                <div class="fact-line">
                    <span class="fact-label">Candidate</span>
                    <span class="fact-value">{html.escape(candidate_education)}</span>
                </div>
                <div class="fact-line">
                    <span class="fact-label">Required</span>
                    <span class="fact-value">{html.escape(required_education)}</span>
                </div>
            </section>
            """,
            unsafe_allow_html=True
        )


    # =====================================================
    # RESUME QUALITY
    # =====================================================

    st.divider()

    st.header(
        "📋 Resume Quality"
    )

    st.metric(
        "Resume Completeness",
        f'{selected_result["resume_quality"]}%'
    )

    section_rows = []

    for section, present in (
        selected_result["sections"].items()
    ):

        section_rows.append(
            {
                "Resume Section":
                    section,

                "Status":
                    (
                        "✅ Present"
                        if present
                        else "❌ Missing"
                    )
            }
        )

    section_df = pd.DataFrame(
        section_rows
    )

    st.dataframe(
        section_df,
        use_container_width=True,
        hide_index=True
    )


    # =====================================================
    # CANDIDATE RECOMMENDATION
    # =====================================================

    st.divider()

    st.header(
        "💡 Candidate Recommendation"
    )

    recommendation = (
        selected_result[
            "recommendation"
        ]
    )

    if recommendation == (
        "⭐ Strong Candidate"
    ):

        st.success(
            recommendation
        )

    elif recommendation == (
        "👍 Moderate Candidate"
    ):

        st.warning(
            recommendation
        )

    else:

        st.error(
            recommendation
        )


    # =====================================================
    # CANDIDATE ANALYTICS
    # =====================================================

    st.divider()

    st.header(
        "📈 Candidate Analytics"
    )

    total_candidates = len(
        results
    )

    best_match = results[0][
        "final_score"
    ]

    average_match = round(
        sum(
            result["final_score"]
            for result in results
        )
        / total_candidates,
        2
    )

    required_skills = len(
        results[0]["job_skills"]
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "Total Candidates",
            total_candidates
        )

    with col2:

        st.metric(
            "Best Match",
            f"{best_match}%"
        )

    with col3:

        st.metric(
            "Average Match",
            f"{average_match}%"
        )

    with col4:

        st.metric(
            "Required Skills",
            required_skills
        )


    # =====================================================
    # SCORE SUMMARY TABLE
    # =====================================================

    analytics_rows = []

    for result in results:

        analytics_rows.append(
            {
                "Resume":
                    result["resume_name"],

                "Predicted Role":
                    result["predicted_role"],

                "Overall Score":
                    f'{result["final_score"]}%',

                "Skill Score":
                    f'{result["skill_score"]}%',

                "Experience Score":
                    f'{result["experience_score"]}%',

                "Education Score":
                    f'{result["education_score"]}%'
            }
        )

    analytics_df = pd.DataFrame(
        analytics_rows
    )

    st.dataframe(
        analytics_df,
        use_container_width=True,
        hide_index=True
    )


# =========================================================
# MODEL EVALUATION
# =========================================================

if results:

    st.divider()

    st.header(
        "🎯 Model Evaluation"
    )

    st.write(
        "Select the actual/correct role for each candidate. "
        "The system compares the actual role with the predicted role."
    )

    try:

        model_roles = list(
            model.classes_
        )

    except:

        model_roles = []

    role_options = list(
        dict.fromkeys(
            model_roles
            +
            [
                result["predicted_role"]
                for result in results
            ]
        )
    )

    with st.form(
        "model_evaluation_form"
    ):

        selected_roles = {}

        for index, result in enumerate(
            results
        ):

            resume_name = (
                result["resume_name"]
            )

            current_value = (
                st.session_state.actual_roles.get(
                    resume_name,
                    role_options[0]
                    if role_options
                    else ""
                )
            )

            selected_roles[
                resume_name
            ] = st.selectbox(

                f"Actual role for #{index + 1} — "
                f"{resume_name}",

                role_options,

                index=(
                    role_options.index(
                        current_value
                    )
                    if current_value
                    in role_options
                    else 0
                ),

                key=f"actual_role_{index}"
            )

        evaluate_button = (
            st.form_submit_button(
                "📊 Evaluate Model",
                type="primary"
            )
        )


    if evaluate_button:

        st.session_state.actual_roles = (
            selected_roles
        )

        st.session_state.evaluation_done = (
            True
        )

        st.rerun()


# =========================================================
# PREDICTION RESULTS
# =========================================================

if (
    results
    and st.session_state.evaluation_done
):

    prediction_rows = []

    for result in results:

        resume_name = (
            result["resume_name"]
        )

        actual_role = (
            st.session_state.actual_roles[
                resume_name
            ]
        )

        predicted_role = (
            result["predicted_role"]
        )

        if actual_role == predicted_role:

            evaluation_result = (
                "✅ Correct"
            )

        else:

            evaluation_result = (
                "❌ Incorrect"
            )

        prediction_rows.append(
            {
                "Resume":
                    resume_name,

                "Actual Role":
                    actual_role,

                "Predicted Role":
                    predicted_role,

                "Result":
                    evaluation_result
            }
        )

    st.divider()

    st.subheader(
        "📋 Prediction Results"
    )

    prediction_df = pd.DataFrame(
        prediction_rows
    )

    st.dataframe(
        prediction_df,
        use_container_width=True,
        hide_index=True
    )