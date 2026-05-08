# 📄 AI Resume Analyzer

An AI-powered Resume Analyzer built using **Streamlit**, **Google Gemini API**, and **PyPDF2**.

This application allows users to upload a PDF resume and receive AI-generated feedback including:
- Professional Summary
- Key Strengths
- Missing Skills
- Suggested Improvements
- Suitable Job Roles
- Resume Score

---

# 🚀 Features

✅ Upload PDF Resume  
✅ Extract Resume Text  
✅ AI-Powered Resume Analysis  
✅ Gemini API Integration  
✅ Clean Streamlit UI  
✅ Real-Time AI Feedback  

---

# 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend Logic |
| Streamlit | Web Application UI |
| PyPDF2 | PDF Text Extraction |
| Google Gemini API | AI Analysis |
| python-dotenv | API Key Management |

---

# 📂 Project Structure

```text
ai-resume-analyzer/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md

⚙️ Installation
1️⃣ Clone Repository
git clone https://github.com/YOUR_USERNAME/ai-resume-analyzer.git
2️⃣ Navigate to Project Folder
cd ai-resume-analyzer
3️⃣ Create Virtual Environment
python -m venv .venv
.venv\Scripts\activate
4️⃣ Install Dependencies
pip install -r requirements.txt
🔑 Setup Gemini API Key
Create a .env file:
GEMINI_API_KEY=your_api_key_here
Get API key from:

https://aistudio.google.com/app/apikey

streamlit run app.py
Upload Resume PDF
        ↓
Extract Resume Text
        ↓
Generate AI Prompt
        ↓
Send to Gemini API
        ↓
Receive AI Analysis
        ↓
Display Results

📸 Application Output
Resume Upload
# 📸 Application Output

## Resume Upload

![Resume Upload](output1.png)

---

## AI Resume Analysis

![AI Analysis](output2.png)

AI Resume Analysis

🚀 Future Improvements
ATS Score Prediction
Resume vs Job Description Matching
Downloadable PDF Reports
OCR Support for Scanned PDFs
Advanced UI Improvements
RAG-based Resume Search

👨‍💻 Author

Gautam Sharma

GitHub:
https://github.com/Gautams1990

⭐ If you like this project

Give this repository a ⭐ on GitHub.
