import streamlit as st
import google.generativeai as genai
import os

col1,col2 = st.columns(2)
background_css = """
<style>
body {
    background-color: #00ff00;
}
</style>
"""
genai.configure(api_key="AIzaSyAcC_173cY97ahct08WxuvggA5J40Eqzik")

model = genai.GenerativeModel('gemini-1.5-flash')


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
User_input = st.text_input("")

if st.button("ASK" , use_container_width= 400):
    prompt = User_input
    response = model.generate_content(prompt)
    st.write(response.text)

col1, col2 = st.columns(2)
st.title(" ")
with col1:
    st.subheader("Youtube Channel")
    st.write("- This is a largest CV chanel")
    st.write("- 400k+ Subscriber")
    st.write("- Over 150 free Tutorial")
    st.write("- 1.5 Million Hours+ watch time ")

with col2:
    st.video('https://www.youtube.com/watch?v=_2UqdX8dcsU')
st.title(" ")
st.title("My Setup")
st.image('Giri.jpg')
st.write(" ")
st.title("My Skills")
st.slider("Programming", 0,100,70)
st.slider("teaching" , 0, 100 ,50)
st.slider("ML/DL", 0, 100 , 80)

