import streamlit as st
import openai
from openai import OpenAI
# from pytube import YouTube
# import yt_dlp
import os
import shutil
from dotenv import load_dotenv
from zipfile import ZipFile
from pytubefix import YouTube
from pathlib import Path
import time

from transcriptHelper import save_audio, save_audio_to_transcript

load_dotenv()



# Set the OpenAI API key
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("Missing OPENAI_API_KEY. Set it as an environment variable.")

@st.cache_data


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
            {"role": "user", "content": f"Write a news article in 500 words from the below text: {text}\n. Make sure to bold the title."}
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
    
    
    #write the code to save and download the transcript and article
    transcript_txt = open("transcript.txt", "w")
    transcript_txt.write(transcript)
    transcript_txt.close()
    
    article_txt = open("article.txt", "w")
    article_txt.write(result)
    article_txt.close()
    
    zip_file = ZipFile("output.zip", "w")
    zip_file.write("transcript.txt")
    zip_file.write("article.txt")
    zip_file.close()
    
    with open("output.zip", "rb") as zip_download:
        download_btn = st.download_button(
            data= zip_download,
            file_name= "output.zip",
            label= "Download (in .zip)",
            mime= "application/zip"
        )        
