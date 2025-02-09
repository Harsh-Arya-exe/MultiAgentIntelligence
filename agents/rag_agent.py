from langchain_core.documents import Document
from langchain_groq import ChatGroq
from typing import List, Dict
import numpy as np
from difflib import SequenceMatcher

class RAGAgent:
    def __init__(self):
        self.llm = ChatGroq(model_name="Gemma2-9b-It")
        self.documents = []
        self.initialize_documents()

    def initialize_documents(self):
        """Initialize with knowledge base documents."""
        from data.knowledge_base import get_documents
        self.documents = get_documents()

    def similarity_score(self, text1: str, text2: str) -> float:
        """Calculate text similarity using SequenceMatcher."""
        return SequenceMatcher(None, text1.lower(), text2.lower()).ratio()

    def query(self, question: str) -> str:
        # Find relevant documents using simple text similarity
        similarities = [
            (doc, self.similarity_score(question, doc.page_content))
            for doc in self.documents
        ]

        # Get top 3 most similar documents
        relevant_docs = sorted(similarities, key=lambda x: x[1], reverse=True)[:3]
        context = "\n".join([doc[0].page_content for doc in relevant_docs])

        prompt = f"""Using the following context, answer the question:

        Context:
        {context}

        Question: {question}

        Provide a detailed answer based on the context provided."""

        response = self.llm.invoke(prompt)
        return response.content