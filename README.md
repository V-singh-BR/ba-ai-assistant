# 🤖 AI Business Analyst Assistant

An AI-powered Business Analyst Assistant built with **FastAPI**, **Python**, and **Large Language Models (LLMs)**. This project automates common Business Analyst tasks such as meeting summarization, BRD generation, FRD creation, user stories, acceptance criteria, and document automation.

---

## 🚀 Current Features

- ✅ FastAPI Backend
- ✅ Swagger API Documentation
- ✅ Health Check API
- ✅ File Upload API
- ⏳ Text Extraction (TXT, PDF, DOCX)
- ⏳ AI Meeting Summarization
- ⏳ BRD Generator
- ⏳ FRD Generator
- ⏳ User Story Generator
- ⏳ Acceptance Criteria Generator

---

## 🛠 Tech Stack

- Python 3.13
- FastAPI
- Uvicorn
- Git & GitHub

---

## 📂 Project Structure

```text
AI-MEETING-SUMMARIZER
│
├── app
│   ├── main.py
│   ├── routers
│   ├── services
│   └── utils
│
├── uploads
├── requirements.txt
├── README.md
└── .gitignore
```

## ▶️ Run the Project

Clone the repository:

```bash
git clone https://github.com/V-singh-BR/ba-ai-assistant.git
```

Go to the project:

```bash
cd ba-ai-assistant
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it (Windows):

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
uvicorn app.main:app --reload
```

Open Swagger:

```
http://127.0.0.1:8000/docs
```

---

## 📅 Roadmap

### Phase 1
- ✅ FastAPI Setup
- ✅ File Upload API
- ⏳ Read TXT Files
- ⏳ Read PDF Files
- ⏳ Read DOCX Files

### Phase 2
- ⏳ AI Meeting Summarizer
- ⏳ Action Items
- ⏳ MOM Generator

### Phase 3
- ⏳ BRD Generator
- ⏳ FRD Generator
- ⏳ User Story Generator
- ⏳ Acceptance Criteria Generator

### Phase 4
- ⏳ React Frontend
- ⏳ Authentication
- ⏳ Docker Deployment

---

## 👨‍💻 Author

**Vaibhav Singh**

GitHub: https://github.com/V-singh-BR