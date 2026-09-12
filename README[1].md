# AI University Assistant 🎓

An interactive Retrieval-Augmented Generation (RAG) assistant built with Streamlit, LangChain, FAISS, and Groq API.

## Project Structure
```
AI-University-Assistant
├── app.py                 # Main Streamlit app
├── requirements.txt       # Dependencies
├── README.md
├── .gitignore
├── .env.example           # Environment template
├── src/                   # RAG logic modules
├── pages/                 # Multi-page Streamlit views
├── data/documents/        # Input PDFs directory
└── notebooks/             # Google Colab experimentation
```

## Quick Start
1. Create virtual env: `python -m venv .venv && source .venv/bin/activate` (or `.venv\Scripts\activate` on Windows)
2. Install packages: `pip install -r requirements.txt`
3. Set Groq key in `.env`: `GROQ_API_KEY=your_key`
4. Add university PDF documents to `data/documents/`
5. Launch app: `streamlit run app.py`
