import arxiv
import fitz  # PyMuPDF
import os

def fetch_papers_from_arxiv(query: str, max_results: int = 5) -> list[dict]:
    """
    Fetch papers from arxiv based on a search query.
    Returns a list of dicts with title, abstract, authors, url, and pdf_url.
    """
    client = arxiv.Client()
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.Relevance
    )

    papers = []
    for result in client.results(search):
        papers.append({
            "title": result.title,
            "abstract": result.summary,
            "authors": [str(a) for a in result.authors],
            "url": result.entry_id,
            "pdf_url": result.pdf_url,
            "published": str(result.published.date())
        })

    return papers


def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extract full text from a PDF file using PyMuPDF.
    """
    doc = fitz.open(pdf_path)
    full_text = ""
    for page in doc:
        full_text += page.get_text()
    doc.close()
    return full_text


def clean_text(text: str) -> str:
    """
    Basic text cleaning — remove excessive whitespace and empty lines.
    """
    lines = text.splitlines()
    cleaned = [line.strip() for line in lines if line.strip()]
    return "\n".join(cleaned)