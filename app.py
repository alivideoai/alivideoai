import streamlit as st
import requests
from PIL import Image
import io
import random

st.set_page_config(page_title="Ali Video AI", page_icon="🎬")
st.title("Jo Likho Ge, Video Ban Jayegi!")
st.write("Full HD | Real | No Copyright")

topic = st.text_input("Topic Likho Yahan:", "Qabar Ki Pehli Raat")
style = st.selectbox("Video Size:", ["Short - 9:16 (TikTok/Shorts)", "Long - 16:9 (YouTube Full HD)"])

if style.startswith("Short"):
    W, H = 720, 1280
else:
    W, H = 1920, 1080

if st.button("VIDEO BANAO"):
    try:
        with st.spinner("Aapki Full HD image ban rahi hai..."):
            # Copyright free AI image
            prompt = f"{topic}, ultra realistic, cinematic, 8k, photorealistic, highly detailed"
            seed = random.randint(1, 999999)
            url = f"https://image.pollinations.ai/prompt/{prompt}?width={W}&height={H}&nologo=true&seed={seed}&model=flux"
            
            r = requests.get(url, timeout=60)
            r.raise_for_status()
            
            # Check ke image hai ya nahi
            img = Image.open(io.BytesIO(r.content))
            st.image(img, caption=f"{topic} - Full HD", use_column_width=True)
            
            # Download button
            st.download_button(
                label="📥 FULL HD DOWNLOAD (No Copyright)",
                data=r.content,
                file_name=f"{topic.replace(' ', '_')}.jpg",
                mime="image/jpeg"
            )
            st.success("✅ Ye 100% Real & No-Copyright hai! Isko 4-5 bar banao aur CapCut me jod kar Long/Short video bana lo!")
            st.info("Tip: Alag alag prompt likh kar 5 images banao, phir CapCut/InShot me jod do to Full HD video ban jayegi!")
            
    except Exception as e:
        st.error("Internet slow hai, dobara VIDEO BANAO dabao!")
        st.write(f"Detail: {e}")
