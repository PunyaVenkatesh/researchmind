from utils.paper_parser import fetch_papers_from_arxiv, clean_text

def run_fetcher_agent(topic: str, max_results: int = 5) -> list[dict]:
    """
    Fetcher Agent — searches arxiv and returns clean paper data.
    This is the first agent in the pipeline.
    """
    print(f"🔍 Fetcher Agent: Searching arxiv for '{topic}'...")
    
    papers = fetch_papers_from_arxiv(topic, max_results)
    
    # Clean the abstracts
    for paper in papers:
        paper["abstract"] = clean_text(paper["abstract"])
    
    print(f"✅ Fetcher Agent: Found {len(papers)} papers.")
    return papers