import sys
'''
    逆转字符串——输入一个字符串，将其逆转并输出。
'''
def reverse(str):
    return str[::-1]

if __name__ == '__main__':
    print("String: " + sys.argv[1])
    print("Reversal: " + reverse(sys.argv[1]))