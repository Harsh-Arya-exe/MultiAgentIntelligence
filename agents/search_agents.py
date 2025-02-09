from tavily import TavilyClient
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from typing import Dict, List

class WebSearchAgent:
    """A web search agent that uses Tavily for comprehensive search"""
    def __init__(self):
        self.search = TavilyClient()
        self.llm = ChatGroq(model_name="Gemma2-9b-It")

    def search_and_analyze(self, query: str, memory=None) -> str:
        # Build context from memory
        context = ""
        context_query = query
        if memory:
            recent_msgs = memory.get_recent_messages(3)
            if recent_msgs:
                # Build context string
                context = "\n".join([f"{msg['role']}: {msg['content']}" for msg in recent_msgs])
                # Enhance search query with context
                context_entities = [msg['content'] for msg in recent_msgs if msg['role'] == "user"][-2:]
                context_query = f"{' '.join(context_entities)} {query}"

        # Use advanced search with context-aware query
        search_results = self.search.search(
            context_query,
            search_depth="advanced",
            max_results=5,
            include_answer=True,
            include_domains=["wikipedia.org", "forbes.com", "techcrunch.com", "reuters.com"]
        )

        formatted_results = "\n".join([
            f"- {result['title']}: {result['content']}" 
            for result in search_results['results']
        ])

        prompt = f"""Given the following conversation context and search results, provide a detailed answer:

        Previous conversation:
        {context}

        Current question: {query}

        Search results:
        {formatted_results}

        Direct answer from search: {search_results.get('answer', '')}

        Instructions:
        1. If this is a follow-up question, connect it with the previous context
        2. Look for specific facts and numbers in the search results
        3. If asked about a person's attribute (age, position, etc), focus on finding that specific information
        4. Provide the most up-to-date information available
        5. If information is not found in the results, clearly state that

        Provide a comprehensive analysis that takes into account both the conversation history and the search results."""

        response = self.llm.invoke([HumanMessage(content=prompt)])
        return response.content

class QuickSearchAgent:
    """A quick search agent for basic information retrieval"""
    def __init__(self):
        self.search = TavilyClient()
        self.llm = ChatGroq(model_name="Gemma2-9b-It")

    def search_and_summarize(self, query: str, memory=None) -> str:
        # Build context from memory
        context = ""
        context_query = query
        if memory:
            recent_msgs = memory.get_recent_messages(3)
            if recent_msgs:
                # Build context string
                context = "\n".join([f"{msg['role']}: {msg['content']}" for msg in recent_msgs])
                # Enhance search query with context
                context_entities = [msg['content'] for msg in recent_msgs if msg['role'] == "user"][-2:]
                context_query = f"{' '.join(context_entities)} {query}"

        # Use basic search with context-aware query
        search_results = self.search.search(
            context_query,
            search_depth="basic",
            max_results=3,
            include_answer=True
        )

        formatted_results = "\n".join([
            f"- {result['title']}: {result['content']}" 
            for result in search_results['results']
        ])

        prompt = f"""Given the following conversation context and search results, provide a concise answer:

        Previous conversation:
        {context}

        Current question: {query}

        Search results:
        {formatted_results}

        Direct answer from search: {search_results.get('answer', '')}

        Instructions:
        1. Focus on answering the current question using context from the conversation
        2. For follow-up questions, maintain continuity with previous topics
        3. Provide specific facts when available
        4. Be clear if information is not found in the search results

        Provide a focused response that considers both the conversation history and search results."""

        response = self.llm.invoke([HumanMessage(content=prompt)])
        return response.content