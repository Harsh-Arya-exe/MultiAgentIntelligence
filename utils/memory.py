from typing import List, Dict
from datetime import datetime

class ConversationMemory:
    def __init__(self):
        self.messages = []
    
    def add_message(self, role: str, content: str, agent: str):
        """Add a message to the conversation history."""
        self.messages.append({
            "role": role,
            "content": content,
            "agent": agent,
            "timestamp": datetime.now().isoformat()
        })
    
    def get_recent_messages(self, limit: int = 10) -> List[Dict]:
        """Get the most recent messages."""
        return self.messages[-limit:]
    
    def clear(self):
        """Clear the conversation history."""
        self.messages = []
