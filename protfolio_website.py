import streamlit as st
col1,col2 = st.columns(2)
background_css = """
<style>
body {
    background-color: #00ff00;
}
</style>
"""

# Apply the custom CSS
st.markdown(background_css, unsafe_allow_html=True)

with col1:
    st.subheader('Hi :wave:')
    st.title("I am Giri")
# with col2:
    # st.image("Giri.jpg")

st.title(" ")

st.title("Giri's AI Bot")
st.write("Ask anything about me")
st.text_input("")
st.button("ASK" , use_container_width= 400)