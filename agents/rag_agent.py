import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from core.vectorstore import search_vectorstore

load_dotenv()

def run_rag_agent(vectorstore, question: str) -> dict:
    print("RAG Agent: Answering '" + question + "'...")

    relevant_docs = search_vectorstore(vectorstore, question, k=3)

    context = ""
    sources = []
    for doc in relevant_docs:
        context += "Paper: " + doc.metadata["title"] + "\n"
        context += "Authors: " + doc.metadata["authors"] + "\n"
        context += "Content: " + doc.page_content + "\n"
        context += "-" * 50 + "\n"
        sources.append({
            "title": doc.metadata["title"],
            "authors": doc.metadata["authors"],
            "url": doc.metadata["url"],
            "published": doc.metadata["published"]
        })

    prompt = (
        "You are an expert AI research assistant helping academics understand research papers.\n\n"
        "Based on the following research papers, answer the question clearly and accurately.\n"
        "Always cite which paper(s) you are drawing from in your answer.\n\n"
        "Research Papers:\n"
        + context +
        "\nQuestion: " + question +
        "\n\nProvide a detailed, well-structured answer with citations."
    )

    llm = ChatGroq(
        api_key=os.getenv("GROQ_API_KEY"),
        model_name="llama-3.3-70b-versatile",
        temperature=0.3
    )

    response = llm.invoke(prompt)

    return {
        "answer": response.content,
        "sources": sources
    }