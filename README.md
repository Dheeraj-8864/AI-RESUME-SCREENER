🧠 ATS Resume Scorer – AI-Powered Resume Evaluation using Gemini API

ATS Resume Scorer is an AI-driven Applicant Tracking System that evaluates resumes against job descriptions using Google Gemini API.
It provides match scores, keyword insights, and personalized recommendations, helping candidates optimize their resumes for better hiring outcomes.

📈 Features

✅ Gemini-Powered Resume Evaluation
✅ Automatic Match Scoring & Keyword Extraction
✅ AI-Generated Resume Improvement Tips
✅ Interactive Streamlit Dashboard
✅ Instant Accept/Reject Suggestions

🛠️ Tech Stack
| **Category** |	**Technology** |
|--------------|-----------------|
|🧠 AI Model |	Google Gemini API |
|💻 Frontend/UI |	Streamlit |
|📄 File Parsing |	PyPDF2  pdfminer |
|🧰 Backend Logic |	Python|
📊 Data Handling	Pandas| JSON |

 ---
## **🚀 Setup & Installation**
###1️⃣ Clone the Repository**
```sh
git clone https://github.com/Dheeraj-8864/AI-RESUME-SCREENER/edit/main/README.md
--- 

## **2️⃣ Create Virtual Environment (Optional)**
python -m venv venv
source venv/bin/activate    # for Linux/Mac
venv\Scripts\activate       # for Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Setup Environment Variables

Create a .env file in the project root and add:

GEMINI_API_KEY=your-gemini-api-key

5️⃣ Run the Application
streamlit run app.py

Keyword Extraction	Suggestions & Feedback

	
🧠 API Workflow
Step	Description
🧾 Resume Parsing	Extracts text & metadata from uploaded PDF
🧩 Job Description Analysis	Identifies key roles, skills & keywords
🤖 Gemini API Call	Sends structured prompt (Resume + JD) to Gemini Pro
📊 Response Processing	Extracts match score, missing keywords & suggestions
💡 Display Insights	Shows all insights neatly in Streamlit UI
📀 Example Request
POST /api/score-resume
{
  "resume_text": "Software Engineer with 3 years of experience in React and Python",
  "job_description": "Looking for a full-stack developer skilled in React, Node.js, and cloud deployment"
}

📀 Example Response
{
  "match_score": 82,
  "missing_keywords": ["Node.js", "Cloud Deployment"],
  "recommendations": "Add experience with backend APIs and mention cloud deployment experience."
}

## **🙏 Contributing**
💪 Want to improve Nutshell?  
1. **Fork the repo**  
2. **Create a new branch** (`git checkout -b feature-branch`)  
3. **Commit changes** (`git commit -m "Added new feature"`)  
4. **Push to GitHub** (`git push origin feature-branch`)  
5. **Create a Pull Request** 🎉  
---

## **📩 Contact**
👤 **Attuluri Dheeraj**  
📧 [dheerajattuluri8466@gmail.com]
💼 LinkedIn: [Attuluri Dheeraj](https://www.linkedin.com/in/dheeraj-attuluri-841486335/)  
