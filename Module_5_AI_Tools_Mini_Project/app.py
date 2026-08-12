import os

import streamlit as st
from dotenv import load_dotenv
from groq import Groq
from pypdf import PdfReader


# Load environment variables
load_dotenv()

# Get Groq API key
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.error("Groq API key was not found. Please check your .env file.")
    st.stop()

# Create Groq client
client = Groq(api_key=api_key)


# Page configuration
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄"
)


# Application title
st.title("📄 AI Resume Analyzer")

st.write(
    "Upload your resume and get AI-powered resume analysis."
)


# Upload PDF
uploaded_file = st.file_uploader(
    "Upload your Resume (PDF)",
    type=["pdf"]
)


if uploaded_file is not None:

    st.success("Resume uploaded successfully!")

    # Read PDF
    reader = PdfReader(uploaded_file)

    resume_text = ""

    for page in reader.pages:
        text = page.extract_text()

        if text:
            resume_text += text


    # Display extracted text
    st.subheader("📑 Extracted Resume Text")

    st.text_area(
        "Resume Content",
        resume_text,
        height=300
    )


    # Analyze button
    if st.button("🤖 Analyze Resume"):

        with st.spinner("AI is analyzing your resume..."):

            prompt = f"""
You are an expert professional resume analyzer and ATS consultant.

Analyze the resume below.

Provide the following:

1. ATS Score out of 100
2. Technical Skills
3. Soft Skills
4. Education Summary
5. Missing or Recommended Skills
6. Resume Strengths
7. Resume Weaknesses
8. Improvement Suggestions
9. Overall Resume Summary

Give the answer in a clear and professional format.

Resume:

{resume_text}
"""


            # Send request to Groq
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.3
            )


            # Get AI response
            analysis = response.choices[0].message.content


            # Display result
            st.subheader("🤖 AI Resume Analysis")

            st.markdown(analysis)