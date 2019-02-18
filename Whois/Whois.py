import sys
from urllib.request import urlopen, Request
from lxml import etree


'''
    Whois查询工具——输入一个ip或者主机地址，通过whois查询并将结果返回。
'''


def Whois(url):
    req = Request('http://whois.chinaz.com/' + url)

    req.add_header('User-Agent',
                   'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
    data = urlopen(req).read().decode('utf8')

    html = etree.HTML(data)

    try:
        i1 = html.xpath('//*[@id="sh_info"]/li[2]/div[2]/div/span/text()')
        i2 = html.xpath('//*[@id="sh_info"]/li[3]/div[2]/span/text()')
        i3 = html.xpath('//*[@id="sh_info"]/li[4]/div[2]/span/text()')
        i4 = html.xpath('//*[@id="sh_info"]/li[6]/div[2]/span/text()')
        i5 = html.xpath('//*[@id="sh_info"]/li[7]/div[2]/span/text()')
        i6 = html.xpath('//*[@id="sh_info"]/li[9]/div[2]/span/text()')

        print('查询地址：' + url)
        print('注册商：' + i1[0])
        print('联系邮箱：' + i2[0])
        print('联系电话：' + i3[0])
        print('创建时间：' + i4[0])
        print('过期时间：' + i5[0])
        print('域名服务器：' + i6[0])

    except:
        print("Cannot find url:" + url)


if __name__ == '__main__':
    Whois(sys.argv[1])
    # Whois('t.me')
