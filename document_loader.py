import os
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_and_split_documents(data_dir: str = "data/documents"):
    """Loads PDF documents from directory and splits them into chunks."""
    if not os.path.exists(data_dir) or not os.listdir(data_dir):
        return []
    
    loader = PyPDFDirectoryLoader(data_dir)
    documents = loader.load()
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150
    )
    return text_splitter.split_documents(documents)
