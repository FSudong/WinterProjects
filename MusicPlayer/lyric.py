import tkinter
import os


class Lyric(tkinter.Frame):
    def __init__(self, master):
        frame = tkinter.Frame(master)
        frame.pack(side=tkinter.TOP, fill=tkinter.Y)

        self.label = tkinter.Label(frame,
                                   text="",
                                   bg="green",
                                   fg="white",
                                   font=("华文琥珀", 15))
        self.label.pack(fill=tkinter.X)
        self.txt = tkinter.Text(frame,
                                width=100,
                                height=34,
                                bg="green",
                                fg="white")
        self.txt.pack(side=tkinter.TOP, fill=tkinter.Y)

    def vis(self):
        str = "\n\n\n\n\n\n\n\t\t\t\tMP3 player"
        self.txt.insert(tkinter.INSERT, str)
