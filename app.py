import streamlit as st
import PyPDF2
from io import BytesIO
from google import genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

# Create Gemini client
client = genai.Client(api_key=api_key)

st.title("📄 AI Resume Analyzer")

st.write("Upload your resume and get AI feedback.")

uploaded_file = st.file_uploader(
    "Upload your resume (PDF)",
    type=["pdf"]
)

# Function to extract text
def extract_text_from_pdf(pdf_file):

    pdf_reader = PyPDF2.PdfReader(
        BytesIO(pdf_file.read())
    )

    text = ""

    for page in pdf_reader.pages:

        page_text = page.extract_text()

        if page_text:

            text += page_text + "\n"

    return text.strip()

# If file uploaded
if uploaded_file is not None:

    st.success("Resume uploaded successfully!")

    resume_text = extract_text_from_pdf(uploaded_file)

    st.write("Characters extracted:", len(resume_text))

    # Analyze button
    if st.button("Analyze Resume"):

        with st.spinner("Analyzing with AI..."):

            prompt = f"""
            Analyze this resume.

            Give:
            1. Professional summary
            2. Key strengths
            3. Missing skills
            4. Suggested improvements
            5. Best job roles
            6. Resume score out of 10

            Resume:
            {resume_text}
            """

            try:

                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt
                )

                st.subheader("AI Resume Analysis")

                st.write(response.text)

            except Exception as e:

                st.error(str(e))