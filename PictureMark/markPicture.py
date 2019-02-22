from PIL import ImageDraw, Image, ImageFont


class markPicture:
    pictureName = None

    saveName = None

    def __init__(self,picName,sName):
        self.pictureName = picName
        self.saveName = sName

    def markText(self,text):
        img = Image.open(self.pictureName)
        draw = ImageDraw.Draw(img)
        myfont = ImageFont.truetype('C:/Windows/Fonts/Arial.ttf', size=40)
        fillcolor = "#FFFFE0"
        width, height = img.size
        draw.text((width - 500, 5), text, font=myfont, fill=fillcolor)
        img.save('result.jpg', 'jpeg')
        img.show()
        return 0
        pass



if __name__ == '__main__':
    mp = markPicture("timg.jpg","result.jpg")
    mp.markText("@fangsudong")