import os
import openai
import streamlit as st
from dotenv import load_dotenv
from resume_parser import parse_resume
from gpt_feedback import get_gpt_feedback

# ✅ Load API key from .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# ✅ Streamlit app setup
st.set_page_config(page_title="Resume Parser GPT", layout="centered")
st.title("📄 Resume Parser + GPT Feedback")
st.markdown("Upload your resume PDF and get smart insights + GPT-powered feedback!")

# ✅ Upload section
uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

if uploaded_file is not None:
    # Save the uploaded PDF
    with open("sample_resume.pdf", "wb") as f:
        f.write(uploaded_file.read())

    # Parse resume
    parsed_data = parse_resume("sample_resume.pdf")

    # Show parsed info
    st.subheader("📌 Parsed Information")
    for key, value in parsed_data.items():
        st.write(f"**{key}:** {value}")

    # Show GPT feedback
    st.subheader("🤖 GPT Feedback")
    feedback = get_gpt_feedback(parsed_data)
    st.success(feedback)
