# 📄 ResumeGPT: AI-Powered Resume Enhancer & Reviewer

**ResumeGPT** is an intelligent resume assistant designed to review, enhance, and optimize your resume using the power of Generative AI. Built for job seekers, students, and professionals, it offers actionable feedback and rewrites your experience section to help you stand out to recruiters and Applicant Tracking Systems (ATS).

---

## What It Does

ResumeGPT serves as your virtual resume coach by:
- Analyzing your resume content for clarity, structure, and impact  
- Suggesting improved bullet points using action verbs and measurable outcomes  
- Providing a smart resume score out of 100 based on relevance and quality  
- Tailoring feedback to the specific job role you’re targeting

---

## Key Features

###   Resume Analyzer
- Identifies weak phrasing and vague language  
- Checks for missing metrics or impact statements  
- Highlights strengths and areas needing revision

###   Resume Rewriter
- Enhances bullet points using professional language  
- Adds metrics and outcome-driven wording where possible  
- Aligns tone and phrasing with target job roles

###   Resume Score
- Rates the resume on a scale of 0–10 
- Criteria include clarity, action orientation, relevance, and structure  
- Gives interpretation ranges (e.g., “Good”, “Needs Work”, “Excellent”)

---

## Tech Stack

| Component     | Technology Used                            |
|---------------|---------------------------------------------|
| **Interface** | [Streamlit](https://streamlit.io/) for UI         |
| **Backend**   | Python, Hugging Face Spaces           |
| **Model**     | Google Gemini 2.5|
| **PDF Parsing**| `pdfplumber` `pdf2image` |

---

## How It Works

1. **User Input**  
   - Paste resume text manually, or load from a PDF (optional add-on)  
   - Specify the target job role (e.g., “Data Analyst”)

2. **LLM Processing**  
   - ResumeGPT uses a prompt-engineered LLM to analyze and enhance the content  
   - A professional-style review and rewrite is generated

3. **Result Output**  
   - Key observations  
   - Rewritten section  
   - Resume score out of 10 with interpretation

---

## Example Use

> **Input:**  
> - Resume Line: "Worked on Python projects in college"  
> - Job Role: Software Engineer  
>
> **AI Output:**  
> - Rewritten: *"Developed and deployed Python-based applications for real-world college projects, improving user engagement by 30%."*  
> - Score: 7/10 (Good, but could use more quantifiable achievements)

---

### Built With ❤️ By Hemant

