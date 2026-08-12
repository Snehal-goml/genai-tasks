import requests
from personalities import VYRA_BASE, SRK_STYLE, RANVEER_STYLE


class VyraAgent:
    def __init__(self):
        self.model = "llama3.2:3b"
        self.url = "http://localhost:11434/api/generate"
    
    def ask_model(self, prompt):
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
        lower = user_input.lower()
        if "srk" in lower or "shah rukh" in lower:
            return "SRK"
        if "ranveer" in lower:
            return "RANVEER"
        if history:
            recent = history[-3:]
            srk_count = sum(1 for m in recent if m.get("style") == "SRK")
            if srk_count > len(recent) - srk_count:
                return "SRK"
        energetic = ["motivation", "gym", "hype", "energy", "confidence", "excited", "lets go", "pump", "strong"]
        calm = ["think", "feel", "life", "meaning", "advice", "understand", "wisdom", "philosophy"]
        if any(kw in lower for kw in energetic):
            return "RANVEER"
        if any(kw in lower for kw in calm):
            return "SRK"
        return "SRK"
    
    def respond(self, user_input, history):
        style = self.choose_style(user_input, history)
        style_prompt = SRK_STYLE if style == "SRK" else RANVEER_STYLE
        history_text = ""
        for msg in history[-8:]:
            history_text += f'{msg["role"]}: {msg["content"]}\n'
        final_prompt = f"""{VYRA_BASE}

{style_prompt}

Conversation:
{history_text}

User: {user_input}

Answer in the selected style."""
        answer = self.ask_model(final_prompt)
        return {
            "style": style,
            "answer": answer
        }


if __name__ == "__main__":
    print("Testing simple VyraAgent...")
    agent = VyraAgent()
    print("Agent created successfully")
    print(f"Model: {agent.model}")
    print(f"URL: {agent.url}")
