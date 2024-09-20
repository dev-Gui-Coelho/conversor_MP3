from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os 
from pytube import YouTube
from moviepy.editor import *

class MyApp:
    def __init__(self, url:str = None):
        self.__url = url
        self.__create_window()
        self.__var()
        self.__widgets()
        self.__loop()

    def __create_window(self) -> None:
        self.window = Tk()
        self.window.geometry("550x328")
        self.window.resizable(False,False)
        self.window.config(bg='#1E1E1E')
        self.window.title('Conversor MP3')
        
    def __var(self) -> str:
        self.var_url = StringVar(self.window)
        self.__url = self.var_url
    
    def get_url(self):
        return self.__url.get()
    
    def __widgets(self):
        txt_title = Label(self.window, text='Conversor MP3', fg='#fff', bg='#1E1E1E', font=("Arial", 15) ).place(x=200, y=30)
        #URL#
        # var_url = StringVar(self.window)
        # self.url = var_url
        txt_url = Label(self.window, text='URL:', fg='#fff', bg='#1E1E1E', font=("Arial", 12), ).place(x=80, y=80)
        self.ipt_url = Entry(self.window, width=60,textvariable=self.var_url)
        self.ipt_url.place(x=140, y=80)
        #BTNs#
        btn_baixar = Button(self.window, text='Baixar', width=20, height=1, cursor='hand2', command=self.__baixar)
        btn_baixar.place(x=120, y=120)
        btn_histo = Button(self.window, text='Historico', width=20, height=1, cursor='hand2', command=self.__historico)
        btn_histo.place(x=320, y=120)
        btn_sair = Button(self.window, text='Sair', width=10, height=1, cursor='hand2', command=self.sair)
        btn_sair.place(x=450, y=280)
        
    

    def __historico(self) -> None:
        window_2 = Tk()
        window_2.geometry('430x260')
        table = ttk.Treeview(window_2,selectmode='browse', columns=('coluna0','coluna1', 'coluna2'), show='headings')
        table.place(x=17, y=20)
        table.column('coluna0', width=60, minwidth=60, stretch=NO)
        table.heading('#1', text='ID')
        table.column('coluna1', width=190, minwidth=120, stretch=NO)
        table.heading('#2', text='NOME')
        table.column('coluna2', width=140, minwidth=120, stretch=NO)
        table.heading('#3', text='DATA')

        window_2.mainloop()

    def __loop(self) -> None:
        self.window.mainloop()

    def sair(self) -> None:
        if messagebox.askyesno('Sair', 'Deseja sair?'):
            self.window.destroy()
    
    def __baixar(self):
        # teste = self.get_url()
        # print(teste)
        # video = YouTube(self.get_url())
        # print(video.title)
        # steam = video.streams.filter(only_audio=True).first()
        # steam = video.streams.get_highest_resolution().download()
        # name = steam.replace("D:\Codigos\BaixarMusicas_TKinter\\", '')
        # name = steam.replace(".mp4", '')
        # file = AudioFileClip(f'{steam}')
        # file.write_audiofile(f'{name}.mp3')
        # file.close()
        # os.unlink(steam)
        # os.unlink(f'{name}.mp3')
        # print(self.get_url())
        pass

MyApp()