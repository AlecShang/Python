#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Crawler_urllib3.py
@Time    :   2023/03/09 10:13:32
@Author  :   Alec Shang
@Version :   1.0
@Contact :   shangjingweiwork@163.com
@License :   (C)Copyright 2019-2020
@Desc    :   None
'''
#######################
# urllib3 的方法
import urllib3


def download_content(url):
    """
    第一个函数，用来下载网页，返回网页内容
    参数 url 代表所要下载的网页网址。
    整体代码和之前类似
    """
    http = urllib3.PoolManager()
    response = http.request("GET", url)
    response_data = response.data
    html_content = response_data.decode()
    return html_content


# 第二个函数，将字符串内容保存到文件中
# 第一个参数为所要保存的文件名，第二个参数为要保存的字符串内容的变量
def save_to_file(filename, content):
    fo = open(filename, "w", encoding="utf-8")
    fo.write(content)
    fo.close()


def main():
    # 下载报考指南的网页
    url = "https://zkaoy.com/sions/exam"
    result = download_content(url)
    save_to_file("tips1.html", result)


if __name__ == '__main__':
    main()
