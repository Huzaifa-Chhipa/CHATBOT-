# AI Chatbot Application

This project is a web-based AI chatbot created using Python. It leverages the Streamlit framework for the user interface and Google's Gemini API for generating responses.

## How the Agent Works

The application operates as an interactive chat agent. Here is a breakdown of its functionality and architecture:

1.  **Web Interface**: The user interface is built with **Streamlit**. It provides a clean, real-time chat window for users to interact with the AI.

2.  **AI Model**: The chatbot uses the `gemini-2.0-flash` model from Google's Generative AI service. It connects to this service using an OpenAI-compatible API endpoint.

3.  **Agent Definition**: An "Agent" is defined with the following characteristics:
    *   **Name**: "Assistant"
    *   **Instructions**: The agent is programmed to "Answer all questions clearly, accurately, concisely. Stay on topic. Do not make up facts." This guides the tone and behavior of its responses.

4.  **Interaction Flow**:
    *   The user enters a question in the chat input box.
    *   The user's message is timestamped and displayed in the chat window.
    *   The application sends the user's message to the Gemini model.
    *   While waiting for a response, a "Bot is thinking..." message is shown.
    *   The AI's response is received, timestamped, and displayed in the chat window.

5.  **Chat History**:
    *   The application maintains a complete history of the conversation within the current session.
    *   A "Clear Chat History" button in the sidebar allows the user to reset the conversation at any time.

## Security Warning

**IMPORTANT**: The `app.py` file currently contains a hardcoded `GEMINI_API_KEY`. This is a significant security risk. It is strongly recommended to remove the hardcoded key and configure it using an environment variable as intended.

## How to Run the Application

To run this application on your local machine, follow these steps:

1.  **Prerequisites**: Ensure you have Python and `pip` installed.

2.  **Install Dependencies**: You will need to install the necessary Python libraries.
    ```bash
    pip install streamlit openai
    ```
    *(Note: The `agents` library appears to be a local module and must be present in the project directory.)*

3.  **Set Up Environment Variable**:
    *   Create a `.env` file in the root of the project directory.
    *   Add your Gemini API key to the file like this:
        ```
        GEMINI_API_KEY="YOUR_ACTUAL_API_KEY"
        ```
    *   Make sure the hardcoded key in `app.py` is removed to allow the environment variable to be used securely.

4.  **Run the App**: Execute the following command in your terminal:
    ```bash
    streamlit run app.py
    ```
