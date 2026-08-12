import streamlit as st
import uuid
import json
import os
from datetime import datetime

from agent import VyraAgent
from styles import get_css


HISTORY_FILE = os.path.join(os.path.dirname(__file__), "chats_history.json")


def load_chats():
    """Load saved chats from disk. Returns {} if none exist."""
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, dict):
                    return data
        except Exception:
            pass
    return {}


def save_chats():
    """Persist all chats to disk."""
    try:
        with open(HISTORY_FILE, "w", encoding="utf-8") as f:
            json.dump(st.session_state.chats, f, indent=2, ensure_ascii=False)
    except Exception as error:
        print(f"Could not save chat history: {error}")



def init_session():
    if "chats" not in st.session_state:
        st.session_state.chats = load_chats()
    
    # Ensure there is always at least one chat
    if not st.session_state.chats:
        chat_id = str(uuid.uuid4())
        st.session_state.chats[chat_id] = {
            "title": "New Chat",
            "messages": [],
            "created_at": datetime.now().isoformat(),
            "metadata": {
                "message_count": 0,
                "last_style": None
            }
        }
        save_chats()
    
    if "current_chat_id" not in st.session_state or st.session_state.current_chat_id not in st.session_state.chats:
        st.session_state.current_chat_id = next(iter(st.session_state.chats))
    
    if "regenerate_after_edit" not in st.session_state:
        st.session_state.regenerate_after_edit = False


def get_current_chat():
    return st.session_state.chats[st.session_state.current_chat_id]


def create_new_chat():
    chat_id = str(uuid.uuid4())
    st.session_state.chats[chat_id] = {
        "title": "New Chat",
        "messages": [],
        "created_at": datetime.now().isoformat(),
        "metadata": {
            "message_count": 0,
            "last_style": None
        }
    }
    st.session_state.current_chat_id = chat_id
    save_chats()


def update_metadata(style=None):
    chat = get_current_chat()
    chat["metadata"]["message_count"] = len([
        m for m in chat["messages"] if m["role"] == "user"
    ])
    if style:
        chat["metadata"]["last_style"] = style


def generate_chat_title(user_input):
    words = user_input.split()[:5]
    return " ".join(words) + ("..." if len(user_input.split()) > 5 else "")


init_session()
agent = VyraAgent()
st.set_page_config(page_title="VYRA", page_icon="🤖", layout="wide")
st.markdown(get_css(), unsafe_allow_html=True)


with st.sidebar:
    st.title("🤖 VYRA")
    st.caption("Versatile Yet Responsive Assistant")
    
    if st.button("➕ New Chat", use_container_width=True):
        create_new_chat()
        st.rerun()
    
    st.divider()
    st.subheader("History")
    
    for chat_id, chat in list(st.session_state.chats.items()):
        col1, col2 = st.columns([5, 1])
        
        with col1:
            if st.button(chat["title"], key=f"chat_{chat_id}", use_container_width=True):
                st.session_state.current_chat_id = chat_id
                st.rerun()
        
        with col2:
            if st.button("🗑", key=f"delete_{chat_id}"):
                del st.session_state.chats[chat_id]
                save_chats()
                
                if st.session_state.current_chat_id == chat_id:
                    if st.session_state.chats:
                        st.session_state.current_chat_id = next(iter(st.session_state.chats))
                    else:
                        create_new_chat()
                
                st.rerun()


current_chat = get_current_chat()
messages = current_chat["messages"]


st.title("VYRA")
st.caption("Smart enough to help. Sarcastic enough to survive you.")


col1, col2 = st.columns([1, 1])

with col1:
    summarize_clicked = st.button("📝 Summarize", use_container_width=True)

with col2:
    if st.button("🧹 Clear", use_container_width=True):
        current_chat["messages"] = []
        save_chats()
        st.rerun()


if summarize_clicked:
    if not messages:
        st.warning("There is nothing to summarize yet.")
    else:
        conversation = ""
        for message in messages:
            conversation += f'{message["role"]}: {message["content"]}\n'
        
        summary_prompt = f"Summarize the conversation. Keep it short and clear.\n\nConversation:\n\n{conversation}"
        
        try:
            summary = agent.ask_model(summary_prompt)
            st.info(summary)
        except Exception as error:
            st.error(f"Could not summarize: {error}")


for index, message in enumerate(messages):
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
        if message["role"] == "user":
            with st.expander("✏️ Edit prompt"):
                edited_prompt = st.text_area(
                    "Edit your prompt",
                    value=message["content"],
                    key=f"edit_{index}"
                )
                
                if st.button("Save Edit", key=f"save_{index}"):
                    message["content"] = edited_prompt
                    current_chat["messages"] = messages[:index + 1]
                    st.session_state.regenerate_after_edit = True
                    save_chats()
                    st.rerun()


user_input = st.chat_input("Ask VYRA anything...")


# --------------------------------
# AUTO-REGENERATE AFTER EDIT
# --------------------------------

if st.session_state.regenerate_after_edit and messages and messages[-1]["role"] == "user":
    st.session_state.regenerate_after_edit = False
    
    with st.chat_message("assistant"):
        with st.spinner("VYRA is thinking..."):
            try:
                result = agent.respond(messages[-1]["content"], messages[:-1])
                
                if result["style"] == "SRK":
                    st.caption("🎭 Calm witty mode")
                else:
                    st.caption("🔥 High-energy mode")
                
                answer = result["answer"]
                st.markdown(answer)
                
                messages.append({
                    "role": "assistant",
                    "content": answer,
                    "style": result["style"]
                })
                
                update_metadata(style=result["style"])
                save_chats()
                
                st.rerun()
            
            except Exception as error:
                st.error(f"VYRA encountered an error: {error}")


if user_input:
    if current_chat["title"] == "New Chat":
        current_chat["title"] = generate_chat_title(user_input)
    
    with st.chat_message("user"):
        st.markdown(user_input)
    
    messages.append({
        "role": "user",
        "content": user_input
    })
    
    with st.chat_message("assistant"):
        with st.spinner("VYRA is thinking..."):
            try:
                result = agent.respond(user_input, messages[:-1])
                
                if result["style"] == "SRK":
                    st.caption("🎭 Calm witty mode")
                else:
                    st.caption("🔥 High-energy mode")
                
                answer = result["answer"]
                st.markdown(answer)
                
                messages.append({
                    "role": "assistant",
                    "content": answer,
                    "style": result["style"]
                })
                
                update_metadata(style=result["style"])
                save_chats()
                
                st.rerun()
            
            except Exception as error:
                st.error(f"VYRA encountered an error: {error}")

