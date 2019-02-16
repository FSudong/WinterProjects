import sys
'''
    统计元音字母——输入一个字符串，统计处其中元音字母的数量。更复杂点的话统计出每个元音字母的数量。
'''
def VowelsCount(str):
    result = [0,0,0,0,0]

    for i in str:
        if i == 'a':
            result[0] += 1
        if i == 'e':
            result[1] += 1
        if i == 'i':
            result[2] += 1
        if i == 'o':
            result[3] += 1
        if i == 'u':
            result[4] += 1
    return result



if __name__ == '__main__':
    print("String: " + sys.argv[1])
    print("Result: ")
    result = VowelsCount(sys.argv[1])
    print("a: " + str(result[0]))
    print("e: " + str(result[1]))
    print("i: " + str(result[2]))
    print("o: " + str(result[3]))
    print("u: " + str(result[4]))