Intelligent Resume Screening System

An AI-powered Intelligent Resume Screening System that analyzes resumes against job descriptions using Machine Learning and Natural Language Processing (NLP) techniques.
The system helps recruiters identify suitable candidates by evaluating resume content, matching skills, analyzing experience and education, predicting suitable job roles, and ranking candidates based on an overall match score.

🎯 Objective
The main objective of this project is to automate and improve the initial resume screening process by combining **NLP, Machine Learning, skill matching, and candidate scoring** into a single application.

🚀 Features

- 📄 Upload multiple resumes
- 📝 Enter a Job Description
- 🔍 TF-IDF based resume-job similarity
- 🛠️ Automatic skill extraction and skill matching
- 💼 Experience analysis
- 🎓 Education analysis
- 🤖 Machine Learning based job role prediction
- 📊 Candidate ranking
- ⭐ Best candidate identification
- 📈 Model prediction confidence and alternative roles
- 🔎 Detailed candidate analysis
- 💡 Missing skill identification
- 📋 Resume quality and section completeness analysis
- ✅ Candidate recommendation
- 📊 Model evaluation using actual and predicted roles
- 📑 PDF screening report generation

# Machine Learning Approach
The system uses TF-IDF (Term Frequency-Inverse Document Frequency) to convert resume and job description text into numerical vectors.
Cosine Similarity is then used to calculate the similarity between the resume and job description.

The final candidate score combines multiple factors:
- TF-IDF Match – 50%
- Skill Match – 30%
- Experience Match – 10%
- Education Match – 10%

The system also uses a trained Machine Learning classification model to predict the most suitable job role for each resume.

# Supported Job Roles
The model supports multiple technical and non-technical domains, including:

- Software Developer
- Web Developer
- Machine Learning Engineer
- Data Scientist
- Data Analyst
- Accountant
- Financial Analyst
- HR Executive
- Marketing Executive
- Sales Executive
- Business Analyst
- Mechanical Engineer
- Civil Engineer
- Teacher
- Healthcare Administrator
- Electrical Engineer
- Quality Analyst
- Digital Associate
- CRM-related roles

# Technologies Used

# Programming
- Python

# Machine Learning & NLP
- Scikit-learn
- TF-IDF
- Cosine Similarity
- Text Classification

# Data Processing
- Pandas
- NumPy
- Regular Expressions

# Application
- Streamlit

# Development Tools
- Git
- GitHub
- VS Code


# System Workflow

Job Description
       ↓
Resume Upload
       ↓
Text Extraction
       ↓
Text Cleaning
       ↓
TF-IDF Processing
       ↓
Skill Extraction & Matching
       ↓
Experience Analysis
       ↓
Education Analysis
       ↓
ML Role Prediction
       ↓
Candidate Scoring
       ↓
Candidate Ranking
       ↓
Screening Report


# 📊 Candidate Scoring

The system calculates an overall match score using:


Final Score =
(TF-IDF Score × 50%)
+
(Skill Score × 30%)
+
(Experience Score × 10%)
+
(Education Score × 10%)


Based on the final score, candidates are categorized as:

- 75% and above → Strong Candidate
- 50%–74% → Moderate Candidate
- Below 50% → Needs Improvement

#Screening Report
The system can generate a downloadable PDF report containing:

- Candidate ranking
- Match score
- Skill match
- Experience
- Education
- Predicted role
- Actual role
- Missing skills
- Candidate recommendation
- Explanation of the candidate score


