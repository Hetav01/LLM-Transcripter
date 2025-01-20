import streamlit as st
import openai
from openai import OpenAI
# from config import OPENAI_API_KEY
# from pytube import YouTube
# import yt_dlp
import os
import shutil
from dotenv import load_dotenv
import whisper
from zipfile import ZipFile
from pytubefix import YouTube
from pathlib import Path
import time

load_dotenv()



# Set the OpenAI API key
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("Missing OPENAI_API_KEY. Set it as an environment variable.")

@st.cache_data

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
 
# tried with yt_dlp
# def save_audio(url):
#     ydl_opts = {
#         'format': 'bestaudio/best',
#         'outtmpl': '%(title)s.%(ext)s',
#         'postprocessors': [{
#             'key': 'FFmpegExtractAudio',
#             'preferredcodec': 'mp3',
#             'preferredquality': '192',
#         }],
#     }

#     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         info_dict = ydl.extract_info(url, download=True)
#         file_name = ydl.prepare_filename(info_dict)
#         root, ext = os.path.splitext(file_name)
#         audio_filename = root + ".mp3"
    
#     return info_dict['title'], audio_filename



def save_audio_to_transcript(audio_file):
    model = load_model()
    
    result = model.transcribe(audio_file)
    transcript = result["text"]
    
    return transcript

def text_to_Article(text):
    # deprecated...
    #
    # response = openai.ChatCompletion.create(
    #     model="gpt-3.5-turbo",
    #     messages=[
    #         {"role": "system", "content": "You are a helpful assistant."},
    #         {"role": "user", "content": "Write a news article in 500 words from the below text: \n" + text}
    #     ],
    #     temperature=0.7,
    #     max_tokens=600,
    #     top_p=1,
    #     frequency_penalty=0,
    #     presence_penalty=0
    # )
    
    # return response["choices"][0]["text"]
    
    client = OpenAI(
        api_key=api_key
    )
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Write a news article in 500 words from the below text: \n" + text}
        ],
        temperature=0.7,
        max_tokens=600,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    
    return response.choices[0].message.content

#write the streamlit code (frontend for prototyping)

st.markdown("# **YouTube video to Transcript Converter**")

st.header("**Enter the YouTube video URL**")
url_link = st.text_input("Enter the video URL here: ")

def typewriter_streamlit(text: str, speed: int):
    tokens = text.split()
    container = st.empty()
    for index in range(len(tokens) + 1):
        curr_full_text = " ".join(tokens[:index])
        container.markdown(curr_full_text)
        time.sleep(1 / speed)

if st.checkbox("Start Analysis"):
    video_title, audio_filename = save_audio(url_link)
    st.audio(audio_filename)
    
    transcript = save_audio_to_transcript(audio_filename)
    
    st.header("Transcripts are being extracted...")
    transcriptGenerated = typewriter_streamlit(text=transcript, speed=25)
    st.success(transcriptGenerated)
    st.success("Transcripts have been extracted successfully!") 
    
    result = text_to_Article(transcript)
    st.success(result)
    st.success("The article has been generated successfully!")
    
