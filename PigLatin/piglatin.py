import sys
'''
    拉丁猪文字游戏——这是一个英语语言游戏。基本规则是将一个英语单词的第一个辅音音素的字母移动到词尾并且加上后缀-ay（譬如“banana”会变成“anana-bay”）。
'''
def piglatin(str):
    word = str.lower().split(" ")
    for i in range(len(word)):
        if ((word[i][:1] in "aeiou")):
            word[i] = word[i] + "hay";
        elif (list[i][:2] == "qu"):
            word[i] = word[i][len(word[i]):] + "quay";
        else:
            num = getIndex(word[i]);
            # print num;
            word[i] = word[i][num:] + word[i][0:num] + "ay"
    return word


def getIndex(s):
    for i in range(len(s)):
        if((s[i] in "aeiou") or (i!=0 and s[i] =="y")):
            return i;
    return len(s);

if __name__ == '__main__':
    print("String: " + sys.argv[1])
    print("Pig Latin: " + piglatin(sys.argv[1]))