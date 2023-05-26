import os
import streamlit as st 
import openai
import apikey

key = apikey.OPENAI_API_KEY
os.environ["OPENAI_API_KEY"] = key
openai.api_key = os.getenv("OPENAI_API_KEY")

@st.cache_data
def ask(system_prompt, chat_prompt):
    conversation = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": chat_prompt}
            ]
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo",temperature=0.7,presence_penalty=1,frequency_penalty=1,messages=conversation)
    return response

"""
# Speculator 5000
### System prompt
This is the default prompt. Adjust as desired.
"""
system = st.text_input("System prompt:", value="You are a smart and creative author of futurist fiction.")

"""
### Prompt
Enter one or more topics separated by the '|' character to generate articles in markdown format.
The topic will be entered into the default prompt.
"""
topics = st.text_input("Topic(s):", value="healthy eating")
scene = st.text_input("Image scene (optional)", value="No image")

response = ""

def converse(topic):
    chat = f"Please think of an extra spontaneous and creative idea for an article about '{topic}'. Write a 500 word article and provide links to research where helpful. Format the output as markdown. Don't use the word 'conclusion'."
    answer = ask(system, chat)
    answer_text = answer["choices"][0]["message"]["content"]
    st.markdown(answer_text)
    response = answer
    with st.expander("Show request and response"):
        st.write(chat)
        st.text(response)
    return answer_text

@st.cache_data
def make_image(scene):
    img_response = openai.Image.create(prompt=scene,n=2,size="1024x1024")
    return img_response.data

def save_output(fn, text):
    with open(fn, "w", encoding='utf8') as f:
        f.write(text)

save_to_file = st.checkbox("Save output(s) to file(s)?")
run_btn = st.button("Run")

if run_btn:
    if scene != "No image":
        imgs = make_image(scene)
        col1, col2 = st.columns(2)
        with col1:
            st.image(imgs[0]['url'])
        with col2:
            st.image(imgs[1]['url'])
    for topic in topics.split("|"):
        output = converse(topic)
        if save_to_file:
            name_of_file = topic.replace(" ","-") + ".md"
            save_as = os.path.join("output", name_of_file)
            save_output(save_as, output)

st.divider()