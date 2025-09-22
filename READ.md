# YouTube Video Downloader

A simple Python script to download YouTube videos or playlists with user-selected quality. Uses `yt-dlp` and `ffmpeg` to merge video and audio.

## Features

- Download a single video or entire playlist
- Choose video quality:
  - `1` → 1080p max
  - `l` → lowest video quality + best audio
  - `b` → best video + best audio
- Automatically creates a folder `downloaded_videos` for downloads
- Merges video and audio into MP4 format

## Requirements

- Python 3.x
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [imageio-ffmpeg](https://pypi.org/project/imageio-ffmpeg/)

Install dependencies:

```bash
pip install yt-dlp imageio-ffmpeg
