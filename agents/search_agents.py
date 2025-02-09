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
        # Get recent context if available
        context = ""
        if memory:
            recent_msgs = memory.get_recent_messages(3)  # Get last 3 messages
            if recent_msgs:
                context = "\n".join([f"{msg['role']}: {msg['content']}" for msg in recent_msgs])

        search_results = self.search.search(query, search_depth="advanced")
        formatted_results = "\n".join([f"- {result['title']}: {result['content']}" 
                                     for result in search_results['results']])

        prompt = f"""Given the following conversation context and search results, provide a detailed answer:

        Previous conversation:
        {context}

        Current question: {query}

        Search results:
        {formatted_results}

        Provide a comprehensive analysis that takes into account both the conversation history and the search results."""

        response = self.llm.invoke([HumanMessage(content=prompt)])
        return response.content

class QuickSearchAgent:
    """A quick search agent for basic information retrieval"""
    def __init__(self):
        self.search = TavilyClient()
        self.llm = ChatGroq(model_name="Gemma2-9b-It")

    def search_and_summarize(self, query: str, memory=None) -> str:
        # Get recent context if available
        context = ""
        if memory:
            recent_msgs = memory.get_recent_messages(3)  # Get last 3 messages
            if recent_msgs:
                context = "\n".join([f"{msg['role']}: {msg['content']}" for msg in recent_msgs])

        search_results = self.search.search(query, search_depth="basic")
        formatted_results = "\n".join([f"- {result['title']}: {result['content']}" 
                                     for result in search_results['results']])

        prompt = f"""Given the following conversation context and search results, provide a concise answer:

        Previous conversation:
        {context}

        Current question: {query}

        Search results:
        {formatted_results}

        Provide a focused response that considers both the conversation history and search results."""

        response = self.llm.invoke([HumanMessage(content=prompt)])
        return response.content