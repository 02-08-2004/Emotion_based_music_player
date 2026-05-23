# Emotion-based Music Player (minimal)

This repository contains a minimal structure and a small `main.py` to demonstrate an emotion-based music player layout.

Structure created:

- `main.py` — simple CLI to list and play songs
- `songs/happy/happy1.mp3`, `songs/happy/happy2.mp3`
- `songs/sad/sad1.mp3`
- `songs/angry/angry1.mp3`
- `songs/neutral/neutral1.mp3`
- `songs/surprised/surprise1.mp3`

Usage

1. (Optional) Create a virtual environment and install requirements:

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1; pip install -r requirements.txt
```

2. List available emotions:

```powershell
python main.py --list
```

3. Play a random song from an emotion:

```powershell
python main.py --emotion happy
```

4. Let the app pick a random emotion and play from it:

```powershell
python main.py --pick
```

5. Launch the simple GUI (Tkinter):

```powershell
python main.py --gui
```

Notes

- The repo includes placeholder MP3 files (text placeholders). Replace them with real MP3 files you have rights to.
 - Playback uses `pygame`. Install dependencies with `pip install -r requirements.txt`.
 - Generate short demo WAV samples (sine tones) into each `songs/<emotion>/` folder by running:

```powershell
python generate_samples.py
```

	This creates small WAV files for demo/testing; you should replace them with real CC-licensed audio you have rights to if needed.
