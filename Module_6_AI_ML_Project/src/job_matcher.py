import re


SKILLS = [
    "python",
    "java",
    "sql",
    "c",
    "c++",
    "javascript",
    "html",
    "css",
    "react",
    "django",
    "fastapi",
    "flask",
    "pandas",
    "numpy",
    "scikit-learn",
    "machine learning",
    "deep learning",
    "tensorflow",
    "power bi",
    "excel",
    "git",
    "github",
    "docker",
    "aws",
    "rest api",
    "streamlit"
]


def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in SKILLS:

        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(pattern, text):

            found_skills.append(skill)

    return sorted(set(found_skills))


def match_resume_with_job(
    resume_text,
    job_description
):

    resume_skills = set(
        extract_skills(resume_text)
    )

    job_skills = set(
        extract_skills(job_description)
    )

    if not job_skills:

        return {
            "match_percentage": 0,
            "matching_skills": [],
            "missing_skills": []
        }

    matching_skills = sorted(
        resume_skills.intersection(job_skills)
    )

    missing_skills = sorted(
        job_skills - resume_skills
    )

    match_percentage = (
        len(matching_skills)
        / len(job_skills)
    ) * 100

    return {

        "match_percentage":
            round(match_percentage, 2),

        "matching_skills":
            matching_skills,

        "missing_skills":
            missing_skills
    }