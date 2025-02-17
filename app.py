import streamlit as st
import google.generativeai as genai

# Configure Gemini AI with API Key
genai.configure(api_key="AIzaSyAx3h78wGInDTX5DFfeS_yn38mintn4VSI")

# System instruction for AI
system_prompt = """You are an expert Python code reviewer with deep knowledge of best practices, debugging, optimization, and clean coding standards. Your task is to carefully analyze the provided Python code, identifying potential errors, inefficiencies, and areas for improvement.

Provide a structured response that includes:

Code Analysis: Explain the overall functionality of the code.
Error Detection: Identify syntax errors, logical errors, and runtime issues.
Performance Optimization: Suggest ways to improve efficiency.
Best Practices: Recommend improvements for readability, maintainability, and security.
Final Rating: Give a rating out of 5 based on code quality, efficiency, and correctness.
Only accept Python code as input. If the input is not valid Python code, politely reject it and request a valid submission.."""

# Initialize Gemini AI
gemini = genai.GenerativeModel(
    model_name="models/gemini-2.0-pro-exp",
    system_instruction=system_prompt
)

# Streamlit UI
st.title("🚀 Python Code Reviewer")
st.write("Enter your Python code snippet for review.")

# Text input for user
user_prompt = st.text_area("Enter your Python code:", height=250)

# Button to process the code
if st.button("🔍 Review Code"):
    if user_prompt.strip():
        with st.spinner("Reviewing your code... ⏳"):
            response = gemini.generate_content(user_prompt, stream=True)
        # Display AI Review
        st.subheader("✅ AI Review:")
        for chunk in response:
            st.write(chunk.text)
    else:
        st.warning("⚠️ Please enter a Python code snippet first.")

# Instructions
st.sidebar.header("Instructions")
st.sidebar.markdown("""
1. Paste your Python code in the text area
2. Click 'Review Code'
3. View the code review feedback
""")

