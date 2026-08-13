import os

from dotenv import load_dotenv
from groq import Groq


load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError(
        "GROQ_API_KEY was not found in the .env file."
    )

client = Groq(api_key=api_key)


def analyze_resume(resume_text):

    prompt = f"""
You are an expert resume and career analyst.

Analyze the following resume:

-------------------------
{resume_text}
-------------------------

Provide the analysis using these sections:

1. Candidate Name
2. Education
3. Technical Skills
4. Soft Skills
5. Projects
6. Experience
7. Certifications
8. Strengths
9. Weaknesses
10. Missing Skills
11. Resume Improvement Suggestions
12. Suitable Job Roles
13. Overall Resume Score out of 100

Give clear and professional answers.
"""

    response = client.chat.completions.create(

        model="llama-3.1-8b-instant",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.2
    )

    return response.choices[0].message.content