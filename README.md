# Multi-Agent Chatbot System

A sophisticated chatbot system built with LangGraph and Streamlit that combines RAG capabilities, web search, and conversation memory.

## Features

- **Multiple Specialized Agents:**
  - RAG Agent: Handles knowledge base queries
  - Quick Search Agent: For rapid information lookup
  - Web Search Agent: For detailed web research
  - Supervisor Agent: Routes queries to appropriate agents

- **Smart Conversation Memory:** Maintains context across interactions
- **Interactive Web Interface:** Built with Streamlit
- **Visual Workflow:** Graphical representation of the agent system

## Setup Instructions

1. Clone the repository:
```bash
git clone <your-repository-url>
cd multi-agent-chatbot
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
Create a `.env` file with the following:
```
TAVILY_API_KEY=your_tavily_api_key
GROQ_API_KEY=your_groq_api_key
```

4. Run the application:
```bash
streamlit run app.py
```

5. View the workflow visualization:
```bash
streamlit run workflow_graph.py
```

## Project Structure

```
├── .streamlit/
│   └── config.toml
├── agents/
│   ├── supervisor.py
│   ├── rag_agent.py
│   └── search_agents.py
├── data/
│   └── knowledge_base.py
├── utils/
│   ├── memory.py
│   └── embeddings.py
├── app.py
└── workflow_graph.py
```

## Usage

1. Start the main application and workflow visualization
2. Enter your query in the chat interface
3. The system will automatically:
   - Analyze your query
   - Route it to the most appropriate agent
   - Provide a response while maintaining conversation context

## Dependencies

- streamlit
- langgraph
- langchain-groq
- langchain-community
- langchain-core
- tavily-python
- graphviz
- trafilatura

## License

MIT License
