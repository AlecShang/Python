#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   111.py
@Time    :   2023/03/09 10:17:59
@Author  :   Alec Shang
@Version :   1.0
@Contact :   shangjingweiwork@163.com
@License :   (C)Copyright 2019-2020
@Desc    :   None
'''
#######################
# 解析方法一
from bs4 import BeautifulSoup

# 输入参数为要分析的 html 文件名，返回值为对应的 BeautifulSoup 对象
def create_doc_from_filename(filename):
    with open(filename, "r", encoding='utf-8') as f:
        html_content = f.read()
        doc = BeautifulSoup(html_content)
    return doc

def parse(doc):
    post_list = doc.find_all("div", class_="post-info")
    for post in post_list:
        link = post.find_all("a")[1]
        print(link.text.strip())
        print(link["href"])

def main():
    filename = "tips1.html"
    doc = create_doc_from_filename(filename)
    parse(doc)

if __name__ == '__main__':
    main()