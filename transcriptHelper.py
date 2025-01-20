from zipfile import ZipFile
from pytubefix import YouTube
from pathlib import Path
import whisper
import os


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

