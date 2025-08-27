# 🗨️ Chat with Chatbot (via Ollama + Streamlit)

This is a simple chatbot application built using [Streamlit](https://streamlit.io/) and [Ollama](https://ollama.ai/).  
It lets you chat with a locally running Ollama model (e.g., `llama3:latest`) through a Streamlit web UI.  

---

## 🚀 Features
- Chat-based interface using `st.chat_message` and `st.chat_input`
- Keeps conversation history using `st.session_state`
- Powered by Ollama’s local LLMs (e.g., LLaMA 3, Mistral, etc.)
- Simple and lightweight — runs locally

---

## 🛠️ Requirements
- Python **3.10+**  
- [Ollama](https://ollama.ai) installed and running locally  
- The model you want to use (example: `llama3:latest`)

---

## 📦 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/ollama-streamlit-chatbot.git
   cd ollama-streamlit-chatbot
2.

python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

3.Install dependencies

pip install -r requirements.txt


(If you don’t have a requirements.txt yet, generate it with:)

pip freeze > requirements.txt


4.Pull the Ollama model

ollama pull llama3:latest


5.Run the Streamlit app

streamlit run app.py

🖥️ Usage

Type your message in the chat box

The chatbot (powered by Ollama) will reply

Conversation history is preserved in the current session

📁 Project Structure
ollama-streamlit-chatbot/
│── app.py             # Main Streamlit app
│── requirements.txt   # Python dependencies
│── README.md          # Project documentation
└── .gitignore         # Ignore venv, __pycache__, etc.
