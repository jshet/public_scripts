import os
import streamlit as st 
import openai
import apikey
from prompts import prompts
from datetime import datetime

key = apikey.OPENAI_API_KEY
os.environ["OPENAI_API_KEY"] = key
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(layout="wide")
st.title("stGPT")
# Initialization
if 'conversation' not in st.session_state:
    st.session_state['conversation'] = []

@st.cache_data
def ask(question, temp=0.5, model="gpt-3.5-turbo"):
    conversation = st.session_state['conversation']
    conversation.append(question)
    answer = openai.ChatCompletion.create(model=model,temperature=temp,messages=conversation)
    conversation.append(answer["choices"][0]["message"])
    st.session_state['conversation'] = conversation
    return answer

col1, col2 = st.columns([1,2])

with col1:
    """
    ### System prompt
    """
    selected_prompt = st.selectbox("Choose a system prompt", options=prompts.keys())
    system_prompt = st.text_area("System prompt:", value=prompts[selected_prompt])
    response_temp = st.slider("Response temperature:", min_value=0.0, max_value=2.0, value=0.5)
    reset = st.button("(Re)start conversation")
    if reset:
        st.session_state['conversation'] = [{"role": "system", "content": system_prompt}]

    model = "gpt-3.5-turbo"
    model_16k = st.checkbox("Use 16k token gpt model?")
    if model_16k:
        model = "gpt-3.5-turbo-16k"

    chat_prompt = st.text_area(">>>")
    send = st.button("Send")
    trim_prompt = st.button("Delete earlier messages?")
    if trim_prompt:
        conversation = st.session_state['conversation']
        conversation.pop(1)

    if send:
        question = {"role": "user", "content": chat_prompt}
        response = ask(question, temp=response_temp, model=model)
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
    
    save_to_file = st.button("Save conversation to file")
    if save_to_file:
        now = os.path.join("history", str(datetime.now()).replace(" ","-") + ".txt")
        with open(now, 'x') as f:
            for m in conversation:
                f.write(f"{m['role']}: {m['content']}\n")
                f.write("-"*80)
                f.write("\n")
