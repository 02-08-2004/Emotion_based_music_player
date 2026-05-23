import os
import random

import cv2
import numpy as np
from fer import FER
from PIL import Image

import streamlit as st

# ----------------- STREAMLIT PAGE CONFIG -----------------
st.set_page_config(
    page_title="Emotion-Based Music Player", page_icon="🎵", layout="centered"
)

# ----------------- EMOTION → SONG MAP -----------------
# Put your actual mp3 paths here
EMOTION_SONG_MAP = {
    "happy": ["songs/happy/happy1.mp3", "songs/happy/happy2.mp3"],
    "sad": ["songs/sad/sad1.mp3"],
    "angry": ["songs/angry/angry1.mp3"],
    "neutral": ["songs/neutral/neutral1.mp3"],
    "surprise": ["songs/surprised/surprise1.mp3"],
}

VALID_EMOTIONS = list(EMOTION_SONG_MAP.keys())


# ----------------- HELPER FUNCTIONS -----------------
@st.cache_resource
def load_fer_detector():
    # mtcnn=True is more accurate but slower; you can change if needed
    return FER(mtcnn=True)


def detect_emotion_from_image(image: Image.Image):
    """Takes a PIL image, returns (emotion, score) or (None, None)"""
    # Convert PIL image to OpenCV BGR format
    img_rgb = np.array(image.convert("RGB"))
    img_bgr = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)

    detector = load_fer_detector()
    top = detector.top_emotion(img_bgr)

    if top is None:
        return None, None

    emotion, score = top
    return emotion, score


def pick_song_for_emotion(emotion: str):
    """Pick a random song path for given emotion. Falls back to neutral."""
    if emotion not in EMOTION_SONG_MAP or len(EMOTION_SONG_MAP[emotion]) == 0:
        emotion = "neutral"

    songs = EMOTION_SONG_MAP[emotion]
    song_path = random.choice(songs)

    if not os.path.exists(song_path):
        return None  # file missing
    return song_path


# ----------------- UI -----------------
st.markdown(
    """
    <h1 style="text-align:center; color:#347deb;">Emotion-Based Music Player</h1>
    <hr style="height:4px; border:none; background:linear-gradient(90deg,#347deb,#3ad5c6); border-radius:4px;">
    """,
    unsafe_allow_html=True,
)

st.write(
    "### 😊 Upload your photo and let the app choose a song based on your emotion."
)

with st.sidebar:
    st.header("Controls")
    st.write(
        "1. Upload a clear face image\n2. Give permission\n3. Click **Detect & Play**"
    )

    permission = st.checkbox(
        "I allow this app to analyze my face emotion from the uploaded image.",
        value=False,
    )

uploaded_file = st.file_uploader(
    "Upload an image with your face (jpg / jpeg / png)", type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    # Show the uploaded image
    user_image = Image.open(uploaded_file)
    st.image(user_image, caption="Uploaded Image", use_column_width=True)

    if not permission:
        st.warning("Please check the permission box in the sidebar to continue.")
    else:
        if st.button("Detect Emotion & Play Song 🎵"):
            with st.spinner("Analyzing your emotion..."):
                emotion, score = detect_emotion_from_image(user_image)

            if emotion is None:
                st.error(
                    "Could not detect a clear face/emotion in this image. Try another one."
                )
            else:
                st.success(f"Detected emotion: **{emotion}** (confidence: {score:.2f})")

                # Normalize emotion name if needed
                emotion_key = emotion.lower()
                if emotion_key not in VALID_EMOTIONS:
                    st.info("Emotion not in predefined set, falling back to 'neutral'.")
                    emotion_key = "neutral"

                song_path = pick_song_for_emotion(emotion_key)

                if song_path is None:
                    st.error(
                        f"No valid audio file found for emotion '{emotion_key}'. "
                        "Check your song paths in EMOTION_SONG_MAP."
                    )
                else:
                    st.write(f"### Playing song for **{emotion_key}** mood:")
                    st.write(os.path.basename(song_path))

                    # Play song in browser
                    with open(song_path, "rb") as audio_file:
                        audio_bytes = audio_file.read()
                        st.audio(audio_bytes, format="audio/mp3")

else:
    st.info("Upload an image to get started.")
