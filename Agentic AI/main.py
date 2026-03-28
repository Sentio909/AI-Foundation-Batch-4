import streamlit as st

from datetime import datetime
from chat_agent import chat_with_agent, chat_with_bank_agent



messages = st.session_state.get("messages", [])

if "messages" not in st.session_state:
    st.session_state["messages"] = messages

def get_greeting():
    current_hour = datetime.now().hour
    if 5 <= current_hour < 12:
        return "Good morning!"
    elif 12 <= current_hour < 18:
        return "Good afternoon!"
    else:
        return "Good evening!"

st.title("Hello There! 👋")

account_number = st.text_input("What's account number??")
if account_number:
    user_message = st.chat_input("Type your message here...")
    if user_message:
        previous_messages = st.session_state["messages"]
        message = chat_with_bank_agent(user_message , previous_messages , account_number)
        st.session_state["messages"] = messages + [{"role": "user", "content": user_message}, {"role": "assistant", "content": message}]

for message in st.session_state["messages"]:
    st.chat_message(message["role"]).write(message["content"])

#uv run streamlit run main.py
