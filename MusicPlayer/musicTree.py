import tkinter
from tkinter import ttk
import os
import time
import pygame


class TreeWindows(tkinter.Frame):

    songlist = []

    def __init__(self, master, path):
        self.path = path
        frame = tkinter.Frame(master)
        frame.pack(side=tkinter.LEFT, fill=tkinter.Y)
        self.label = tkinter.Label(frame,
                                   text="所有歌曲",
                                   bg="green",
                                   fg="white",
                                   font=("华文琥珀", 15))
        self.label.pack(fill=tkinter.X)
        self.tree = ttk.Treeview(frame)
        self.tree.pack(fill=tkinter.Y, side=tkinter.LEFT)

        # text=os.path.splitext()将路径最后一级分离出来 windows不支持
        root = self.tree.insert("", "end", text=self.getPath(path), open=True, values=(path))

        # 加载所有树枝
        self.loadTree(root, path)

        # 添加滚动条
        self.sy = tkinter.Scrollbar(frame)
        self.sy.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        self.sy.config(command=self.tree.yview)
        self.tree.config(yscrollcommand=self.sy.set)

        # 绑定事件
        self.tree.bind("<<TreeviewSelect>>", self.func)

    def func(self, event):
        self.v = event.widget.selection()
        for sv in self.v:
            file = self.tree.item(sv)["text"]
            absPath = os.path.join(self.path, file)
            pygame.mixer.init()
            if absPath != r"C:\Users\Administrator\Desktop\python基础\音乐播放器\歌曲\歌曲":
                track = pygame.mixer.music.load(absPath)
                pygame.mixer.music.play()

    def loadTree(self, father, fatherPath):
        # 遍历所有目录
        for filename in os.listdir(fatherPath):
            absPath = os.path.join(fatherPath, filename)
            # 插入树枝
            treey = self.tree.insert(father, "end", text=self.getPath(absPath), values=(absPath))
            # 判断是否是目录
            if os.path.isdir(absPath):
                # 递归
                self.loadTree(treey, absPath)
            else:
            # 为歌曲则加入播放列表
                self.songlist.append(absPath)

    def getPath(self, path):
        pathList = os.path.split(path)
        return pathList[-1]

