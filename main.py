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

    video_quality = input("Enter 1 for 1080p ,l for low quality ,b for best quality: ").strip().lower()

    if video_quality == "1":
        video_format = "bestvideo[height<=1080]+bestaudio/best"

    elif video_quality == "l":
        video_format = "worstvideo+bestaudio/best"

    elif video_quality == "b":
        video_format = "bestvideo+bestaudio/best"

    else:
        print("Invalid choice, defaulting to 1080p.")
        video_format = "bestvideo[height<=1080]+bestaudio/best"

    return USER_URL, video_format


def is_valid_url(user_URL):

    try:
        result = urlparse(user_URL)
        return all([result.scheme in ("http", "https"), result.netloc])
    except:
        return False



def main(USER_URL, video_format):

    if not is_valid_url(USER_URL):
        print("Invalid URL")
        return

    ydl_opts = {
        'format': video_format,
        'merge_output_format': 'mp4',
        'ffmpeg_location': ffmpeg_path,
        'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),  # save in folder
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([USER_URL])

if __name__ == "__main__":

    USER_URL, video_format = USER_INPUT()
    main(USER_URL, video_format)

