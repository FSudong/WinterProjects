import uuid
'''
    CD-Key生成器——利用某种算法生成一个唯一的key。软件开发者可以用它来作为软件的激活器。
'''
def reverse(str):
    return str[::-1]

if __name__ == '__main__':
    print(uuid.uuid1())