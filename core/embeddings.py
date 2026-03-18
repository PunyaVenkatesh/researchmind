from langchain_community.embeddings import HuggingFaceEmbeddings

def get_embeddings():
    """
    Load HuggingFace sentence-transformers embeddings.
    Free, no API key needed, runs locally.
    """
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": True}
    )
    return embeddings