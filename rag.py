from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from src.llm import get_llm

def get_rag_chain(vectorstore):
    """Creates RAG chain using Groq LLM and FAISS vector retriever."""
    llm = get_llm()
    retriever = vectorstore.as_retriever(search_kwargs={"k": 4})
    
    system_prompt = (
        "You are an AI University Assistant. Answer questions based ONLY on the provided "
        "university context. If the answer is not in the context, say that you don't have "
        "that specific information available.\n\n"
        "Context:\n{context}"
    )
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{input}"),
    ])
    
    question_answer_chain = create_stuff_documents_chain(llm, prompt)
    return create_retrieval_chain(retriever, question_answer_chain)
