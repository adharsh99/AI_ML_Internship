import streamlit as st

from src.resume_parser import extract_text_from_pdf
from src.resume_analyzer import analyze_resume
from src.job_matcher import match_resume_with_job
from src.ml_model import predict_job_role
from src.interview_coach import (
    generate_interview_questions,
    evaluate_answer
)


st.set_page_config(
    page_title="AI Career Assistant",
    page_icon="🤖",
    layout="wide"
)


def main():

    st.title("🤖 AI Career Assistant")
    st.subheader(
        "Resume Analyzer • Job Matcher • Interview Coach"
    )

    st.sidebar.title("Navigation")

    option = st.sidebar.radio(
        "Choose a feature",
        [
            "🏠 Home",
            "📄 Resume Analyzer",
            "💼 Job Matcher",
            "🎤 Interview Coach"
        ]
    )

    if option == "🏠 Home":

        st.header("Welcome to AI Career Assistant")

        st.write(
            """
            AI Career Assistant is an AI-powered career platform
            designed to help job seekers improve their career readiness.

            Features:

            📄 Resume Analysis
            💼 Job Matching
            🎯 Skill Gap Identification
            🎤 AI Interview Coaching
            🤖 Job Role Recommendation
            """
        )

        st.info(
            "Upload your resume and explore the available career tools."
        )

    elif option == "📄 Resume Analyzer":

        st.header("📄 Resume Analyzer")

        uploaded_file = st.file_uploader(
            "Upload your Resume PDF",
            type=["pdf"]
        )

        if uploaded_file:

            if st.button("Analyze Resume"):

                with st.spinner("Extracting resume text..."):

                    resume_text = extract_text_from_pdf(
                        uploaded_file
                    )

                if not resume_text:

                    st.error(
                        "Unable to extract text from this PDF."
                    )

                else:

                    st.success(
                        "Resume text extracted successfully."
                    )

                    with st.spinner(
                        "AI is analyzing your resume..."
                    ):

                        result = analyze_resume(
                            resume_text
                        )

                    st.subheader("📊 Resume Analysis")

                    st.write(result)

                    st.session_state["resume_text"] = (
                        resume_text
                    )

    elif option == "💼 Job Matcher":

        st.header("💼 Job Matcher")

        resume_text = st.session_state.get(
            "resume_text",
            ""
        )

        if not resume_text:

            st.warning(
                "Please analyze your resume first."
            )

        else:

            job_description = st.text_area(
                "Paste the Job Description"
            )

            if st.button("Match Job"):

                if not job_description.strip():

                    st.error(
                        "Please enter a job description."
                    )

                else:

                    result = match_resume_with_job(
                        resume_text,
                        job_description
                    )

                    st.subheader("🎯 Job Match Result")

                    st.metric(
                        "Match Percentage",
                        f"{result['match_percentage']}%"
                    )

                    st.write("### ✅ Matching Skills")

                    for skill in result["matching_skills"]:
                        st.success(skill)

                    st.write("### ❌ Missing Skills")

                    for skill in result["missing_skills"]:
                        st.error(skill)

                    if result["matching_skills"]:

                        predicted_role = predict_job_role(
                            result["matching_skills"]
                        )

                        st.subheader(
                            "🤖 Recommended Job Role"
                        )

                        st.info(predicted_role)

    elif option == "🎤 Interview Coach":

        st.header("🎤 AI Interview Coach")

        job_role = st.selectbox(
            "Select Job Role",
            [
                "Python Developer",
                "Data Analyst",
                "Machine Learning Engineer",
                "Full Stack Developer",
                "AI Engineer"
            ]
        )

        if st.button(
            "Generate Interview Questions"
        ):

            with st.spinner(
                "Generating interview questions..."
            ):

                questions = (
                    generate_interview_questions(
                        job_role
                    )
                )

            st.session_state["questions"] = questions

        if "questions" in st.session_state:

            st.subheader("📝 Interview Questions")

            st.write(
                st.session_state["questions"]
            )

            question = st.text_area(
                "Enter the interview question"
            )

            answer = st.text_area(
                "Enter your answer"
            )

            if st.button(
                "Evaluate My Answer"
            ):

                if not question or not answer:

                    st.warning(
                        "Please enter both question and answer."
                    )

                else:

                    with st.spinner(
                        "AI is evaluating your answer..."
                    ):

                        feedback = evaluate_answer(
                            question,
                            answer
                        )

                    st.subheader(
                        "📊 Interview Feedback"
                    )

                    st.write(feedback)


if __name__ == "__main__":
    main()