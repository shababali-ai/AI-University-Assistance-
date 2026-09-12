import os
from langchain_community.vectorstores import FAISS
from src.embeddings import get_embedding_model

INDEX_PATH = "faiss_index"

def build_or_load_vectorstore(docs):
    """Builds a new FAISS vector database or loads an existing one."""
    embeddings = get_embedding_model()
    
    if os.path.exists(INDEX_PATH):
        return FAISS.load_local(INDEX_PATH, embeddings, allow_dangerous_deserialization=True)
    
    if docs:
        vectorstore = FAISS.from_documents(docs, embeddings)
        vectorstore.save_local(INDEX_PATH)
        return vectorstore
        
    return None
