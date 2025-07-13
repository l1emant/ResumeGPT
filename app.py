import os
import streamlit as st
from dotenv import load_dotenv
from PIL import Image
import google.generativeai as genai
from pdf2image import convert_from_path
import pytesseract
import pdfplumber

# Load environment variables
load_dotenv()

# Configure Google Gemini AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        # Try direct text extraction
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text

        if text.strip():
            return text.strip()
    except Exception as e:
        print(f"Direct text extraction failed: {e}")

    # Fallback to OCR for image-based PDFs
    print("Falling back to OCR for image-based PDF.")
    try:
        images = convert_from_path(pdf_path)
        for image in images:
            page_text = pytesseract.image_to_string(image)
            text += page_text + "\n"
    except Exception as e:
        print(f"OCR failed: {e}")

    return text.strip()

# Function to get response from Gemini AI
def analyze_resume(resume_text, job_description=None):
    if not resume_text:
        return {"error": "Resume text is required for analysis."}
    
    model = genai.GenerativeModel("gemini-2.5-flash")
    
    base_prompt = f"""
    You are an experienced HR with Technical Experience in the field of any one job role from Data Science, Data Analyst, DevOPS, Machine Learning Engineer, Prompt Engineer, AI Engineer, Full Stack Web Development, Big Data Engineering, Marketing Analyst, Human Resource Manager, Software Developer your task is to review the provided resume.
    Please share your professional evaluation on whether the candidate's profile aligns with the role.ALso mention Skills he already have and siggest some skills to imorve his resume , alos suggest some course he might take to improve the skills.Highlight the strengths and weaknesses.Rate the resume on a scale of 1 to 10 based on the following criteria:

    Professional Experience: {resume_text}
    Education: {resume_text}
    Skills: {resume_text}
    Certifications: {resume_text}
    Projects: {resume_text}
    Soft Skills: {resume_text}
    Overall Impression: {resume_text}
    Provide a detailed analysis of the resume, including any notable achievements or areas for improvement.
    
    If you find any areas for improvement, please provide suggestions for improvement.
    Provide a summary of the candidate's qualifications and readiness for the job market.

    Resume:
    {resume_text}
    """

    if job_description:
        base_prompt += f"""
        Additionally, compare this resume to the following job description:
        
        Job Description:
        {job_description}
        
        Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
        """

    response = model.generate_content(base_prompt)

    analysis = response.text.strip()
    return analysis


# Streamlit app

st.set_page_config(page_title="ResumeGPT", layout="wide", initial_sidebar_state="expanded")
st.markdown("""
    <style>
        body {
            background-color: #262626;
            color: white;
        }
        h1, h2, h3, h4, h5, h6 {
            color: #B3001B;
        }
    </style>
""", unsafe_allow_html=True)

st.title("ResumeGPT")
st.markdown("""
    <style>
        .stApp {
            background-color: #262626;
        }
        .stButton>button {
            background-color: #B3001B;
            color: white;
            border-radius: 5px;
            padding: 10px 20px;
            border: none;
            font-size: 16px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #B3001B;
            color: white;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }
        .stButton>button:active {
            background-color: #B3001B;
            color: white;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
            transform: translateY(2px);
        }
        .stButton>button:focus {
            outline: none;
            box-shadow: 0 0 0 3px rgba(0, 0, 0, 0.2);
            background-color: #B3001B;
            color: white;
        }
        .stButton>button:disabled {
            background-color: #B3001B;
            color: white;
            opacity: 0.5;
            cursor: not-allowed;
            box-shadow: none;
        }
    </style>
""", unsafe_allow_html=True)
# Title
st.title("AI Resume Analyzer")
st.write("ResumeGPT is an intelligent resume assistant designed to review, enhance, and optimize your resume using the power of Generative AI.")

col1 , col2 = st.columns(2)
with col1:
    uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])
with col2:
    job_description = st.text_area("Enter Job Description:", placeholder="Paste the job description here...")

if uploaded_file is not None:
    st.success("Resume uploaded successfully!")
else:
    st.warning("Please upload a resume in PDF format.")


st.markdown("<div style= 'padding-top: 10px;'></div>", unsafe_allow_html=True)
if uploaded_file:
    # Save uploaded file locally for processing
    with open("uploaded_resume.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())
    # Extract text from PDF 
    st.markdown("### Extracting text from resume...")
    st.spinner("Extracting text from resume...")
    st.markdown("<div style= 'padding-top: 10px;'></div>", unsafe_allow_html=True)
    st.markdown("### Analyzing resume...")
    st.spinner("Analyzing resume...")
    st.markdown("<div style= 'padding-top: 10px;'></div>", unsafe_allow_html=True)
    # Extract text from the uploaded PDF
    resume_text = extract_text_from_pdf("uploaded_resume.pdf")
    if not resume_text:
        st.error("Failed to extract text from the resume. Please ensure the PDF is readable.")
    else:
        st.success("Text extracted successfully!")
        st.markdown("### Extracted Text:")
        st.text_area("Resume Text", value=resume_text, height=300)
    st.markdown("<div style= 'padding-top: 10px;'></div>", unsafe_allow_html=True)
    # Analyze the resume
    st.markdown("### Analyzing resume...")
    st.spinner("Analyzing resume...")
    st.markdown("<div style= 'padding-top: 10px;'></div>", unsafe_allow_html=True)
    # Check if the resume text is available
    if not resume_text:
        st.error("No resume text available for analysis. Please upload a valid PDF resume.")
    else:
        st.success("Resume text is ready for analysis.")
    # Button to trigger analysis
    st.markdown("<div style= 'padding-top: 10px;'></div>", unsafe_allow_html=True)
    st.markdown("### Click the button below to analyze the resume:")
    st.markdown("<div style= 'padding-top: 10px;'></div>", unsafe_allow_html=True)
    st.markdown("### Resume Analysis:")
# Button to analyze resume
if st.button("Analyze Resume"):
    with st.spinner("Analyzing resume..."):
        try:
            # Analyze resume
            analysis = analyze_resume(resume_text, job_description)
            st.success("Analysis complete!")
            st.write(analysis)
            
            # Download button for the analysis
            st.markdown("<div style= 'padding-top: 10px;'></div>", unsafe_allow_html=True)
            st.markdown("### Download Analysis Report:")
            st.download_button(
                label="Download Analysis Report",
                data=analysis,
                file_name="analysis_report.txt",
                mime="text/plain"
            )
        except Exception as e:
            st.error(f"Analysis failed: {e}")


#Footer
st.markdown("---")
st.markdown("""
    <style>
        footer {
            text-align: center;
            padding: 20px;
            background-color: #262626;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)
st.markdown("<footer>Made with ❤️ by Hemant</footer>", unsafe_allow_html=True)