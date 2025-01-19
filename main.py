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

def load_model():
    model = whisper.load_model("base")
    return model
    

def save_audio(url):
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    
    out_file = video.download()     # Download the file
    root, ext = os.path.splitext(out_file)
    
    file_name = root + ".mp3"
    