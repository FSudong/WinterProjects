import sys

'''
    判断是否为回文——判断用户输入的字符串是否为回文。回文是指正反拼写形式都是一样的词，譬如“racecar”。
'''

def Palindrome(str):
    return str == str[::-1]



if __name__ == '__main__':
    print("String: " + sys.argv[1] + "")
    print("Result: " + str(Palindrome(sys.argv[1])))