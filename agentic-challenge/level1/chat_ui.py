# VERSION-1 (Basic Chatbot with Gemini API)
# import os
# import json
# import streamlit as st
# import google.generativeai as genai
# from dotenv import load_dotenv
# from datetime import datetime

# # --- Page Config ---
# st.set_page_config(page_title="ASTRO AI ", page_icon="🤖")

# st.title("🤖 ASTRO - AI Chat BOT")
# st.caption("An AI-powered chatbot using Google Gemini API")

# # --- Load Gemini API ---
# load_dotenv()
# api_key = os.getenv("GOOGLE_API_KEY")
# if not api_key:
#     st.error("API key not found! Please set GOOGLE_API_KEY in your .env file.")
#     st.stop()
# genai.configure(api_key=api_key)
# model = genai.GenerativeModel('gemini-2.5-pro')

# # --- Chat History Management ---
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# if "system_prompt" not in st.session_state:
#     st.session_state.system_prompt = (
#         "You are ASTRO, a helpful AI assistant. "
#         "Provide concise and informative answers, and use markdown formatting for code."
#     )

# # --- Sidebar Features ---
# with st.sidebar:
#     if st.button("Reset Conversation"):
#         st.session_state.messages = []
#     if st.button("Export Chat"):
#         with open("chat_history.json", "w") as f:
#             json.dump(st.session_state.messages, f, indent=4)
#         st.success("Chat history saved as chat_history.json!")

# # --- Display Chat Messages ---
# for msg in st.session_state.messages:
#     with st.chat_message(msg["role"]):
#         st.markdown(msg["content"])

# # --- Chat Input ---
# if prompt := st.chat_input("Ask me anything..."):
#     # Add user message
#     user_message = {"role": "user", "content": prompt, "time": str(datetime.now())}
#     st.session_state.messages.append(user_message)
#     with st.chat_message("user"):
#         st.markdown(prompt)

#     # Generate AI response with context
#     messages_for_gemini = [{"role": "system", "content": st.session_state.system_prompt}] + st.session_state.messages
#     try:
#         with st.chat_message("assistant"):
#             with st.spinner("Thinking..."):
#                 response = model.generate_content(prompt, candidate_count=1)
#                 response_text = response.text

#                 # Render response word by word for realism
#                 for chunk in response_text.split(". "):
#                     st.markdown(chunk + ".")
#         # Store AI response
#         st.session_state.messages.append({"role": "assistant", "content": response_text, "time": str(datetime.now())})
#     except Exception as e:
#         st.error(f"Failed to get response: {e}")


# VERSION-2 (Improved with Space Theme, Search, and Better UI)
# import os
# import json
# import streamlit as st
# import google.generativeai as genai
# from dotenv import load_dotenv
# from datetime import datetime
# import re

# # --- Page Config ---
# st.set_page_config(
#     page_title="ASTRO AI Chatbot",
#     page_icon="🌌",
#     layout="wide"
# )

# # --- Custom CSS for Space Theme ---
# st.markdown("""
# <style>
# body {
#     background-color: #0b0c10;
#     color: #c5c6c7;
#     font-family: 'Courier New', monospace;
# }
# .stButton>button {
#     background-color: #1f2833;
#     color: #66fcf1;
# }
# .stTextInput>div>input {
#     background-color: #1f2833;
#     color: #c5c6c7;
# }
# .stChatMessage {
#     border-radius: 10px;
#     padding: 10px;
#     margin-bottom: 5px;
# }
# .stChatMessage.user {
#     background-color: #45a29e;
#     color: #0b0c10;
# }
# .stChatMessage.assistant {
#     background-color: #1f2833;
#     color: #66fcf1;
# }
# </style>
# """, unsafe_allow_html=True)

# st.title("🌌 ASTRO - AI Space Chatbot")
# st.caption("A cosmic AI assistant powered by Google Gemini API")

# # --- Load Gemini API ---
# load_dotenv()
# api_key = os.getenv("GOOGLE_API_KEY")
# if not api_key:
#     st.error("API key not found! Please set GOOGLE_API_KEY in your .env file.")
#     st.stop()
# genai.configure(api_key=api_key)
# model = genai.GenerativeModel('gemini-2.5-pro')

# # --- Session State Management ---
# if "messages" not in st.session_state:
#     st.session_state.messages = []
# if "system_prompt" not in st.session_state:
#     st.session_state.system_prompt = (
#         "You are ASTRO, a cosmic AI assistant. "
#         "Provide informative and space-themed responses. "
#         "Use markdown for formatting, including code snippets."
#     )

# # --- Sidebar Features ---
# with st.sidebar:
#     st.header("🌠 Options")
#     if st.button("Reset Conversation"):
#         st.session_state.messages = []
#         st.success("Conversation reset!")

#     st.subheader("🔍 Search Chat History")
#     search_query = st.text_input("Enter keyword to search")
#     if search_query:
#         results = [m for m in st.session_state.messages if search_query.lower() in m["content"].lower()]
#         st.write(f"Found {len(results)} message(s) containing '{search_query}':")
#         for msg in results:
#             st.markdown(f"**{msg['role'].capitalize()} ({msg['time']}):** {msg['content']}")

#     if st.button("Export Chat"):
#         with open("chat_history.json", "w") as f:
#             json.dump(st.session_state.messages, f, indent=4)
#         st.success("Chat history saved as chat_history.json!")

# # --- Display Chat Messages ---
# for msg in st.session_state.messages:
#     with st.chat_message(msg["role"]):
#         st.markdown(msg["content"], unsafe_allow_html=True)

# # --- Chat Input ---
# if prompt := st.chat_input("Ask me anything about space..."):
#     user_message = {"role": "user", "content": prompt, "time": str(datetime.now())}
#     st.session_state.messages.append(user_message)
#     with st.chat_message("user"):
#         st.markdown(prompt)

#     # --- Streaming AI Response ---
#     with st.chat_message("assistant"):
#         response_text = ""
#         placeholder = st.empty()
#         try:
#             # Gemini response
#             response = model.generate_content(prompt)
#             for chunk in response.text.split(". "):  # simulate typing
#                 response_text += chunk + ". "
#                 placeholder.markdown(response_text + "▌")  # blinking cursor effect
#             placeholder.markdown(response_text)
#         except Exception as e:
#             st.error(f"Failed to get response: {e}")

#     # Store assistant response
#     st.session_state.messages.append({
#         "role": "assistant",
#         "content": response_text,
#         "time": str(datetime.now())
#     })


# VERSION-3 (Advanced with Contextual Memory and Enhanced UI)
import os
import json
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
from datetime import datetime
import time

# --- Page Config ---
st.set_page_config(
    page_title="ASTRO AI Chatbot",
    page_icon="🌌",
    layout="wide"
)

# --- Custom CSS for Space Theme and Starfield ---
st.markdown("""
<style>
body {
    background-color: #0b0c10;
    color: #c5c6c7;
    font-family: 'Courier New', monospace;
    overflow-x: hidden;
}
.stButton>button {
    background-color: #1f2833;
    color: #66fcf1;
}
.stTextInput>div>input {
    background-color: #1f2833;
    color: #c5c6c7;
}
.stChatMessage {
    border-radius: 10px;
    padding: 10px;
    margin-bottom: 5px;
}
.stChatMessage.user {
    background-color: #45a29e;
    color: #0b0c10;
}
.stChatMessage.assistant {
    background-color: #1f2833;
    color: #66fcf1;
}

/* Animated starfield */
@keyframes moveStars {
    from {background-position: 0 0;}
    to {background-position: -1000px 1000px;}
}
body::before {
    content: "";
    position: fixed;
    top:0; left:0; width: 100%; height: 100%;
    background: url('https://i.ibb.co/0s3pdnc/starfield.png') repeat;
    z-index: -1;
    animation: moveStars 120s linear infinite;
}
</style>
""", unsafe_allow_html=True)

st.title("🌌 ASTRO - AI Space Chatbot")
st.caption("A cosmic AI assistant powered by Google Gemini API")

# --- Load Gemini API ---
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    st.error("API key not found! Please set GOOGLE_API_KEY in your .env file.")
    st.stop()
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-2.5-pro')

# --- Session State ---
if "messages" not in st.session_state:
    st.session_state.messages = []

if "system_prompt" not in st.session_state:
    st.session_state.system_prompt = (
        "You are ASTRO, a cosmic AI assistant. "
        "Provide space-themed, informative answers. Use markdown for formatting, including code snippets. "
        "Keep track of the conversation context and summarize previous exchanges when needed."
    )

# --- Sidebar ---
with st.sidebar:
    st.header("🌠 Options")
    if st.button("Reset Conversation"):
        st.session_state.messages = []
        st.success("Conversation reset!")

    st.subheader("🔍 Search Chat History")
    search_query = st.text_input("Enter keyword to search")
    if search_query:
        results = [m for m in st.session_state.messages if search_query.lower() in m["content"].lower()]
        st.write(f"Found {len(results)} message(s) containing '{search_query}':")
        for msg in results:
            st.markdown(f"**{msg['role'].capitalize()} ({msg['time']}):** {msg['content']}")

    if st.button("Export Chat"):
        with open("chat_history.json", "w") as f:
            json.dump(st.session_state.messages, f, indent=4)
        st.success("Chat history saved as chat_history.json!")

# --- Display Chat Messages ---
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"], unsafe_allow_html=True)

# --- Generate context summary for multi-turn memory ---
def summarize_context(messages, max_tokens=1500):
    """
    Summarize previous conversation for better context in long chats.
    """
    if len(messages) < 4:
        return ""  # skip summarization for short conversations
    summary_prompt = "Summarize the conversation so far concisely:\n\n"
    for msg in messages[-10:]:  # last 10 messages
        summary_prompt += f"{msg['role'].capitalize()}: {msg['content']}\n"
    try:
        summary = model.generate_content(summary_prompt).text
        return summary
    except:
        return ""  # fallback

# --- Chat Input ---
if prompt := st.chat_input("Ask me anything about space..."):
    user_message = {"role": "user", "content": prompt, "time": str(datetime.now())}
    st.session_state.messages.append(user_message)
    with st.chat_message("user"):
        st.markdown(prompt)

    # --- Multi-turn Memory ---
    context_summary = summarize_context(st.session_state.messages)
    full_prompt = st.session_state.system_prompt
    if context_summary:
        full_prompt += f"\nPrevious conversation summary:\n{context_summary}\nUser question: {prompt}"
    else:
        full_prompt += f"\nUser question: {prompt}"

    # --- Streaming Word-by-Word AI Response ---
    with st.chat_message("assistant"):
        response_text = ""
        placeholder = st.empty()
        try:
            response = model.generate_content(full_prompt)
            for char in response.text:  # stream character by character
                response_text += char
                placeholder.markdown(response_text + "▌")  # blinking cursor
                time.sleep(0.01)  # small delay for realistic typing
            placeholder.markdown(response_text)
        except Exception as e:
            st.error(f"Failed to get response: {e}")

    # Store assistant response
    st.session_state.messages.append({
        "role": "assistant",
        "content": response_text,
        "time": str(datetime.now())
    })
