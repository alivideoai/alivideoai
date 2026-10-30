import streamlit as st
from gtts import gTTS
import requests
from PIL import Image
import io

st.set_page_config(page_title="Ali Video AI")
st.title("Ali Video AI - Text to Video")
st.write("Jo Likho Ge, Video Ban Jayegi!")

topic = st.text_input("Topic Likho Yahan:", "Qabar Ki Pehli Raat")

if st.button("VIDEO BANAO"):
    st.write("Video ban rahi hai...")
    
    # Free Photo Ban Rahi Hai
    url = f"https://image.pollinations.ai/prompt/{topic} Islamic cinematic"
    r = requests.get(url)
    img = Image.open(io.BytesIO(r.content))
    st.image(img)
    
    # Free Awaz Ban Rahi Hai
    tts = gTTS(f"{topic} ki kahani suniye", lang='ur')
    tts.save("voice.mp3")
    st.audio("voice.mp3")
    
    st.success("Video Ready Ho Gayi!")
