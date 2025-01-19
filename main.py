import streamlit as st
import openai
from pytube import YouTube
import os
import shutil
from dotenv import load_dotenv
import whisper
from zipfile import ZipFile

load_dotenv()

# Set the OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

@st.cache

def load_model():
    model = whisper.load_model("base")
    return model
    

def save_audio(url):
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    
    out_file = video.download()     # Download the file
    root, ext = os.path.splitext(out_file)
    
    file_name = root + ".mp3"
    
    try: 
        os.rename(out_file, file_name)  # Rename the file
    except OSError as e:
        os.remove(file_name)
        os.rename(out_file, file_name)
    
    audio_filename = Path(file_name).stem + ".mp3"
    
    print(f"{yt.title} has been successfully downloaded")     # Success message
    print(file_name)
    
    return yt.title, audio_filename


def save_audio_to_transcript(audio_file):
    model = load_model()
    
    result = model.transcribe(audio_file)
    transcript = result["text"]
    
    return transcript

#write the streamlit code (frontend for prototyping)

