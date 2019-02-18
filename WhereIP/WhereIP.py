import sys
from urllib.request import urlopen, Request
from lxml import etree

'''
    IP注册地查询——输入ip地址，查询该ip是在哪注册的。
'''


def WhereIP(ip):
    req = Request('https://www.ip.cn/index.php?ip=' + ip)

    req.add_header('User-Agent',
                   'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
    data = urlopen(req).read().decode('utf8')

    html = etree.HTML(data)
    try:
        areanm = html.xpath('//*[@id="result"]/div/p[2]/code/text()')
        GeoIP = html.xpath('//*[@id="result"]/div/p[3]/text()')
        loc = html.xpath('//*[@id="result"]/div/p[4]/text()')

        print(ip + ':')
        print(areanm[0])
        print(GeoIP[0])
        print(loc[0])
    except:
        print("Cannot find ip:" + ip)


if __name__ == '__main__':
    WhereIP(sys.argv[1])
    # WhereIP('49.64.191.167')
