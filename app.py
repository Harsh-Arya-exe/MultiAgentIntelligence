import streamlit as st
from agents.supervisor import SupervisorAgent
from agents.search_agents import QuickSearchAgent, WebSearchAgent
from agents.rag_agent import RAGAgent
from utils.memory import ConversationMemory

# Initialize session state
if 'memory' not in st.session_state:
    st.session_state.memory = ConversationMemory()
if 'agents' not in st.session_state:
    st.session_state.agents = {
        'supervisor': SupervisorAgent(),
        'quick': QuickSearchAgent(),
        'web': WebSearchAgent(),
        'rag': RAGAgent()
    }

st.title("Multi-Agent Chatbot")
st.markdown("""
    This chatbot uses multiple specialized agents to answer your questions:
    - RAG Agent: For specific topic knowledge
    - Quick Search Agent: For rapid information lookup
    - Web Search Agent: For detailed analysis and research
""")

# Chat interface
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(f"**Agent: {message['agent']}**")
        st.write(message["content"])

# Chat input
if prompt := st.chat_input("What would you like to know?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt, "agent": "user"})
    with st.chat_message("user"):
        st.write(prompt)

    # Process with supervisor
    with st.spinner("Thinking..."):
        # Get agent selection from supervisor
        selected_agent = st.session_state.agents['supervisor'].analyze_query(prompt)

        # Get response from selected agent with memory context
        if selected_agent == 'rag':
            response = st.session_state.agents['rag'].query(prompt, memory=st.session_state.memory)
        elif selected_agent == 'quick':
            response = st.session_state.agents['quick'].search_and_summarize(prompt, memory=st.session_state.memory)
        else:  # web
            response = st.session_state.agents['web'].search_and_analyze(prompt, memory=st.session_state.memory)

        # Display assistant response
        with st.chat_message("assistant"):
            st.markdown(f"**Agent: {selected_agent}**")
            st.write(response)

        # Add assistant response to chat history
        st.session_state.messages.append({
            "role": "assistant",
            "content": response,
            "agent": selected_agent
        })

        # Add to conversation memory
        st.session_state.memory.add_message("user", prompt, "user")
        st.session_state.memory.add_message("assistant", response, selected_agent)

# Sidebar with conversation memory
with st.sidebar:
    st.header("Conversation Memory")
    recent_messages = st.session_state.memory.get_recent_messages()
    for msg in recent_messages:
        st.text(f"{msg['role']} ({msg['agent']})")
        st.text(msg['content'][:100] + "..." if len(msg['content']) > 100 else msg['content'])
        st.text("---")