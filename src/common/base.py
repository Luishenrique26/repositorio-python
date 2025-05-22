from tkinter import Tk


class TkinterBase:

    def __init__(self, master: Tk) -> None:
        self.master = master


    def open_window(self, window=None, destroy=False):
        if not destroy:
            self.master.destroy()
        new_window = Tk()
        window(new_window)
        return