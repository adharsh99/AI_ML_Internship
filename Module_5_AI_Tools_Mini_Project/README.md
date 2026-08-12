# AI Resume Analyzer

## Module 5 - AI Tools & Mini Project

## 1. Project Description

AI Resume Analyzer is a simple AI-powered web application developed as part of Module 5 of the AI/ML Internship.

The application allows users to upload a PDF resume and receive AI-powered feedback about their resume.

## 2. Project Objective

The main objectives of this project are:

- Explore AI tools
- Understand how AI can help with productivity
- Learn AI API integration
- Build a simple AI-powered application
- Practice Python and Streamlit
- Analyze resumes using Generative AI

## 3. AI Tools Explored

During this module, I explored AI tools such as:

- ChatGPT
- Google Gemini
- Microsoft Copilot
- Groq

These tools can help with:

- Coding
- Research
- Writing
- Productivity
- Learning
- Data Analysis

## 4. Mini Project

### AI Resume Analyzer

The application analyzes a user's resume and provides useful AI-generated feedback.

## 5. Technologies Used

- Python
- Streamlit
- Groq API
- Llama 3.3 70B
- PyPDF
- python-dotenv

## 6. Features

The application provides:

- PDF Resume Upload
- Resume Text Extraction
- ATS Score
- Technical Skills Analysis
- Soft Skills Analysis
- Education Summary
- Recommended Skills
- Resume Strengths
- Resume Weaknesses
- Improvement Suggestions
- Overall Resume Summary

## 7. Application Workflow

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

## 8. Project Structure

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

## 9. Installation

### Step 1: Create virtual environment

python -m venv venv

### Step 2: Activate virtual environment

Windows CMD:

venv\Scripts\activate.bat

### Step 3: Install required packages

pip install -r requirements.txt

## 10. API Key Configuration

Create a .env file in the project folder.

Add:

GROQ_API_KEY=your_api_key_here

Do not share the API key publicly.

The .env file is included in .gitignore.

## 11. Run the Application

Run:

python -m streamlit run app.py

Then open:

http://localhost:8501

## 12. How to Use

1. Open the application.
2. Click the resume upload button.
3. Select a PDF resume.
4. Wait for the resume text to be extracted.
5. Click "Analyze Resume".
6. Wait for the AI analysis.
7. Read the generated resume feedback.

## 13. AI Analysis Output

The application generates:

### ATS Score

A score out of 100 based on the resume content.

### Technical Skills

Identifies technical skills mentioned in the resume.

### Soft Skills

Identifies soft skills mentioned in the resume.

### Education Summary

Provides a summary of educational qualifications.

### Recommended Skills

Suggests skills that could improve the resume.

### Strengths

Identifies strong areas of the resume.

### Weaknesses

Identifies areas that need improvement.

### Improvement Suggestions

Provides recommendations to improve the resume.

### Overall Summary

Provides a professional summary of the resume.

## 14. Learning Outcomes

Through this project, I learned:

- How AI tools can help developers
- How to integrate an AI API with Python
- How to use Streamlit
- How to extract text from PDF files
- How to use environment variables
- How to build an AI-powered application
- How to document a project
- How to use GitHub for project submission

## 15. Future Improvements

Possible future improvements include:

- DOCX resume support
- Job description comparison
- Downloadable analysis report
- Resume improvement generator
- Multiple AI model support
- Job-specific ATS scoring

## 16. Conclusion

The AI Resume Analyzer demonstrates how Generative AI can be integrated into a practical application.

The project combines Python, Streamlit, PDF processing and AI to provide useful resume analysis.

## 17. Author

BCA Graduate

## 18. Internship Module

Codemax AI/ML Internship

Module 5 - AI Tools & Mini Project