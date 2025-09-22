import os
from urllib.parse import urlparse
import yt_dlp
import imageio_ffmpeg as ffmpeg

ffmpeg_path = ffmpeg.get_ffmpeg_exe()


download_folder = "downloaded_videos"

# Create the folder if it doesn't exist
os.makedirs(download_folder, exist_ok=True)

def USER_INPUT():
    # global USER_URL ,video_format
    while True:
        USER_URL = input("Enter the Url of the video or playlist you want to download: ")

        if is_valid_url(USER_URL):
            break
        print("Invalid URL. Please try again.")

    download_type = input("Enter 'v' for video, 'a' for audio-only: ").strip().lower()

    if download_type == "v":
        video_quality = input("Enter 1 for 1080p, l for low quality, b for best quality: ").strip().lower()

        if video_quality == "1":
            file_format = "bestvideo[height<=1080]+bestaudio/best"
        elif video_quality == "l":
            file_format = "worstvideo+bestaudio/best"
        elif video_quality == "b":
            file_format = "bestvideo+bestaudio/best"
        else:
            print("Invalid choice, defaulting to 1080p.")
            file_format = "bestvideo[height<=1080]+bestaudio/best"

    elif download_type == "a":
        file_format = "bestaudio/best"
    else:
        print("Invalid choice, defaulting to video 1080p.")
        file_format = "bestvideo[height<=1080]+bestaudio/best"
        download_type = "v"

    return USER_URL, file_format, download_type


def is_valid_url(user_URL):

    try:
        result = urlparse(user_URL)
        return all([result.scheme in ("http", "https"), result.netloc])
    except:
        return False



def main(USER_URL, file_format ,download_type):

    if not is_valid_url(USER_URL):
        
        return

    if download_type == "v":
            folder = download_folder
            ydl_opts = {
                'format': file_format,
                'merge_output_format': 'mp4',
                'ffmpeg_location': ffmpeg_path,
                'outtmpl': os.path.join(folder, '%(title)s.%(ext)s'),
                'noplaylist': False  # set True if you want only single video
        }
            
    else:  # audio-only
        folder = download_folder
        ydl_opts = {
            'format': file_format,
            'ffmpeg_location': ffmpeg_path,
            'outtmpl': os.path.join(folder, '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'noplaylist': False  # set True to download only single audio
        }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([USER_URL])

if __name__ == "__main__":

    USER_URL, file_format, download_type = USER_INPUT()
    main(USER_URL, file_format, download_type)

