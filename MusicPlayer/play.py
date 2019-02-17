import tkinter
import os
from musicTree import TreeWindows
from lyric import Lyric
from musicButton import MusicButton
import sys, time

win = tkinter.Tk()
win.title("Music Player")
win.geometry("600x700+300+100")

path = r"E:\CloudMusic"

frameL = tkinter.Frame(win)
frameL.pack(fill=tkinter.Y, side=tkinter.LEFT)

frameR = tkinter.Frame(win)
frameR.pack(fill=tkinter.Y, side=tkinter.RIGHT)

ly = Lyric(frameR)
ly.vis()
treeWin = TreeWindows(frameL, path)
button = MusicButton(frameR, path, treeWin.songlist)

win.mainloop()

