from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import random
'''
    验证码生成器——应该在登录时见过有数字有字母的验证码图片吧？这可以防止自动登录和垃圾广告。试着自己做一个，如果使用PHP的话，看下GD的图片函数。
'''

def getRandomColor():
    '''获取一个随机颜色(r,g,b)格式的'''
    c1 = random.randint(0, 255)
    c2 = random.randint(0, 255)
    c3 = random.randint(0, 255)
    return (c1, c2, c3)


def getRandomStr():
    '''获取一个随机字符串，每个字符的颜色也是随机的'''
    random_num = str(random.randint(0, 9))
    random_low_alpha = chr(random.randint(97, 122))
    random_upper_alpha = chr(random.randint(65, 90))
    random_char = random.choice([random_num, random_low_alpha, random_upper_alpha])

    return random_char

if __name__ == '__main__':
    # 获取一个Image对象，参数分别是RGB模式。宽150，高30，随机颜色
    image = Image.new('RGB', (150, 30), getRandomColor())

    # 获取一个画笔对象，将图片对象传过去
    draw = ImageDraw.Draw(image)

    # 获取一个font字体对象参数是ttf的字体文件的目录，以及字体的大小
    font = ImageFont.truetype("KumoFont.ttf", size=26)

    for i in range(5):
        # 循环5次，获取5个随机字符串
        random_char = getRandomStr()

        # 在图片上一次写入得到的随机字符串,参数是：定位，字符串，颜色，字体
        draw.text((10 + i * 30, 0), random_char, getRandomColor(), font=font)

    # 保存到硬盘，名为test.png格式为png的图片
    image.save(open('CAPTCHA.png', 'wb'), 'png')
    print("CAPTCHA has ben saved as CAPTCHA.png")
