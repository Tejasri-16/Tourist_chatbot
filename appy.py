import streamlit as st
import openai

# Securely access your API key from Streamlit's secrets manager
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("My First Chatbot")

# --- Add your chatbot logic below ---
# For example, a text input and a button
user_input = st.text_input("Ask me anything!")

if st.button("Send"):
    if user_input:
        # A simple response for demonstration
        st.write(f"You said: {user_input}")
        # In a real app, you would call the OpenAI API here
    else:
        st.warning("Please enter a question.")