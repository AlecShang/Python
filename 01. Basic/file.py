#!/usr/local/bin/python3.7
# -*- coding:utf-8 -*-

import sys

# 用with读取文件

# with open(r'../shang.txt','r') as f:
#     print(type(f))
#     l = list(f)
#     print(type(l))
#     for i in l:
#         print(i)

# 普通的读取文件方式
# f = open(r'../shang.txt','r')
# for i in f:
#     print(i)
# f.close()

# 将文本当中的内容以字符方式读取
# with open(r'../shang.txt', 'r') as f:
#     # 1. 首先判断文件是否读取完毕,如果没有读取完毕,则一直进行读取操作.
#     while f.readable:
#         n = f.read(1)
#         if n != '':
#             print(n)
#         else:
#             break
# print('Done....')

# 2. 可以使用seek先判断内容的最后一个字符,然后按照这个长度进行循环
# with open(r'../shang.txt', 'r') as f:
#     n, i = f.seek(0,2), 0
#     f.seek(0,0)
#     while i < n:
#         print(f.read(1))
#         i += 1
# print('Done......')

# 使用seek从指定的位置开始读取文件内容
# with open(r'../shang.txt', 'r') as f:
#     print(f.seek(0,2))

# 向文件里添加内容.
# with open(r'../shang.txt', 'a') as f:
#     f.writelines('\n这是新添加的一句话,在新的一行!')

# 序列化,也可以认为是打包或者是加密输入文件的操作
# 序列化之后文件不可直接打开
# import pickle

# with open(r'../shang.txt','wb') as f:
#     p = 'this is a pickle text'
#     pickle.dump(p,f)
# print('Done.....')

# 反序列化,一般是将序列化的文件进行一个解码操作
# import pickle

# with open(r'../shang.txt','rb') as f:
#     n = pickle.load(f)
#     print(p)

# 持久化文件,类似于数据库文件.db,存储方式是典型的子类型k,v

# import shelve

# with shelve.open(r'shang', 'c') as d:
#     # d['one'] = 1
#     # d['two'] = 2
#     # d['three'] = 3
#     print(d['two'])

# print('Done......')