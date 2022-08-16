import io
import streamlit as st 
from PIL import Image
import image_resizer 

st.markdown("# Image resizer")
st.markdown("## Upload image")

try:
    im = st.file_uploader("Upload image", type=['jpg','png','jpeg'])
except:
    pass

try:
    with st.expander("More options"):
        c1, c2 = st.columns(2)
        with c1:
            width = st.number_input("Max width:", value=1920)
        with c2:
            height = st.number_input("Max height:", value=1920)

        max_dimension = max(width, height)

    original, thumb = image_resizer.make_thumbnail(im, max_dimension=max_dimension)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("## Input")
        i_size = original.size
        st.image(original)
        st.write(f'Size: {i_size}')

    with col2:
        st.markdown("## Output")
        t_size = thumb.size
        st.image(thumb)
        st.write(f'Size: {t_size}')

    st.markdown("## Download image")
    im_bytes = io.BytesIO()
    thumb.save(im_bytes, format='JPEG')
    fn = st.text_input('Save as:',value=im.name)
    st.download_button('Download image', im_bytes.getvalue(), file_name=fn)

except:
    pass