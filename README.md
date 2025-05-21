# YouTube English Accent Analyzer

This project is a simple web-based tool built with Streamlit that accepts a public YouTube video URL, extracts and transcribes the spoken English audio using OpenAI's Whisper model, and classifies the accent (e.g., British, American, Australian, Indian).

---

## Features

- Audio extraction from YouTube videos using `yt-dlp`.
- High-quality speech-to-text transcription using the Whisper model (`base` or higher).
- Keyword-based accent classification:
  - British English
  - American English
  - Australian English
  - Indian English
  - General English (if no strong indicators)
- Confidence score (0–100%) for how clearly the accent matches.
- Short explanation or reasoning provided in the output.
- Interactive Streamlit web interface.

---

## Getting Started

### 1. Clone the repository:

```bash
git clone https://github.com/ahmedmohamedabdelsalam/accent-analyzer.git
cd accent-analyzer
