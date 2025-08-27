import streamlit as st
from ollama import chat

st.title("Chat with chatbot (Via Ollama)")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Your message: "):
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    response = chat(
        model="llama3:latest",
        messages=st.session_state.messages,
        stream=False
    )

    # ✅ Only run when response exists
    assistant_msg = response["message"]["content"]

    st.session_state.messages.append({"role": "assistant", "content": assistant_msg})
    st.chat_message("assistant").write(assistant_msg)
