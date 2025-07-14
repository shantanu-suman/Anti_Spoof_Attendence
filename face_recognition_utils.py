import cv2
import face_recognition
import os
import numpy as np

def load_known_faces(known_faces_dir):
    known_encodings = []
    known_names = []

    for filename in os.listdir(known_faces_dir):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            image_path = os.path.join(known_faces_dir, filename)
            image = cv2.imread(image_path)

            if image is None:
                print(f"Could not read image {image_path}")
                continue

            # Handle images with alpha channel (4 channels)
            if len(image.shape) == 3 and image.shape[2] == 4:
                image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)

            # Convert BGR to RGB
            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            # Ensure dtype is uint8
            if image_rgb.dtype != np.uint8:
                image_rgb = image_rgb.astype(np.uint8)

            encodings = face_recognition.face_encodings(image_rgb)
            if encodings:
                known_encodings.append(encodings[0])
                known_names.append(os.path.splitext(filename)[0])
            else:
                print(f"No face found in {filename}")

    return known_encodings, known_names

def recognize_face(frame, known_encodings, known_names):
    # Handle images with alpha channel (4 channels)
    if len(frame.shape) == 3 and frame.shape[2] == 4:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Ensure dtype is uint8
    if rgb_frame.dtype != np.uint8:
        rgb_frame = rgb_frame.astype(np.uint8)

    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_enc
