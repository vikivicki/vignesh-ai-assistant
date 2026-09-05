import streamlit as st
from google import genai  # Modern Google Gemini SDK
from dotenv import load_dotenv
from gtts import gTTS
import whisper  # speech-to-text
import json
import os
import tempfile

load_dotenv()

# Gemini API Key configuration
gemini_api_key = st.secrets["GEMINI_API_KEY"]

st.set_page_config(
    page_title="Voice FAQ Bot",
    page_icon="🎙️",
    layout="centered"
)

st.title("🎙️ Voice FAQ Bot")
st.write("Ask a question using your voice or type it below.")

if not gemini_api_key:
    st.error("Gemini API key not found. Please check your key configuration.")
    st.stop()

# FIXED: Initialized the client exactly once with the key. Overwrite removed.
client = genai.Client(api_key=gemini_api_key)

with open("faq.json", "r", encoding="utf-8") as file:
    faq_data = json.load(file)

st.subheader("🎤 Voice Input")
audio = st.audio_input("Record your question")

voice_text = ""

if audio:
    st.success("✅ Recording received!")
    st.audio(audio)

    with st.spinner("🎧 Converting speech to text locally..."):
        try:
            # Save Streamlit audio to a temporary file for local Whisper to process
            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
                temp_audio.write(audio.read())
                temp_audio_path = temp_audio.name

            model_whisper = whisper.load_model("base")
            result = model_whisper.transcribe(temp_audio_path)
            voice_text = result["text"]

            st.subheader("📝 Speech-to-Text")
            st.info(voice_text)
            
            # Clean up the temporary file
            os.remove(temp_audio_path)

        except Exception as e:
            st.error("Speech-to-text failed.")
            st.error(str(e))

st.subheader("⌨️ Text Input")
typed_text = st.text_input("Type your question here:")

question = ""

if voice_text:
    question = voice_text
elif typed_text:
    question = typed_text


if st.button("🤖 Ask Question", use_container_width=True):
    if not question:
        st.warning("Please speak or type a question first.")
    else:
        st.subheader("❓ Your Question")
        st.write(question)

        faq_context = ""
        for item in faq_data:
            faq_context += (
                f"Question: {item['question']}\n"
                f"Answer: {item['answer']}\n\n"
            )

        with st.spinner("🤖 Gemini is finding the answer..."):
            try:
                prompt = f"""
You are a helpful FAQ assistant.

Answer the user's question using ONLY the FAQ information below.

If the answer is not available in the FAQ, respond exactly:
"Sorry, I don't have information about that in the FAQ."

Do not invent information.

FAQ:
{faq_context}

User question:
{question}
"""

                # FIXED: Changed syntax to client.models.generate_content 
                # FIXED: Set model to a valid production endpoint ("gemini-2.5-flash")
                response = client.models.generate_content(
                    model="gemini-3.6-flash",
                    contents=prompt,
                    config={"temperature": 0}
                )
                
                answer = response.text

                st.subheader("🤖 Answer")
                st.success(answer)

                st.subheader("🔊 Voice Answer")
                with st.spinner("🔊 Creating voice answer..."):
                    try:
                        tts = gTTS(text=answer, lang="en")
                        audio_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
                        audio_path = audio_file.name
                        audio_file.close()

                        tts.save(audio_path)
                        st.audio(audio_path, format="audio/mp3")
                    except Exception as e:
                        st.error("Text-to-speech failed.")
                        st.error(str(e))

            except Exception as e:
                st.error("Something went wrong while getting the answer from Gemini.")
                st.error(str(e))
