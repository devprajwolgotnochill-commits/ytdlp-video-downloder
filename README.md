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
pip install -r requirements.txt



output : --------------------------------------------------------------------------------------------------------------------
ytdlp-video-downloder> python .\main.py

Enter the Url of the video or playlist you want to download: https://www.youtube.com/watch?v=V9PVRfjEBTI
Enter 'v' for video, 'a' for audio-only: v
Enter 1 for 1080p, l for low quality, b for best quality: b
[youtube] Extracting URL: https://www.youtube.com/watch?v=V9PVRfjEBTI 
[youtube] V9PVRfjEBTI: Downloading webpage 
[youtube] V9PVRfjEBTI: Downloading tv simply player API JSON 
[youtube] V9PVRfjEBTI: Downloading tv client config 
[youtube] V9PVRfjEBTI: Downloading tv player API JSON 
[info] V9PVRfjEBTI: Downloading 1 format(s): 401+251 
[download] Destination: downloaded_videos\Billie Eilish - BIRDS OF A FEATHER (Official Music Video).f401.mp4 
[download]  72.2% of  260.44MiB at    3.61MiB/s ETA 00:20
