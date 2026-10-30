import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import requests
import io
import os
import random
from moviepy.editor import ImageSequenceClip, TextClip, CompositeVideoClip

st.set_page_config(page_title="Ali Video AI - Full HD", layout="centered")
st.title("Jo Likho Ge, Video Ban Jayegi!")
st.write("Full HD | Real | No Copyright")

topic = st.text_input("Topic Likho Yahan:", "Qabar Ki Pehli Raat")
video_type = st.selectbox("Video Type:", ["Short - 30 sec (9:16)", "Long - 60 sec (16:9)"])

if st.button("VIDEO BANAO"):
    status = st.empty()
    status.write("🎬 Aapki Full HD video ban rahi hai... 1-2 minute lagega...")
    
    try:
        if "Short" in video_type:
            width, height = 720, 1280
            duration = 30
        else:
            width, height = 1920, 1080
            duration = 60

        # 5 alag alag scenes banayenge topic se
        prompts = [
            f"{topic}, cinematic, ultra realistic, 8k",
            f"{topic} close up, detailed, photorealistic",
            f"{topic}, dramatic lighting, full hd",
            f"{topic}, wide angle, realistic",
            f"{topic}, emotional scene, high quality"
        ]
        
        images = []
        progress = st.progress(0)
        
        for i, p in enumerate(prompts):
            progress.progress((i+1)*20)
            status.write(f"Scene {i+1}/5 ban raha hai...")
            url = f"https://image.pollinations.ai/prompt/{p}?width={width}&height={height}&nologo=true&seed={random.randint(1,9999)}"
            r = requests.get(url, timeout=40)
            img = Image.open(io.BytesIO(r.content)).convert("RGB")
            img_path = f"/tmp/scene_{i}.jpg"
            img.save(img_path)
            images.append(img_path)

        status.write("🎥 Ab video jod raha hu...")
        # Video banao
        clip = ImageSequenceClip(images, fps=1)
        # Har image 6 sec ya 12 sec
        clip = clip.set_duration(duration)
        clip = clip.resize((width, height))
        
        video_path = "/tmp/final_video.mp4"
        clip.write_videofile(video_path, fps=24, codec='libx264', audio=False, logger=None)
        
        progress.progress(100)
        status.write("✅ Video Ready!")
        
        st.video(video_path)
        with open(video_path, "rb") as f:
            st.download_button("📥 FULL HD VIDEO DOWNLOAD KARO", f, file_name=f"{topic}.mp4", mime="video/mp4")
        
        st.success("Ye video 100% No-Copyright hai, YouTube / TikTok par laga sakte ho!")

    except Exception as e:
        st.error(f"Error: {e}")
        st.info("Dobara VIDEO BANAO dabao, internet ki wajah se kabhi kabhi fail hota hai.")
        
