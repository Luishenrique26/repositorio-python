from tkinter import Tk


class ListarActivies:
    def __init__(self, master: Tk):
        self.master = master
        self.master.title("Lista de atividades")
        self.master.geometry("300x300")
        self.master.resizable(False, False)
