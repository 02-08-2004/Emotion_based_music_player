# Emotion-Based Music Player

A Streamlit web application that detects emotions from uploaded images and plays corresponding mood-based music.

## Features

- 📸 **Face Emotion Detection**: Uses FER (Facial Expression Recognition) with MTCNN for accurate emotion detection
- 🎵 **Music Playback**: Plays music based on detected emotions (happy, sad, angry, neutral, surprised)
- 🎨 **Web Interface**: Built with Streamlit for an intuitive user experience
- 🔐 **Privacy-Focused**: Analyzes images locally without storing data

## Project Structure

```
.
├── main.py                 # Streamlit web application
├── generate_samples.py     # Script to generate demo WAV samples
├── requirements.txt        # Python dependencies
├── README.md              # This file
└── songs/
    ├── happy/             # Happy mood songs
    ├── sad/               # Sad mood songs
    ├── angry/             # Angry mood songs
    ├── neutral/           # Neutral mood songs
    └── surprised/         # Surprised mood songs
```

## Installation

1. **Install dependencies**:

```powershell
pip install -r requirements.txt
```

Or install manually:

```powershell
pip install streamlit fer opencv-python-headless numpy pillow pygame
```

2. **(Optional) Generate demo audio samples**:

```powershell
python generate_samples.py
```

This creates sine wave WAV files for testing. Replace with real CC-licensed audio for production use.

## Usage

Launch the Streamlit app:

```powershell
python -m streamlit run main.py
```

The app will open in your browser at `http://localhost:8502`

### How to Use

1. Upload a clear face image (JPG, JPEG, or PNG)
2. Check the permission box in the sidebar
3. Click **Detect Emotion & Play Song 🎵**
4. The app detects your emotion and plays a corresponding song

## Notes

- **Supported Emotions**: Happy, Sad, Angry, Neutral, Surprised
- **Image Requirements**: Clear front-facing face for best results
- **Audio Files**: The `songs/` folders contain demo MP3 and WAV files. For production, replace with real CC-licensed audio you have rights to
- **Fallback**: If emotion detection fails or an emotion is not recognized, the app falls back to "neutral" music
- **Privacy**: Images are analyzed locally and not stored or transmitted
