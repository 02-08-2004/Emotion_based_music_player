"""
Generate short CC0-like WAV samples into each emotion folder under `songs/`.
This script creates simple sine wave tones (WAV, 16-bit PCM) for demo and testing.

Usage:
    python generate_samples.py

It will create one or two short WAV files per folder if none exist.
"""

import os
import wave
import struct
import math

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SONGS_DIR = os.path.join(BASE_DIR, "songs")

EMOTION_FREQ = {
    "happy": 880,
    "sad": 220,
    "angry": 440,
    "neutral": 330,
    "surprised": 1320,
}


def make_sine_wav(path, freq=440, duration=1.5, rate=22050, amp=0.5):
    n_samples = int(duration * rate)
    with wave.open(path, "w") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)  # 16-bit
        wf.setframerate(rate)
        for i in range(n_samples):
            t = float(i) / rate
            val = amp * math.sin(2.0 * math.pi * freq * t)
            # 16-bit PCM
            data = struct.pack("<h", int(val * 32767.0))
            wf.writeframesraw(data)
        wf.writeframes(b"")


def generate_for_all():
    if not os.path.isdir(SONGS_DIR):
        print("No songs directory found:", SONGS_DIR)
        return
    for emo in sorted(os.listdir(SONGS_DIR)):
        emo_dir = os.path.join(SONGS_DIR, emo)
        if not os.path.isdir(emo_dir):
            continue
        # check for existing audio files
        existing = [
            f for f in os.listdir(emo_dir) if f.lower().endswith((".mp3", ".wav"))
        ]
        if existing:
            print(f"Skipping {emo}: already has {len(existing)} audio file(s)")
            continue
        freq = EMOTION_FREQ.get(emo.lower(), 440)
        out1 = os.path.join(emo_dir, f"{emo}_sample1.wav")
        out2 = os.path.join(emo_dir, f"{emo}_sample2.wav")
        print(f"Generating samples for {emo}: {out1}, {out2}")
        make_sine_wav(out1, freq=freq, duration=1.5)
        make_sine_wav(out2, freq=int(freq * 1.5), duration=1.2)


if __name__ == "__main__":
    generate_for_all()
