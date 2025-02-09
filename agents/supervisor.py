from typing import Dict, List, Tuple
from langgraph.graph import StateGraph, MessageGraph
from langchain_core.messages import HumanMessage, AIMessage
from langchain_groq import ChatGroq

class SupervisorAgent:
    def __init__(self):
        self.llm = ChatGroq(model_name="Gemma2-9b-It")

    def analyze_query(self, query: str) -> str:
        """Determine which agent should handle the query."""
        prompt = f"""Analyze the following query and decide which agent should handle it:
        Query: {query}

        Available agents:
        1. RAG Agent - For specific topic knowledge from our database
        2. Quick Search Agent - For rapid information lookup and summaries
        3. Web Search Agent - For detailed web analysis and research

        Respond with only one of: 'rag', 'quick', or 'web'"""

        response = self.llm.invoke([HumanMessage(content=prompt)])
        return response.content.strip().lower()

def create_supervisor_graph():
    workflow = StateGraph(name="supervisor")

    # Add nodes
    workflow.add_node("analyze", SupervisorAgent().analyze_query)

    # Add edges
    workflow.add_conditional_edges(
        "analyze",
        lambda x: x,
        {
            "rag": "rag_agent",
            "quick": "quick_agent",
            "web": "web_agent"
        }
    )

    workflow.set_entry_point("analyze")
    return workflow