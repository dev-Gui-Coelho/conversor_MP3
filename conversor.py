import os 
from pytube import YouTube
from moviepy.editor import *
import time

#  video = YouTube(values['url'])
#                 steam = video.streams.get_highest_resolution().download()
#                 name = steam.replace("D:\Codigos\Baixar_Musicas\\", '')
#                 name = steam.replace(".mp4", '')
#                 file = AudioFileClip(f'{steam}')
#                 file.write_audiofile(f'{name}.mp3')
#                 file.close()
#                 os.unlink(steam)
#                 os.unlink(f'{name}.mp3')