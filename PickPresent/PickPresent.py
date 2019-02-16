import sys
import random
'''
    帮你挑礼物——输入一堆你可能会送的礼物，当有人过生日时，该程序会随机选择一样礼物。也可以加上一个额外功能，可以告知哪里可以弄到这个礼物。
'''
def PickPresent(str):
    presents = str.lower().split(",")
    num = len(presents)
    pick = random.randint(0,num)
    return presents[pick]

if __name__ == '__main__':
    print("Input: " + sys.argv[1])
    print("Pick: " + PickPresent(sys.argv[1]))