import shutil
from pytubefix import YouTube


yt = YouTube(input('URL'))
print(yt.title)

ys = yt.streams.get_audio_only().download(mp3=True)

caminho_ori = f'D:\Codigos\BaixarMusicas_TKinter\{yt.title}.mp3'
caminho_dest = 'D:\Codigos\BaixarMusicas_TKinter\Musicas'
shutil.move(caminho_ori, caminho_dest)