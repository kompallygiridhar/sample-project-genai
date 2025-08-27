# 🚀 Sample Project GenAI

An AI Agent project powered by **LangChain**, **Groq LLMs**, and **MCP tools** with RAG (Retrieval Augmented Generation) support.

---

## 📦 Prerequisites

- Python **3.12**
- [uv](https://github.com/astral-sh/uv) (for dependency + venv management)
- Git

---

## ⚙️ Setup

Follow these steps carefully 👇

### 1️⃣ Clone the repository
```bash
git clone https://github.com/kompallygiridhar/sample-project-genai.git
cd sample-project-genai

2️⃣ Create .env file

In the project root, create a file named .env and add your Groq API key:

GROQ_API_KEY=your_api_key_here


3️⃣ Install uv (if not installed)
pip install uv

4️⃣ Install dependencies & setup virtual environment
uv sync

This will:

Create a virtual environment (default: .venv)

Install all dependencies from pyproject.toml

5️⃣ Activate the environment

Linux / Mac

source .venv/bin/activate


Windows (PowerShell)

.venv\Scripts\Activate.ps1

6️⃣ Run the app
python app.py


You should see:

🤖 AI Agent + RAG (multi-file) is ready! Type 'exit' to quit.
