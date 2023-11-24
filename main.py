from __future__ import unicode_literals
from yt_dlp import YoutubeDL

links = ['https://www.youtube.com/watch?v=dQw4w9WgXcQ'
]

ydl_opts = {
    'download_archive': 'archive.txt',
    'ignoreerrors': True,
    'nooverwrites': True,
    'format': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]/best',
    'noplaylist' : False
}

with YoutubeDL(ydl_opts) as ydl:
    ydl.download(links)