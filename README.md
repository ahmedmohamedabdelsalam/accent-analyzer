# 🎙️ YouTube English Accent Analyzer

This project is a Streamlit web app that downloads a YouTube video, extracts its audio, transcribes the speech using OpenAI's Whisper model, and then classifies the English accent (e.g., British, American, Australian, Indian) based on common linguistic patterns and expressions.

---

## 🔍 Features

- 🎧 **Audio Extraction**: Downloads and converts YouTube video audio automatically.
- 🧠 **Whisper Transcription**: Uses OpenAI's Whisper model (`large`) to accurately transcribe English speech.
- 🌍 **Accent Classification**:
  - British English 🇬🇧
  - American English 🇺🇸
  - Australian English 🇦🇺
  - Indian English 🇮🇳
  - General English (if no strong regional indicators found)
- 📊 **Confidence Score** and short **explanation/note** for transparency.
- 🖥️ **Streamlit UI**: Clean, interactive web interface.

---

## 🚀 Getting Started

### 1. Clone the repository:

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
