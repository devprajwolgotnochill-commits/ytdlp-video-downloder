# YouTube Video Downloader

A simple tool to download YouTube **videos or playlists** with **custom quality selection**.  
Works with both **Python script** (`main.py`) and **standalone .exe version** (no setup needed).

---

## 🚀 Features

- ✅ Download **single videos** or **full playlists**
- ✅ Choose download quality:
  - `1` → 1080p (max available)
  - `l` → Lowest video quality + best audio
  - `b` → Best video + best audio
- ✅ **Video / Audio-only selection**
- ✅ Automatically creates `downloaded_videos` folder
- ✅ Uses **yt-dlp + ffmpeg** to merge video & audio into MP4

---

## 📦 Installation & Usage

### 🟢 Option 1: Windows `.EXE` (No Python Needed)

Just download and run:

🔗 **Download v1.1 (.exe)** →  
https://github.com/devprajwolgotnochill-commits/ytdlp-video-downloder/releases/download/v1.1/main.exe

> ✅ No installation required — double-click and start downloading!

---

### 🐍 Option 2: Python Script

#### Requirements

- Python 3.x
- yt-dlp
- imageio-ffmpeg

Install dependencies:

```bash
pip install -r requirements.txt
