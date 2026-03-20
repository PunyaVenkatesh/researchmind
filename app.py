import streamlit as st
from dotenv import load_dotenv
from agents.fetcher_agent import run_fetcher_agent
from agents.rag_agent import run_rag_agent
from agents.hypothesis_agent import run_hypothesis_agent
from core.vectorstore import build_vectorstore

load_dotenv()

# Page config
st.set_page_config(
    page_title="ResearchMind",
    page_icon="🔬",
    layout="wide"
)

# Header
st.title("ResearchMind")
st.markdown("#### An Agentic AI Assistant for Scientific Discovery")
st.markdown("---")

# Session state to store papers and vectorstore
if "papers" not in st.session_state:
    st.session_state.papers = []
if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None
if "hypothesis" not in st.session_state:
    st.session_state.hypothesis = None

# Sidebar
with st.sidebar:
    st.header("Search Research Papers")
    topic = st.text_input("Enter a research topic", placeholder="e.g. large language models")
    max_results = st.slider("Number of papers", min_value=3, max_value=100, value=5)
    search_btn = st.button("Search arxiv", use_container_width=True)

    if search_btn and topic:
        with st.spinner("Fetching papers from arxiv..."):
            papers = run_fetcher_agent(topic, max_results)
            vectorstore = build_vectorstore(papers)
            st.session_state.papers = papers
            st.session_state.vectorstore = vectorstore
            st.session_state.hypothesis = None
        st.success(str(len(papers)) + " papers loaded!")

# Main content
if st.session_state.papers:
    
    # Tabs
    tab1, tab2, tab3 = st.tabs([
        "Papers Found",
        "Ask a Question",
        "Hypothesis Analysis"
    ])

    # Tab 1 - Papers
    with tab1:
        st.subheader("Papers Retrieved from arxiv")
        for i, paper in enumerate(st.session_state.papers, 1):
            with st.expander(str(i) + ". " + paper["title"]):
                st.markdown("**Authors:** " + ", ".join(paper["authors"]))
                st.markdown("**Published:** " + paper["published"])
                st.markdown("**Abstract:**")
                st.write(paper["abstract"])
                st.markdown("[View on arxiv](" + paper["url"] + ")")

    # Tab 2 - RAG Q&A
    with tab2:
        st.subheader("Ask Questions About These Papers")
        question = st.text_input(
            "Enter your research question",
            placeholder="e.g. What are the main challenges in LLM alignment?"
        )
        ask_btn = st.button("Get Answer", use_container_width=True)

        if ask_btn and question:
            with st.spinner("Searching papers and generating answer..."):
                result = run_rag_agent(st.session_state.vectorstore, question)

            st.markdown("### Answer")
            st.write(result["answer"])

            st.markdown("### Sources Used")
            for source in result["sources"]:
                st.markdown("- **" + source["title"] + "** — " + source["authors"])
                st.markdown("  [View Paper](" + source["url"] + ")")

    # Tab 3 - Hypothesis
    with tab3:
        st.subheader("AI Research Analysis")
        st.markdown("Extracts key findings, research gaps and novel hypotheses from the papers.")

        analyse_btn = st.button("Run Hypothesis Analysis", use_container_width=True)

        if analyse_btn:
            with st.spinner("Analysing papers for insights..."):
                result = run_hypothesis_agent(st.session_state.papers)
                st.session_state.hypothesis = result

        if st.session_state.hypothesis:
            st.markdown("### Analysis Results")
            st.write(st.session_state.hypothesis["analysis"])
            st.info("Analysis based on " + str(st.session_state.hypothesis["paper_count"]) + " papers.")

else:
    # Empty state
    st.markdown("###")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("Step 1: Enter a research topic in the sidebar")
    with col2:
        st.info("Step 2: Click Search to fetch papers from arxiv")
    with col3:
        st.info("Step 3: Ask questions or run hypothesis analysis")