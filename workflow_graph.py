import streamlit as st
import graphviz

# Create a directed graph
graph = graphviz.Digraph()
graph.attr(rankdir='TB')

# Add nodes
graph.node('User Input', 'User Query', shape='ellipse')
graph.node('Supervisor', 'Supervisor Agent\nQuery Analysis', shape='diamond')
graph.node('RAG', 'RAG Agent\nKnowledge Base', shape='box')
graph.node('Quick', 'Quick Search Agent\nBasic Information', shape='box')
graph.node('Web', 'Web Search Agent\nDetailed Research', shape='box')
graph.node('Memory', 'Conversation Memory', shape='cylinder')

# Add edges with labels
graph.edge('User Input', 'Supervisor')
graph.edge('Supervisor', 'RAG', 'Knowledge Base Query')
graph.edge('Supervisor', 'Quick', 'Basic Information')
graph.edge('Supervisor', 'Web', 'Complex Research')

# Memory connections
graph.edge('Memory', 'RAG', 'Context')
graph.edge('Memory', 'Quick', 'Context')
graph.edge('Memory', 'Web', 'Context')
graph.edge('RAG', 'Memory', 'Store')
graph.edge('Quick', 'Memory', 'Store')
graph.edge('Web', 'Memory', 'Store')

# Display the graph
st.title('Multi-Agent Chatbot Workflow')
st.graphviz_chart(graph)

# Add explanation
st.markdown("""
### Workflow Explanation:

1. **User Input**: The process starts when a user submits a query.

2. **Supervisor Agent**:
   - Analyzes the query using LLM
   - Determines which specialized agent is best suited to handle it
   - Routes the query to the appropriate agent

3. **Specialized Agents**:
   - **RAG Agent**: Handles queries about specific topics in our knowledge base
   - **Quick Search Agent**: Provides rapid information lookup and basic answers
   - **Web Search Agent**: Performs detailed web research and analysis

4. **Conversation Memory**:
   - Maintains context of the conversation
   - Provides relevant history to agents for contextual understanding
   - Stores responses for future reference

### Routing Logic:
- Knowledge base queries → RAG Agent
- Simple factual queries → Quick Search Agent
- Complex research queries → Web Search Agent
""")
