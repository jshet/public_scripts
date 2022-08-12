import io
import streamlit as st 
import qr_code_generator 

initial_values = {
    'fill_color':'#000000', 
    'back_color': '#FFFFFF',
    'border':2,
    'box_size':10
    }

prayer = "Our Father in heaven, hallowed be your name, your kingdom come, your will be done, on earth as it is in heaven. Give us today our daily bread. And forgive us our debts, as we also have forgiven our debtors. And lead us not into temptation, but deliver us from the evil one."

for s in initial_values:
    if s not in st.session_state:
        st.session_state[s] = initial_values[s]

def reset_values():
    for s in initial_values:
        st.session_state[s] = initial_values[s]

st.markdown("# QR Code Generator")

col1, col2, col3 = st.columns([1,.1,2])

with col1:
    st.markdown("## Inputs")
    data = st.text_input(label='QR code data', value=prayer)
    is_url = st.checkbox("Is this a url?", value=False)
    fn = st.text_input('Save as filename', value='test.png')

    if is_url:
        data = data.replace(" ","+")
        st.write(f'(Link will go here: {data})')

    st.markdown('## Options')
    st.markdown('#### Fill color')
    st.session_state.fill_color = st.text_input('Type it (example: "#000000")', value=st.session_state.fill_color, max_chars=7)
    st.session_state.fill_color = st.color_picker('Fill color', value=st.session_state.fill_color)

    st.markdown('#### Background color')
    st.session_state.back_color = st.text_input('Type it (example: "#000000")', value=st.session_state.back_color, max_chars=7)
    st.session_state.back_color = st.color_picker('Background color', value=st.session_state.back_color)

    st.markdown('#### Border size')
    st.session_state.border = st.slider("Pick a border size", value=st.session_state.border, max_value=10)

    st.markdown('#### Box size')
    st.session_state.box_size = st.slider("Pick a box size", value=st.session_state.box_size, min_value=1, max_value=50)

    st.button('Reset to default values', on_click=reset_values)

with col3:
    qr = qr_code_generator.make_qr_code(data, fill_color=st.session_state.fill_color, back_color=st.session_state.back_color, border=st.session_state.border, box_size=st.session_state.box_size)
    qr_bytes = io.BytesIO()
    qr.save(qr_bytes, format='PNG')

    st.markdown("## Output")
    st.image(qr_bytes.getvalue())
    st.download_button('Download image', qr_bytes.getvalue(), file_name=fn)