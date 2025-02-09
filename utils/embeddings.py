from langchain_community.embeddings import HuggingFaceEmbeddings

def get_embeddings():
    """Initialize and return the embeddings model."""
    return HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
