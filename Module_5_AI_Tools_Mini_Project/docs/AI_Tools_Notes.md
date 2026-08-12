# AI Tools & Mini Project Notes

## 1. Introduction

Module 5 focuses on understanding AI tools and building a simple AI-powered application.

For this module, I developed an AI Resume Analyzer.

## 2. AI Tools

AI tools can help with:

- Coding
- Research
- Writing
- Productivity
- Data Analysis
- Learning
- Resume Improvement

Examples of AI tools include:

- ChatGPT
- Google Gemini
- Microsoft Copilot
- Groq

## 3. Mini Project

### Project Name

AI Resume Analyzer

### Objective

The objective of this project is to create an AI-powered application that analyzes a user's resume and provides useful feedback.

## 4. Technologies Used

- Python
- Streamlit
- Groq API
- Llama 3.3 70B
- PyPDF
- python-dotenv

## 5. Application Workflow

Upload Resume
        |
        v
Extract PDF Text
        |
        v
Send Resume Text to AI
        |
        v
AI Analysis
        |
        v
Display Results

## 6. Features

The application provides:

- PDF Resume Upload
- Resume Text Extraction
- ATS Score
- Technical Skills
- Soft Skills
- Education Summary
- Recommended Skills
- Resume Strengths
- Resume Weaknesses
- Improvement Suggestions
- Overall Resume Summary

## 7. How AI Is Used

The application extracts the text from the uploaded PDF resume.

The extracted resume text is sent to the AI model through the Groq API.

The AI analyzes the resume and provides professional feedback.

## 8. Learning Outcomes

I learned:

- How AI tools can help developers
- How AI can be used for productivity
- How to integrate an AI API with Python
- How to use Streamlit
- How to extract text from PDF files
- How to use environment variables
- How to build an AI-powered application
- How to document a project
- How to use GitHub for project submission

## 9. Project Structure

Module_5_AI_Tools_Mini_Project
|
|-- app.py
|-- README.md
|-- requirements.txt
|-- .gitignore
|
|-- data
|
|-- docs
|   |-- ai tools notes.md
|
|-- screenshots
|
|-- venv

## 10. How to Run the Project

Step 1: Create virtual environment

python -m venv venv

Step 2: Activate virtual environment

venv\Scripts\activate.bat

Step 3: Install required packages

pip install -r requirements.txt

Step 4: Add the Groq API key to .env

GROQ_API_KEY=your_api_key_here

Step 5: Run the application

python -m streamlit run app.py

Step 6: Open the application

http://localhost:8501

## 11. Future Improvements

- Add DOCX resume support
- Compare resume with job descriptions
- Generate downloadable analysis reports
- Add resume improvement suggestions
- Add multiple AI model support
- Add resume scoring based on specific job descriptions

## 12. Conclusion

The AI Resume Analyzer helped me understand the practical use of AI tools and API integration.

This project combines Python, Streamlit, PDF processing and Generative AI to create a simple real-world AI application.