# 📁 File: DialectApp/app.py

import streamlit as st
from utils.stt import start_listening, stop_listening
from utils.grammar_check import correct_grammar
from utils.tts import text_to_speech
from utils.translation import translate_text
from utils.export import export_transcript
from utils.overlay import show_subtitle_overlay
from utils.languages import LANGUAGES

st.set_page_config(page_title="🗣️ Dialect Translator", layout="centered")
st.title("🗣️ Dialect Translator")
st.markdown("Translate, correct, and subtitle spoken dialects live!")

# Select languages
source_lang = st.selectbox("🎙️ Input Language", list(LANGUAGES.keys()), key="src")
target_lang = st.selectbox("📝 Output Language", list(LANGUAGES.keys()), index=1, key="tgt")

src_lang_code = LANGUAGES[source_lang]
tgt_lang_code = LANGUAGES[target_lang]

# Buttons for listening
if "listening" not in st.session_state:
    st.session_state.listening = False
    st.session_state.live_subtitles = ""

if not st.session_state.listening:
    if st.button("🎤 Start Listening"):
        start_listening(lang=src_lang_code)
        st.session_state.listening = True
        st.info("🟡 Listening... Press 'Translate' to stop.")
else:
    if st.button("🛑 Translate"):
        recognized_text = stop_listening()
        st.session_state.listening = False

        if recognized_text:
            st.success("✅ Captured Voice Input")
            st.markdown(f"**🗒️ Recognized Text:**\n\n{recognized_text}")

            corrected_text = correct_grammar(recognized_text)
            st.markdown(f"**✍️ Corrected & Enhanced:**\n\n{corrected_text}")

            if src_lang_code != tgt_lang_code:
                translated = translate_text(corrected_text, src_lang_code, tgt_lang_code)
                st.markdown(f"**🌐 Translated Output:**\n\n{translated}")
            else:
                translated = corrected_text

            if st.button("🔊 Play Output"):
                text_to_speech(translated, tgt_lang_code)

            if st.button("💾 Export Transcript"):
                export_transcript(translated)
                st.success("📁 Transcript saved to output folder.")

            if st.button("🪟 Show Subtitle Overlay (CC Mode)"):
                show_subtitle_overlay(translated)
        else:
            st.error("❌ Nothing was captured from audio.")

# 🟢 Live Subtitle Simulation
if st.session_state.listening:
    with st.empty():
        import time
        while st.session_state.listening:
            live_text = " ".join(stop_listening().split()[-10:])  # Display last 10 words as subtitle
            st.markdown(f"**🟢 Live Subtitle:** {live_text}")
            time.sleep(3)













