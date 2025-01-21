# 📰 LLaMe NEWS: AI-Powered News Article Generator

## 📌 Overview
LLaMe NEWS is an AI-powered tool that extracts audio from YouTube videos, transcribes the content using OpenAI Whisper, and generates well-structured news articles using OpenAI's GPT-3.5 Turbo. The project provides an interactive web interface built with Streamlit, making it easy to use.

## ✨ Features
- 🎥 Download and extract audio from YouTube videos
- 📝 Generate accurate transcripts using OpenAI Whisper
- 📰 Convert transcripts into structured news articles
- 💻 Streamlit-based UI for seamless interaction
- 📂 Downloadable transcript and article files in a ZIP format

## 🔧 Prerequisites
Before setting up the project, ensure you have the following installed:

- **Python 3.8+**
- **pip or pip3** (Python package manager)
- **Virtual environment** (recommended)
- **OpenAI API Key**

## 🚀 Setup Instructions

### 📥 Step 1: Clone the Repository
```sh
git clone <your-repository-url>
cd <your-repository-folder>
```

### 🌐 Step 2: Create a Virtual Environment (Recommended)
#### On macOS/Linux
```sh
python3 -m venv venv
source venv/bin/activate
```
#### On Windows
```sh
python -m venv venv
venv\Scripts\activate
```

### 📦 Step 3: Install Dependencies
```sh
pip install -r requirements.txt
```

### 🔑 Step 4: Set Up OpenAI API Key
#### On macOS/Linux
```sh
export OPENAI_API_KEY="your-api-key-here"
```
#### On Windows (PowerShell)
```powershell
$env:OPENAI_API_KEY="your-api-key-here"
```

Alternatively, create a `.env` file in the root directory and add:
```
OPENAI_API_KEY=your-api-key-here
```

### ▶️ Step 5: Run the Application
```sh
streamlit run main.py
```

## 📖 Usage Guide
1. 🔗 Enter a YouTube video URL in the input field.
2. ✅ Click the checkbox to start the analysis.
3. ⏳ Wait for the audio extraction and transcription.
4. 📰 The generated news article will appear on the screen.
5. 📥 Download the transcript and article as a `.zip` file.

## 🛠 Troubleshooting
- **Missing Dependencies?** Run `pip install -r requirements.txt` again.
- **API Key Not Found?** Ensure it's set in the environment or `.env` file.
- **Streamlit Not Running?** Check for errors and ensure you activated the virtual environment.

## 🏗 Technologies Used
- **🐍 Python** (Core Programming Language)
- **🌐 Streamlit** (Web Framework for UI)
- **🤖 OpenAI GPT-3.5 Turbo** (Article Generation)
- **🎙 OpenAI Whisper** (Audio Transcription)
- **📹 PytubeFix** (YouTube Audio Extraction)

## ❗ Known Issues
### `pytubefix.exceptions.BotDetection: sVGg90hukLI This request was detected as a bot.`

![Bug Image](https://github.com/Hetav01/LLaMe-Transcripter/blob/main/BotBug)

This error occurs when YouTube detects automated access to its content and blocks the request. This issue is common with `pytubefix`, as YouTube regularly updates its bot detection mechanisms. Possible workarounds include:
- Using a VPN or proxy to change your IP address.
- Implementing a delay between requests to mimic human behavior.
- Using an alternative method for downloading YouTube audio, such as `yt-dlp`.
- Updating `pytubefix` to the latest version to check for fixes.

This issue is currently being investigated for a more permanent solution.

## 📜 License
This project is licensed under the MIT License.

## 👤 Author
**Hetav a.k.a GodSpeed**

---
🚀 Enjoy using **LLaMe NEWS** and revolutionize news generation! 📰✨
