from tavily import TavilyClient
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from typing import Dict, List

class WebSearchAgent:
    """A web search agent that uses Tavily for comprehensive search"""
    def __init__(self):
        self.search = TavilyClient()
        self.llm = ChatGroq(model_name="Gemma2-9b-It")

    def search_and_analyze(self, query: str) -> str:
        search_results = self.search.search(query, search_depth="advanced")
        formatted_results = "\n".join([f"- {result['title']}: {result['content']}" 
                                     for result in search_results['results']])

        prompt = f"""Analyze these search results and provide detailed insights:
        {formatted_results}

        Consider multiple perspectives and provide a comprehensive analysis for the query: {query}"""

        response = self.llm.invoke([HumanMessage(content=prompt)])
        return response.content

class QuickSearchAgent:
    """A quick search agent for basic information retrieval"""
    def __init__(self):
        self.search = TavilyClient()
        self.llm = ChatGroq(model_name="Gemma2-9b-It")

    def search_and_summarize(self, query: str) -> str:
        search_results = self.search.search(query, search_depth="basic")
        formatted_results = "\n".join([f"- {result['title']}: {result['content']}" 
                                     for result in search_results['results']])

        prompt = f"""Summarize these search results concisely:
        {formatted_results}

        Focus on the most relevant information for the query: {query}"""

        response = self.llm.invoke([HumanMessage(content=prompt)])
        return response.content