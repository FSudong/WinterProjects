import sys
import urllib.request
from urllib.request import urlopen, Request
from lxml import etree

import http.cookiejar

'''
    原子钟校时——从网上同步原子钟时间。全世界有很多原子钟，可以把它们都列出来。
'''


def Timeis():
    req = Request('https://time.is/')
    head = {
        'Connection': 'Keep-Alive',
        'Accept': 'text/html, application/xhtml+xml, */*',
        'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'}

    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    uop = opener.open('https://time.is/', timeout=1000)
    data = uop.read()
    html = etree.HTML(data)
    try:
        Tokyo = html.xpath('//*[@id="favt1"]/text()')
        Beijing = html.xpath('//*[@id="favt2"]/text()')
        Moscow = html.xpath('//*[@id="favt3"]/text()')
        Paris = html.xpath('//*[@id="favt4"]/text()')
        London = html.xpath('//*[@id="favt5"]/text()')
        New_York = html.xpath('//*[@id="favt6"]/text()')
        Los_Angeles = html.xpath('//*[@id="favt7"]/text()')
        print("Tokyo: " + Tokyo[0])
        print("Beijing: " + Beijing[0])
        print("Moscow: " + Moscow[0])
        print("Paris: " + Paris[0])
        print("London: " + London[0])
        print("New_York: " + New_York[0])
        print("Los_Angeles: " + Los_Angeles[0])
    except:
        print("No time found")

if __name__ == '__main__':
    Timeis()
