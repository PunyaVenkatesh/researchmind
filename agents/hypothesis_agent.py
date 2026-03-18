import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

def run_hypothesis_agent(papers: list) -> dict:
    """
    Hypothesis Agent - extracts key findings, research gaps,
    and potential hypotheses from a set of papers.
    This is what makes ResearchMind unique for academic use.
    """
    print("Hypothesis Agent: Analysing papers for insights...")

    paper_summaries = ""
    for i, paper in enumerate(papers, 1):
        paper_summaries += "\nPaper " + str(i) + ": " + paper["title"] + "\n"
        paper_summaries += "Authors: " + ", ".join(paper["authors"]) + "\n"
        paper_summaries += "Abstract: " + paper["abstract"][:500] + "...\n"
        paper_summaries += "-" * 40 + "\n"

    prompt = (
        "You are an expert AI research analyst working with a professor at a top university.\n\n"
        "Analyse the following research papers and provide:\n\n"
        "1. KEY FINDINGS: The 3 most important discoveries across these papers\n"
        "2. RESEARCH GAPS: What questions remain unanswered? What is missing?\n"
        "3. HYPOTHESES: 3 novel research hypotheses that could be tested next\n"
        "4. CONNECTIONS: How do these papers relate to each other?\n\n"
        "Research Papers:\n"
        + paper_summaries +
        "\nProvide a structured, detailed analysis that would be useful for a research professor."
    )

    llm = ChatGroq(
        api_key=os.getenv("GROQ_API_KEY"),
        model_name="llama-3.3-70b-versatile",
        temperature=0.5
    )

    response = llm.invoke(prompt)

    return {
        "analysis": response.content,
        "paper_count": len(papers)
    }