import streamlit as st
import openai
# from pytube import YouTube
# import yt_dlp
import os
import shutil
from dotenv import load_dotenv
import whisper
from zipfile import ZipFile

load_dotenv()

# Set the OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

@st.cache_data

def load_model():
    model = whisper.load_model("base")
    return model
    

# def save_audio(url):
#     yt = YouTube(url)
#     video = yt.streams.filter(only_audio=True).first()
    
#     out_file = video.download()     # Download the file
#     root, ext = os.path.splitext(out_file)
    
#     file_name = root + ".mp3"
    
#     try: 
#         os.rename(out_file, file_name)  # Rename the file
#     except OSError as e:
#         os.remove(file_name)
#         os.rename(out_file, file_name)
    
#     audio_filename = Path(file_name).stem + ".mp3"
    
#     print(f"{yt.title} has been successfully downloaded")     # Success message
#     print(file_name)
    
#     return yt.title, audio_filename

def save_audio(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        file_name = ydl.prepare_filename(info_dict)
        root, ext = os.path.splitext(file_name)
        audio_filename = root + ".mp3"
    
    return info_dict['title'], audio_filename


def save_audio_to_transcript(audio_file):
    model = load_model()
    
    result = model.transcribe(audio_file)
    transcript = result["text"]
    
    return transcript

#write the streamlit code (frontend for prototyping)

st.markdown("# **YouTube video to Transcript Converter**")

st.header("**Enter the YouTube video URL**")
url_link = st.text_input("Enter the video URL here: ")

if st.checkbox("Start Analysis"):
    video_title, audio_filename = save_audio(url_link)
    st.audio(audio_filename)


