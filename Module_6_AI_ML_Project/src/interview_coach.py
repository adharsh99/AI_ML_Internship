
import os

from dotenv import load_dotenv
from groq import Groq


# Load environment variables
load_dotenv()

# Get Groq API key
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError(
        "GROQ_API_KEY was not found in the .env file."
    )

# Create Groq client
client = Groq(api_key=api_key)


def generate_interview_questions(job_role):
    """
    Generate interview questions for a selected job role.
    """

    prompt = f"""
You are an expert technical interviewer.

Generate 5 interview questions for a candidate
applying for the following job role:

{job_role}

Include:
1. Technical questions
2. Practical questions
3. Scenario-based questions
4. HR question

Number all questions clearly.
Keep the questions suitable for a fresher.
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.4
    )

    return response.choices[0].message.content


def evaluate_answer(question, answer):
    """
    Evaluate a candidate's interview answer.
    """

    prompt = f"""
You are an AI interview coach.

Interview Question:
{question}

Candidate Answer:
{answer}

Evaluate the candidate's answer.

Provide:

1. Score out of 10
2. Technical Accuracy
3. Communication Quality
4. What was done well
5. Missing Points
6. Improvement Suggestions

Give clear and professional feedback suitable
for a fresher preparing for an interview.
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