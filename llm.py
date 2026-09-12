import os
from langchain_groq import ChatGroq

def get_llm():
    """Initializes the Groq LLM model."""
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY is not set in environment variables.")
    
    return ChatGroq(
        groq_api_key=api_key,
        model_name="llama-3.1-70b-versatile",
        temperature=0.2
    )
