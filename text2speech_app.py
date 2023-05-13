# -*- coding: utf-8 -*-
"""
Created on Sat May 13 09:32:23 2023

@author: ElaheMsvi
"""

import streamlit as st
from gtts import gTTS
from io import BytesIO
import base64


def text_to_speech(text, lang):
    # Create a gTTS object to convert the text to speech
    tts = gTTS(text=text, lang=lang)

    # Save the audio output as a BytesIO object
    audio_bytes = BytesIO()
    tts.write_to_fp(audio_bytes)
    audio_bytes.seek(0)

    return audio_bytes


# Set the default language to English
lang = 'en'

# Create a Streamlit app
st.title("Text-to-Speech")

# Create a text input for the user to enter their text
text_input = st.text_input("Enter your text here:")

# Create a language selection dropdown for the user to choose the language
lang = st.selectbox("Select language:", ['en', 'es', 'fr', 'de', 'it'])

# Create a "Generate Speech" button
if st.button("Generate Speech"):
    # Call the text_to_speech function to generate the audio output
    audio_bytes = text_to_speech(text_input, lang)

    # Create a download link for the audio output
    b64 = base64.b64encode(audio_bytes.read()).decode()
    href = f'<a href="data:audio/mp3;base64,{b64}" download="output.mp3">Download audio</a>'
    st.markdown(href, unsafe_allow_html=True)

    # Play the audio output
    st.audio(audio_bytes, format='audio/mp3')
