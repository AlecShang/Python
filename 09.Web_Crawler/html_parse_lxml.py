#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   111.py
@Time    :   2023/03/09 10:18:41
@Author  :   Alec Shang
@Version :   1.0
@Contact :   shangjingweiwork@163.com
@License :   (C)Copyright 2019-2020
@Desc    :   None
'''
#######################
# 解析方法二，指定解析器
from bs4 import BeautifulSoup

# 输入参数为要分析的 html 文件名，返回值为对应的 BeautifulSoup 对象
def create_doc_from_filename(filename):
    with open(filename, "r", encoding='utf-8') as f:
        html_content = f.read()
        soup = BeautifulSoup(html_content, "lxml")
    return soup

def parse(soup):
    post_list = soup.find_all("div", class_="post-info")
    for post in post_list:
        link = post.find_all("a")[1]
        print(link.text.strip())
        print(link["href"])

def main():
    filename = "tips1.html"
    soup = create_doc_from_filename(filename)
    parse(soup)

if __name__ == '__main__':
    main()