import tkinter

from IPython.terminal.pt_inputhooks import tk
from PIL import Image, ImageTk
from envs.mlbook.Lib import os


class gui:

    current = 0
    pics = []
    lbPic = None

    def __init__(self,path):
        # 创建tkinter应用程序窗口
        root = tkinter.Tk()
        # 设置窗口大小和位置
        root.geometry('430x650+40+30')
        # 不允许改变窗口大小
        root.resizable(False, False)
        # 设置窗口标题
        root.title('显示图片')
        # 获取当前文件夹中所有图片文件列表
        suffix = ('.jpg', '.bmp', '.png')
        self.pics = [p for p in os.listdir(path) if p.endswith(suffix)]
        btnPre = tkinter.Button(root, text='上一张', command=self.btnPreClick)
        btnPre.place(x=100, y=20, width=80, height=30)
        btnNext = tkinter.Button(root, text='下一张', command=self.btnNextClick)
        btnNext.place(x=230, y=20, width=80, height=30)
        # 用来显示图片的Label组件
        self.lbPic = tkinter.Label(root, text='test', width=400, height=600)
        self.lbPic.place(x=10, y=50, width=400, height=600)
        # 启动消息主循环
        root.mainloop()

    def changePic(self,flag):

        '''flag=-1表示上一个，flag=1表示下一个'''
        new = self.current + flag
        if new < 0:
            new = len(self.pics)-1
        elif new >= len(self.pics):
            new = 0
        # 获取要切换的图片文件名
        pic = self.pics[new]
        # 创建Image对象并进行缩放
        im = Image.open(pic)
        w, h = im.size
        # 这里假设用来显示图片的Label组件尺寸为400*600
        if w > 400:
            h = int(h * 400 / w)
            w = 400
        if h > 600:
            w = int(w * 600 / h)
            h = 600
        im = im.resize((w, h))
        # 创建PhotoImage对象，并设置Label组件图片
        im1 = ImageTk.PhotoImage(im)
        self.lbPic['image'] = im1
        self.lbPic.image = im1
        self.current = new

    # “上一张”按钮

    def btnPreClick(self):
        self.changePic(-1)

    def btnNextClick(self):
        self.changePic(1)

if __name__ == '__main__':
    g = gui('.')
