# 🌿 Healthy Habit Tracker Backend

This is the backend for the Healthy Habit Tracker — an AI-powered habit planning and motivational system built with **FastAPI**, **CrewAI**, and **MongoDB**. It provides API endpoints for generating healthy habit plans, logging daily activity, and receiving motivational messages.

---

## ⚙️ Tech Stack

- 🐍 Python 3.11+
- ⚡ FastAPI
- 🧠 CrewAI + LangChain + OpenAI (GPT-4o)
- ☁️ MongoDB (via `motor`)

---

## 🧠 AI Agents

- **Habit Coach Agent** – Generates personalized 7-day healthy habit plans
- **Mindfulness Mentor Agent** – Delivers daily motivational messages
- _(Optional)_ Progress Analyst Agent – Analyzes habit logs (coming later)

---

## 📦 Installation & Setup

### 1. Clone the repo

```bash
git clone https://github.com/yourname/healthy-habit-backend.git
cd healthy-habit-backend

python -m venv venv
# Activate it:
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
pip install -r requirements.txt
```


## ⚙️ Setup Environement
Create a .env file in the root with the following:

OPENAI_API_KEY=your_openai_key_here
MONGO_URI=mongodb://localhost:27017
CORS_ORIGINS=http://localhost:5173


## ⚙️ Run Server
```bash
python run.py
```