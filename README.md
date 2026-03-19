---
title: ResearchMind
emoji: 🔬
colorFrom: blue
colorTo: indigo
sdk: streamlit
sdk_version: 1.55.0
app_file: app.py
pinned: false
---

# ResearchMind — Agentic AI Assistant for Scientific Discovery

An agentic AI system that helps researchers explore academic literature, 
ask questions with cited answers, and discover novel research hypotheses.
Built with LangChain, Groq LLaMA 3, FAISS, and Streamlit.

---

## What It Does

- Fetches real research papers live from arxiv based on any topic
- Answers research questions with citations from retrieved papers
- Extracts key findings, research gaps and novel hypotheses using AI
- Connects related papers and maps the research landscape

---

## Architecture
```
User Query
    │
    ▼
Fetcher Agent ──► arxiv API ──► 5-10 Real Papers
    │
    ▼
Vector Store (FAISS + HuggingFace Embeddings)
    │
    ├──► RAG Agent ──► Groq LLaMA 3 ──► Cited Answer
    │
    └──► Hypothesis Agent ──► Key Findings + Research Gaps + Novel Hypotheses
```

---

## Tech Stack

| Tool | Purpose |
|---|---|
| LangChain | Agent orchestration and RAG pipeline |
| Groq LLaMA 3.3 70B | Fast, free, powerful LLM |
| FAISS | Vector similarity search |
| HuggingFace Embeddings | Local sentence embeddings |
| arxiv API | Live research paper retrieval |
| Streamlit | Interactive web interface |

---

## Run Locally
```bash
git clone https://github.com/PunyaVenkatesh/researchmind.git
cd researchmind
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Create a `.env` file:
```
GROQ_API_KEY=your_groq_api_key_here
```

Run the app:
```bash
streamlit run app.py
```

---

## Inspired By

This project is inspired by the LLM4SD research at Monash University,
which uses LLMs to simulate scientific discovery workflows.

---

## Author

Punya Venkatesh — Masters of AI, Monash University (2026)

[LinkedIn](https://linkedin.com/in/yourprofile) | [GitHub](https://github.com/PunyaVenkatesh)