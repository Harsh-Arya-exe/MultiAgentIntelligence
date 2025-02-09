from langchain_core.documents import Document
from typing import List

def get_documents() -> List[Document]:
    """Return a list of documents for the knowledge base."""
    # Example documents about AI and Machine Learning
    documents = [
        Document(
            page_content="Machine Learning is a subset of artificial intelligence that provides systems the ability to automatically learn and improve from experience without being explicitly programmed.",
            metadata={"source": "AI basics", "topic": "machine_learning"}
        ),
        Document(
            page_content="Deep Learning is part of a broader family of machine learning methods based on artificial neural networks with representation learning.",
            metadata={"source": "AI basics", "topic": "deep_learning"}
        ),
        Document(
            page_content="Natural Language Processing (NLP) is a branch of artificial intelligence that helps computers understand, interpret and manipulate human language.",
            metadata={"source": "AI basics", "topic": "nlp"}
        )
    ]
    return documents
