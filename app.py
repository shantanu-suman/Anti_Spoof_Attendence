import streamlit as st
import cv2
import numpy as np
from utils.face_recognition_utils import load_known_faces, recognize_face
from utils.liveness_detection import is_real_face
from database import log_attendance

st.title("🎯 Face Recognition Attendance System")

frame_window = st.image([])

cap = cv2.VideoCapture(0)

known_faces, names = load_known_faces('images/known_faces_rgb')

run = st.checkbox('Start Camera')

while run:
    ret, frame = cap.read()
    if not ret:
        break

    # Flip frame for natural mirror effect
    frame = cv2.flip(frame, 1)

    if is_real_face(frame):  # Basic liveness check
        name = recognize_face(frame, known_faces, names)
        if name:
            log_attendance(name)
            st.success(f"✅ Attendance marked for {name}")
        else:
            st.warning("Unknown Face")

    else:
        st.error("⚠️ Spoofing Detected! Please show real face")

    frame_window.image(frame, channels="BGR")

cap.release()
