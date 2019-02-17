import tkinter
import os
import pygame
import random


class MusicButton(tkinter.Frame):

    songlist = []

    def __init__(self, master, path, songlist):
        self.songlist = songlist
        self.path = path
        frame = tkinter.Frame(master)
        frame.pack(side=tkinter.TOP, fill=tkinter.X)

        self.label = tkinter.Label(frame)
        self.label.pack(fill=tkinter.X, side=tkinter.TOP)

        self.button1 = tkinter.Button(frame,
                                      text="上一曲",
                                      command=self.func1,
                                      width=8,
                                      height=2,
                                      bg="blue",
                                      fg="white",
                                      font=("华文琥珀", 8))
        self.button1.pack(side=tkinter.LEFT)

        self.button2 = tkinter.Button(frame,
                                      text="播放",
                                      command=self.func2,
                                      width=8,
                                      height=2,
                                      bg="blue",
                                      fg="white",
                                      font=("华文琥珀", 8))
        self.button2.pack(side=tkinter.LEFT)

        self.button3 = tkinter.Button(frame,
                                      text="暂停",
                                      command=self.func3,
                                      width=8,
                                      height=2,
                                      bg="blue",
                                      fg="white",
                                      font=("华文琥珀", 8))
        self.button3.pack(side=tkinter.LEFT)

        self.button4 = tkinter.Button(frame,
                                      text="下一曲",
                                      command=self.func4,
                                      width=8,
                                      height=2,
                                      bg="blue",
                                      fg="white",
                                      font=("华文琥珀", 8))
        self.button4.pack(side=tkinter.LEFT)

        # self.label = tkinter.Label(frame,
        #                            text="这  里  是  进  度  条 ……",
        #                            bg="light green",
        #                            fg="blue")
        self.label.pack(fill=tkinter.X, side=tkinter.BOTTOM)

    def func1(self):
        RandSongIndex = random.randint(0, len(self.songlist)-1)
        absPath = self.songlist[RandSongIndex]
        pygame.mixer.init()
        if absPath != r"C:\Users\Administrator\Desktop\python基础\音乐播放器\歌曲\歌曲":
            track = pygame.mixer.music.load(absPath)
            pygame.mixer.music.play()

    def func2(self):
        pygame.mixer.music.play()

    def func3(self):
        pygame.mixer.music.pause()

    def func4(self):
        self.func1()
