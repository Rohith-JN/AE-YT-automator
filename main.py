from urllib.parse import urlencode
import requests
from pytube import YouTube
import os
from secrets import *

url_params = {
    "part": "snippet",
    "channelId": 'UC_aEa8K-EOJ3D6gOs7HcyNg',
    "key": api_key,
    "order": "date",
    "maxResults": 1,
    "type": "video"
}
req = f"https://www.googleapis.com/youtube/v3/search?{urlencode(url_params)}"
data = requests.get(req).json()
title = data['items'][0]['snippet']['title'].replace("&amp;", "&") + '.mp4'
videoId = data['items'][0]['id']['videoId']

def DownloadVideo(link):
    youtubeObject = YouTube(link)
    youtubeObject= youtubeObject.streams.get_audio_only()
    try:
        youtubeObject.download()
    except:
        pass

link = 'https://www.youtube.com/watch?v=' + videoId

files = os.listdir('D:\\Projects\\Python\\AE-YT-automator')
file = ''
for filename in files:
    if filename.endswith('.mp4'):
        file = filename

if os.path.exists(title) and title == file:
    pass
else:
    DownloadVideo(link)

if os.path.exists('Footage/audio.mp4'):
    os.remove('Footage/audio.mp4')
    os.rename(title, 'Footage/audio.mp4')
else:
    os.rename(title, 'Footage/audio.mp4')
    
# Todo Upload video to YouTube using Youtube Data API