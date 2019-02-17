import sys
from urllib.request import urlopen,Request
from lxml import etree
'''
    邮编查询——输入邮编，返回使用该邮编的地区名称。
'''

def PostalCode(code):
    req = Request('http://opendata.baidu.com/post/s?wd=' + code + '&p=mini&rn=20')

    req.add_header('User-Agent',
                   'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
    data = urlopen(req).read().decode('gbk')

    html = etree.HTML(data)
    try:
        areanm = html.xpath('/html/body/section/article[1]/h3/text()')[0].split(':')
        print(code + areanm[0])
    except:
        print("Postal code not found!")




if __name__ == '__main__':
    PostalCode(sys.argv[1])
    # PostalCode('213200')
