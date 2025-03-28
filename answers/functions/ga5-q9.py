# /// script
# requires-python = ">=3.9"
# dependencies = ["yt-dlp"]
# ///

import yt_dlp

def download_audio(url: str) -> None:
    """Download audio at speech-optimized quality."""
    ydl_opts = {
        'format': 'ba[abr<50]/worstaudio',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '32'
        }]
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Example usage
download_audio('https://www.youtube.com/watch?v=VIDEO_ID')