from langchain_community.embeddings import HuggingFaceEmbeddings

def get_embedding_model():
    """Initializes HuggingFace Sentence Transformers for embeddings."""
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
