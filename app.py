
import streamlit as st
import asyncio
from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled
import os
from datetime import datetime
os.environ["GEMINI_API_KEY"] = "AIzaSyAIhv0wg9_xq6eI7xXTTSrNfvctSkey1Yw"

# --- Agent and API Configuration ---
# It's recommended to set the API key as an environment variable for security
gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    st.error("GEMINI_API_KEY environment variable not set. Please set it to run the app.")
    st.stop()

# Reference: https://ai.google.dev/gemini-api/docs/openai-compat
client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# Disable tracing for the agent SDK
set_tracing_disabled(disabled=True)

# Define the agent with its instructions and model
agent = Agent(
    name="Assistant",
    instructions="Answer all questions clearly, accurately, concisely. Stay on topic. Do not make up facts.",
    model=OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=client),
)

async def get_agent_response(user_message: str) -> str:
    """
    Asynchronously get the agent's response for a given user message.
    """
    try:
        result = await Runner.run(agent, user_message)
        return result.final_output
    except Exception as e:
        st.error(f"An error occurred while getting the agent's response: {e}")
        return "Sorry, I encountered an error."

# --- Streamlit UI ---

st.set_page_config(page_title="AI Chatbot UI", layout="wide")
st.title("AI Chatbot UI")

# --- Chat History Management ---

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Function to clear chat history
def clear_chat_history():
    st.session_state.messages = []

# --- UI Components ---

# Add a button to clear the chat history
st.sidebar.button("Clear Chat History", on_click=clear_chat_history, use_container_width=True)

# Display chat messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(f"*{message['timestamp']}*")
        st.markdown(message["content"])

# --- Chat Input and Response Logic ---

if prompt := st.chat_input("What would you like to ask?"):
    # Get current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Add user message to chat history
    st.session_state.messages.append({"role": "You", "content": prompt, "timestamp": timestamp})

    # Display user message in chat message container
    with st.chat_message("You"):
        st.markdown(f"*{timestamp}*")
        st.markdown(prompt)

    # Display a spinner while waiting for the bot's response
    with st.spinner("Bot is thinking..."):
        # Get bot response
        bot_response = asyncio.run(get_agent_response(prompt))
        bot_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Add bot response to chat history
    st.session_state.messages.append({"role": "Bot", "content": bot_response, "timestamp": bot_timestamp})

    # Display bot response
    with st.chat_message("Bot"):
        st.markdown(f"*{bot_timestamp}*")
        st.markdown(bot_response)

    # Rerun to update the chat display immediately
    st.experimental_rerun()
