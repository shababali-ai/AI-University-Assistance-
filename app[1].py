import streamlit as st
import os
from dotenv import load_dotenv
from src.document_loader import load_and_split_documents
from src.vectorstore import build_or_load_vectorstore
from src.rag import get_rag_chain

load_dotenv()

st.set_page_config(page_title="AI University Assistant", page_icon="🎓", layout="wide")

st.title("🎓 AI University Assistant")
st.subheader("Your AI Guide for University Admissions, Academics, Fees, and Scholarships")

@st.cache_resource
def initialize_system():
    docs = load_and_split_documents()
    vectorstore = build_or_load_vectorstore(docs)
    return vectorstore

try:
    vectorstore = initialize_system()
    
    if vectorstore is None:
        st.warning("⚠️ No documents found in `data/documents/`. Please add university PDF files and restart the app.")
    else:
        rag_chain = get_rag_chain(vectorstore)
        
        st.write("---")
        query = st.text_input("Ask any question about university policies, courses, or procedures:")
        
        if query:
            with st.spinner("Searching documents..."):
                response = rag_chain.invoke({"input": query})
                st.markdown("### Answer:")
                st.write(response["answer"])
                
                with st.expander("View Source Context"):
                    for i, doc in enumerate(response["context"]):
                        st.markdown(f"**Source {i+1}:** {doc.metadata.get('source', 'Unknown')}")
                        st.caption(doc.page_content)
except Exception as e:
    st.error(f"Error initializing assistant: {str(e)}")
