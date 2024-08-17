# chatbot_assistant.py
##import streamlit as st
##import openai
##import time
##
##st.set_page_config(page_title = "My Ai Chatbot", page_icon = ":skull:", layout = "wide")
##
##st.sidebar.title("Setup")
##api_key = st.sidebar.text_input("Enter your OpenAI API Key", type = "password")
##st.title("My AI Chatbot friend")
##
##if "messages" not in st.session_state:
##    st.session_state.messages = []
##
##ASSISTANT_ID = "asst_dO0fFVkhZW6MkEKllW8gL7xl"
##THREAD_ID = "thread_vpVgMpKWxJ8mqp4tialviS9V"
##
##def wait_for_run_complete(client, thread_id, run_id):
##    while True:
##        run = client.beta.threads.runs.retreive(thread_id=thread_id, run_id=run_id)
##        if run.complete_at:
##            return run.status
##        time.sleep(1)
##
##def get_assistant_response(client, user_input):
##    client.beta.threads.messages.create(
##        thread_id=THREAD_ID,
##        role = "user",
##        content = user_input
##
##        )
##    run = client.beta.threads.runs.create(
##        thread_id=THREAD_ID,
##        assistant_id=ASSISTANT_ID
##        )
##    wait_for_run_complete(client,THREAD_ID,run_id)
##    messages = client.beta.threads.message.list(thread_id=THREAD_ID)
##
##    return messages.data[0].content[0],text.value
##
##for messages in st.session_state.messages:
##    with st.chat_message(messages['role']):
##        st.markdown(messages['content'])
##
### chat input
##if api_key:
##    client = openai.OpenAI(api_key=api_key)
##
##    prompt = st.chat_input("Ask me anything!")
##
##    if prompt:
##        st.session_state.messages.append({"role":"user",
##                                                                      'content': prompt})
##        with st.chat_message('user'):
##            st.markdown(prompt)
##            
##        with st.chat_message('assistant'):
##            message_placeholder = st.empty
##            full_response = get_assistant_response(client, prompt)
##            message_placeholder.markdown(full_response)
##
##        st.session_state.messages.append({'role':'assistant',
##                                                                        'content':full_response})
##else:
##    st.warning("Please enter your OpenAI API Key in the sidebar to chat")


import streamlit as st
import openai
import time

# Streamlit page config
st.set_page_config(page_title="My AI Chatbot", page_icon="🤖", layout="wide")

# Sidebar for API key input
st.sidebar.title("Setup")
api_key = st.sidebar.text_input("Enter your OpenAI API Key", type="password")

# Main chat interface
st.title("🤖 My AI Chatbot")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Replace these with your own Assistant ID and Thread ID
ASSISTANT_ID = 'asst_dO0fFVkhZW6MkEKllW8gL7xl'
THREAD_ID = 'thread_vpVgMpKWxJ8mqp4tialviS9V'

def wait_for_run_complete(client, thread_id, run_id):
    while True:
        run = client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run_id)
        if run.completed_at:
            return run.status
        time.sleep(1)

def get_assistant_response(client, user_input):
    # Add the user's message to the thread
    client.beta.threads.messages.create(
        thread_id=THREAD_ID,
        role='user',
        content=user_input
    )
    # Create a run
    run = client.beta.threads.runs.create(
        thread_id=THREAD_ID,
        assistant_id=ASSISTANT_ID
    )
    # Wait for the run to complete
    wait_for_run_complete(client, THREAD_ID, run.id)
    # Retrieve the assistant's messages
    messages = client.beta.threads.messages.list(thread_id=THREAD_ID)

    # Return the latest assistant message
    return messages.data[0].content[0].text.value

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if api_key:
    client = openai.OpenAI(api_key=api_key)
    prompt = st.chat_input("Ask me anything!")
    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = get_assistant_response(client, prompt)
            message_placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})
else:
    st.warning("Please enter your OpenAI API key in the sidebar to start the chat.")
