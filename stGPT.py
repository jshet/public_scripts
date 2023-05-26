import os
import streamlit as st 
import openai
import apikey

key = apikey.OPENAI_API_KEY
os.environ["OPENAI_API_KEY"] = key
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(layout="wide")
st.title("stGPT")
# Initialization
if 'conversation' not in st.session_state:
    st.session_state['conversation'] = []

@st.cache_data
def ask(question, temp=0.5):
    conversation = st.session_state['conversation']
    conversation.append(question)
    answer = openai.ChatCompletion.create(model="gpt-3.5-turbo",temperature=temp,messages=conversation)
    conversation.append(answer["choices"][0]["message"])
    st.session_state['conversation'] = conversation
    return answer

col1, col2 = st.columns([1,2])

with col1:
    """
    ### System prompt
    """
    system_prompt = st.text_input("System prompt:", value="You are a smart and creative writing assistant.")
    reset = st.button("Reset")
    if reset:
        st.session_state['conversation'] = [{"role": "system", "content": system_prompt}]

    chat_prompt = st.text_area(">>>")
    send = st.button("Send")
    trim_prompt = st.button("Delete earlier messages?")
    if trim_prompt:
        conversation = st.session_state['conversation']
        conversation.pop(1)

    if send:
        question = {"role": "user", "content": chat_prompt}
        response = ask(question)
        with st.expander("Response details"):
            response

with col2:
    """
    ### Conversation
    """
    conversation = st.session_state["conversation"]
    for message in conversation:
        st.write(message['role'])
        st.write(message['content'])
    
    show_json = st.button("JSONify?")
    if show_json:
        msg = conversation[-1]['content']
        st.json(msg)

    show_raw = st.button("Raw output?")
    if show_raw:
        msg = conversation[-1]['content']
        st.code(msg)