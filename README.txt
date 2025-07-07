# 🗣️ Dialect Translator App

A smart web app that:
- 🎙️ Captures speech in dialects like Hindi, Tamil, Bengali, etc.
- ✍️ Corrects grammar and improves fluency
- 🌐 Translates to fluent US English (or any supported language)
- 🔊 Plays back translated speech
- 📁 Exports transcripts
- 🪟 Shows real-time subtitle overlay (CC-style)

## 🌟 Live Demo

👉 [Streamlit Cloud App](https://your-streamlit-app-url)

---

## 🔧 Features

- 🎤 **Speech Recognition** (Indian English, Hindi, etc.)
- 🧠 **Grammar Correction** using LanguageTool
- 🌍 **Smart AI Translation** using Cohere or Google Translate
- 🔊 **Text-to-Speech (TTS)** in the selected output dialect
- 🪟 **Live Subtitle Overlay** for meetings
- 📦 Deploy-ready with `requirements.txt` and `.streamlit/secrets.toml`

---

## 🚀 How to Run Locally

```bash
git clone https://github.com/Sanjitadas/dialect-translator.git
cd dialect-translator

# (Optional) Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

pip install -r requirements.txt

# Set API Key (if not using Streamlit secrets)
export COHERE_API_KEY=your-key-here

streamlit run app.py
