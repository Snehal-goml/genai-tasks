import requests
from typing import Dict, Any

from personalities import VYRA_BASE, SRK_STYLE, RANVEER_STYLE


class VyraAgent:
    """
    VYRA Agent - Simple but smart AI assistant
    Automatically chooses between SRK and Ranveer speaking styles
    """
    
    def __init__(self):
        self.model = "llama3.2:3b"
        self.url = "http://localhost:11434/api/generate"
    
    def ask_model(self, prompt):
        """Send prompt to AI model and get response"""
        response = requests.post(
            self.url,
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False
            },
            timeout=120
        )
        response.raise_for_status()
        return response.json()["response"]
    
    def choose_style(self, user_input, history):
        """
        Decide which style to use: SRK or Ranveer
        Based on: explicit mentions, conversation context, keywords
        """
        lower = user_input.lower()
        
        # Check if user explicitly asked for a style
        if "srk" in lower or "shah rukh" in lower:
            return "SRK"
        if "ranveer" in lower:
            return "RANVEER"
        
        # Look at recent messages to maintain style
        if history:
            recent = history[-3:]
            srk_count = sum(1 for m in recent if m.get("style") == "SRK")
            if srk_count > len(recent) - srk_count:
                return "SRK"
        
        # Check message content for style hints
        energetic = ["motivation", "gym", "hype", "energy", "confidence", 
                     "excited", "lets go", "pump", "strong"]
        calm = ["think", "feel", "life", "meaning", "advice", 
                "understand", "wisdom", "philosophy"]
        
        if any(kw in lower for kw in energetic):
            return "RANVEER"
        if any(kw in lower for kw in calm):
            return "SRK"
        
        return "SRK"  # Default to thoughtful SRK style
    
    def respond(self, user_input, history):
        """
        Main method: Generate response in SRK or Ranveer style
        
        Process:
        1. Choose appropriate style
        2. Get style-specific prompt
        3. Build conversation context
        4. Send to AI model
        5. Return response with style info
        """
        # Step 1: Choose style
        style = self.choose_style(user_input, history)
        
        # Step 2: Get style instructions
        style_prompt = SRK_STYLE if style == "SRK" else RANVEER_STYLE
        
        # Step 3: Build conversation history (last 8 messages)
        history_text = ""
        for msg in history[-8:]:
            history_text += f'{msg["role"]}: {msg["content"]}\n'
        
        # Step 4: Create the full prompt
        final_prompt = f"""{VYRA_BASE}

{style_prompt}

Conversation:
{history_text}

User: {user_input}

Answer in the selected style."""
        
        # Step 5: Get AI response
        answer = self.ask_model(final_prompt)
        
        # Return result with style info
        return {
            "style": style,
            "answer": answer
        }
