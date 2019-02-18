import sys
import requests
import json


'''
    获取当前天气——获取某个地区当前的天气情况。
'''


def WhatWeather(city):
    url = "https://www.tianqiapi.com/api/?version=v1&city=" + city
    req = requests.get(url)
    data = json.loads(req.text)
    print(city + '的一周天气情况：')
    for i in range(7):
        print(data['data'][i]['day'] + ':' + data['data'][i]['wea'])

if __name__ == '__main__':
    WhatWeather(sys.argv[1])
