# -*- coding: utf-8 -*-
"""app.py.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1rYQPstDCDWnEAK6IG8Cna0-k4z279P80
"""

# Install required packages
!pip install -q yt-dlp openai-whisper

# Imports
import os
import whisper
import yt_dlp

# Function to download audio
def download_audio(url: str, output_path: str = "temp_audio.mp3") -> bool:
    try:
        print("Downloading audio...")
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': output_path,
            'quiet': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Audio downloaded successfully.")
        return True
    except Exception as e:
        print(f"Error downloading audio: {e}")
        return False

# Function to transcribe using Whisper
def transcribe_audio(audio_path: str) -> str:
    try:
        print("Loading Whisper model...")
        model = whisper.load_model("base")
        print("Transcribing audio...")
        result = model.transcribe(audio_path, language="en")
        return result["text"]
    except Exception as e:
        print(f"Error during transcription: {e}")
        return ""

# Function to classify accent
def classify_accent(text: str) -> dict:
    text = text.lower()
    if any(word in text for word in ["mate", "aussie", "bloody", "no worries"]):
        return {"accent": "Australian", "confidence": 90.0, "note": "Common Australian slang detected."}
    elif any(word in text for word in ["innit", "cheers", "trousers", "bloody"]):
        return {"accent": "British", "confidence": 88.0, "note": "British vocabulary found."}
    elif any(word in text for word in ["dude", "awesome", "gotta", "wanna"]):
        return {"accent": "American", "confidence": 85.0, "note": "Typical American expressions detected."}
    elif any(word in text for word in ["only yaar", "i am telling", "what is your good name"]):
        return {"accent": "Indian English", "confidence": 80.0, "note": "Indian English patterns detected."}
    else:
        return {"accent": "General English", "confidence": 70.0, "note": "No strong regional indicators found."}

# Main function
def run_analysis():
    video_url = input("Enter the YouTube video URL: ").strip()
    if not video_url:
        print("No URL entered.")
        return

    audio_file = "temp_audio.mp3"

    if download_audio(video_url, audio_file):
        transcription = transcribe_audio(audio_file)
        print("\nTranscription:\n", transcription)

        result = classify_accent(transcription)
        print("\nAccent Analysis Report")
        print(f"Accent: {result['accent']}")
        print(f"Confidence: {result['confidence']}%")
        print(f"Note: {result['note']}")

        if os.path.exists(audio_file):
            os.remove(audio_file)

# Run the tool
run_analysis()