# coding:utf8
import subprocess

import time

import os


# 传入url，加载相应的视频 获得视屏 版本
def download_by_url(url):
    # 查询视频信息语句
    # subprocess模块支持 windows系统 与  python交互
    p = subprocess.Popen('youtube-dl -F ' + url, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    start = time.time()
    print("********\t查询:" + url + "\t" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start)))
    # 打印控制台信息
    formatcode = {"mp4": [], "3gp": [], "webm": []}
    while True:
        line = p.stdout.readline().decode(encoding="GBK")
        if line != '':
            print(line)
            if line.find("mp4") > -1:
                formatcode["mp4"].append(line.split(" ")[0])
            if line.find("3gp") > -1:
                formatcode["3gp"].append(line.split(" ")[0])
            if line.find("webm") > -1:
                formatcode["webm"].append(line.split(" ")[0])
        else:
            break
    p.wait()

    # 下载视频
    # formatcode["mp4"] 是mp4格式的视频code 不同的code代表不同的视频分辨率
    code = ""
    for x in formatcode["mp4"]:
        if x == "18":
            code = "18"
    if code == "" and len(formatcode["mp4"])>0:
        code = formatcode["mp4"][0]
    print(code)
    # 下载视频
    p = subprocess.Popen('youtube-dl -f ' + code + " " + url, shell=True, stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)

    print("********\t下载:" + url + "\t" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start)))
    # 打印控制台信息

    while True:
        line = p.stdout.readline().decode(encoding="GBK")
        if line != '':
            print(line)
        else:
            break
    p.wait()

    end = time.time()
    print("********\tEnd\t" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end)), )
    print("taking：" + str(int(end - start)) + " seconds")


if __name__ == '__main__':
    download_by_url("https://www.youtube.com/watch?v=wNDsp9_MSDA")