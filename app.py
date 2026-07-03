import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
import PyPDF2
import io

# Load environment variables
load_dotenv()

# Page config for dark theme
st.set_page_config(
    page_title="AI Resume Screener",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for dark theme
st.markdown("""
<style>
    .stApp {
        background-color: #1a1a1a;
        color: #ffffff;
    }
    .stSidebar {
        background-color: #2d2d2d;
    }
    .stTextInput, .stTextArea, .stNumberInput {
        background-color: #3d3d3d !important;
        color: #ffffff !important;
    }
    .stButton>button {
        width: 100%;
        background-color: #ff4b4b;
        color: white;
        border: none;
        padding: 10px 15px;
        border-radius: 5px;
    }
    .stButton>button:hover {
        background-color: #ff6b6b;
    }
    .upload-box {
        border: 2px dashed #666;
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        margin: 10px 0;
    }
    .main-title {
        color: #ff4b4b;
        text-align: center;
        padding: 20px 0;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar Configuration
with st.sidebar:
    st.title("⚙️ Configuration")
    
    # API Key Setup
    st.subheader("🔑 API Setup")
    api_key = st.text_input(
        "Google API Key",
        type="password",
        help="Get your API key from https://makersuite.google.com/app/apikey"
    )
    
    if not api_key:
        st.warning("API key required for AI features")
    
    # Scoring Method
    st.subheader("📊 Scoring Method")
    scoring_method = st.selectbox(
        "Choose analysis approach:",
        ["Hybrid Approach", "Keyword Matching", "Semantic Analysis"],
        index=0
    )
    
    # Qualification Threshold
    st.subheader("🎯 Qualification Threshold")
    threshold = st.slider(
        "Minimum score for qualification",
        min_value=0,
        max_value=100,
        value=70
    )

# Main Content
st.markdown("<h1 class='main-title'>🎯 AI Resume Screener</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888;'>Powered by Gemini AI & Advanced Analytics</p>", unsafe_allow_html=True)

# Create two columns for job description and resume
col1, col2 = st.columns(2)

with col1:
    st.subheader("📄 Job Description")
    job_description = st.text_area(
        "Paste the complete job description here",
        height=300,
        placeholder="Enter the job requirements, skills needed, experience level, etc."
    )

with col2:
    st.subheader("📎 Resume Upload")
    uploaded_file = st.file_uploader(
        "Upload your resume (PDF)",
        type=["pdf"],
        help="Upload a PDF file only"
    )
    
    resume_text = ""
    if uploaded_file:
        try:
            pdf_reader = PyPDF2.PdfReader(io.BytesIO(uploaded_file.read()))
            for page in pdf_reader.pages:
                resume_text += page.extract_text()
            st.success("Resume uploaded successfully!")
        except Exception as e:
            st.error(f"Error processing PDF: {str(e)}")

# Analysis Button
if st.button("🔍 Start Resume Screening", use_container_width=True):
    if not api_key:
        st.error("Please enter your Google API Key in the sidebar first.")
    elif not job_description:
        st.error("Please enter the job description.")
    elif not resume_text:
        st.error("Please upload your resume.")
    else:
        try:
            # Configure Google Generative AI with the provided API key
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-pro')
            
            with st.spinner('Analyzing your resume...'):
                prompt = f"""Analyze this resume against the job description and provide:
                1. ATS Score (0-100)
                2. Missing Keywords
                3. Improvement Suggestions
                4. Overall Analysis

                Scoring Method: {scoring_method}
                Qualification Threshold: {threshold}%

                Resume:
                {resume_text}

                Job Description:
                {job_description}
                """
                
                response = model.generate_content(prompt)
                
                # Display results in an organized way
                st.markdown("### 📊 Analysis Results")
                st.markdown(response.text)
                
        except Exception as e:

            st.error(f'Error analyzing resume: {str(e)}')

