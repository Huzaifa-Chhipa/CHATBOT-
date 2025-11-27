# How the Agent Works in Your Chatbot

1. **Agent Definition**
   - The `Agent` is like a smart assistant object.
   - It has:
     - A **name** (`Assistant`).
     - **Instructions** that tell it how to behave (clear, accurate, concise, no hallucinations).
     - A **model** (`gemini-2.0-flash`) that actually generates the responses.

2. **Sending a Message**
   - When the user types a message, it is passed to the agent via:
     ```python
     Runner.run(agent, user_message)
     ```
   - The `Runner` is responsible for executing the agent with the given input.

3. **Processing Inside the Agent**
   - The agent applies the instructions to guide how the model should respond.
   - It sends the input to the model (`OpenAIChatCompletionsModel`) asynchronously.
   - The model generates a response based on the instructions and input.

4. **Getting the Response**
   - The result returned by `Runner.run` contains `final_output`, which is the agent’s answer.
   - Example:
     ```python
     result = await Runner.run(agent, user_message)
     bot_response = result.final_output
     ```

5. **Output Back to UI**
   - The bot response is added to `st.session_state.messages`.
   - It is displayed in the Streamlit chat interface.

**Flow Summary:**
