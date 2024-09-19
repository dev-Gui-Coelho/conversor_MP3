from tkinter import *
from tkinter import ttk

class MyApp:
    def __init__(self):
        self.__create_window()
        self.__var()
        self.__widgets()
        self.__loop()

    def __create_window(self):
        self.window = Tk()
        self.window.geometry("550x328")
        self.window.resizable(False,False)
        self.window.config(bg='#1E1E1E')
        self.window.title('Conversor MP3')
        
    def __var(self):
        self.var_url = StringVar(self.window)
        # print(self.var_url.get())
    def __widgets(self):
        txt_title = Label(self.window, text='Conversor MP3', fg='#fff', bg='#1E1E1E', font=("Arial", 15) ).place(x=200, y=30)
        #URL#
        self.txt_url = Label(self.window, text='URL:', fg='#fff', bg='#1E1E1E', font=("Arial", 12), ).place(x=80, y=80)
        self.ipt_url = Entry(self.window, width=60,textvariable=self.var_url)
        self.ipt_url.place(x=140, y=80)
        #BTNs#
        btn_baixar = Button(self.window, text='Baixar', width=20, height=1, cursor='hand2')
        btn_baixar.place(x=180, y=120)
        self.btn_histo = Button(self.window, text='Historico', width=20, height=1, cursor='hand2', command=self.__historico)
        self.btn_histo.place(x=300, y=120)
        #Historico#
        

    def __historico(self):
        window_2 = Tk()
        self.table = ttk.Treeview(window_2,selectmode='browse', columns=('coluna0','coluna1', 'coluna2'), show='headings')
        self.table.place(x=100, y=150)
        self.table.column('coluna0', width=60, minwidth=60, stretch=NO)
        self.table.heading('#1', text='ID')
        self.table.column('coluna1', width=190, minwidth=120, stretch=NO)
        self.table.heading('#2', text='NOME')
        self.table.column('coluna2', width=140, minwidth=120, stretch=NO)
        self.table.heading('#3', text='DATA')
        window_2.mainloop()
    def __loop(self):
        self.window.mainloop()

    
MyApp()