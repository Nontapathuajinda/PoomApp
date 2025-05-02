import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.title("ตรวจจับใบหน้าภาพ")

uploaded_file = st.file_uploader("อัปโหลดรูปภาพจากมือถือ",type=["jpg","png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    img_np = np.array(image.convert('RGB'))
    img = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)
    
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +"haarcascade_frontalface_default.xml")

    gray =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,    
    minNeighbors=1,
    minSize=(200, 200))

    for (x, y, w, h) in faces:
        cv2.rectangle(img_np, (x, y), (x + w, y + h), (255, 0, 0), 2)

    st.image(img_np,caption=f"ตรวจบพใบหน้า {len(faces)} คน",use_container_width=True)
    st.success(f"ตรวจพบใบหน้าทั้งหมด: {len(faces)} คน")
    
bg1="""
<style>
.stApp {
    background-color: #9AD9DB;
    color: #000000;
}
</style>
"""
st.html(bg1)
