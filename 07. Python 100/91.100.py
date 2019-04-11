#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   91.100.py
@Time    :   2019/04/09 11:23:18
@Author  :   Alec Shang
@Version :   1.0
@Contact :   shangjingweiwork@163.com
@License :   (C)Copyright 2019-2020
@Desc    :   None
'''
#######################

# 91. 时间函数举例1(略过)

# 92. 时间函数举例2(略过)。

# 93. 时间函数举例3。(略过)

# # 94. 时间函数举例4,一个猜数游戏，判断一个人反应快慢。
# from random import randint

# x = randint(1, 50)
# i = int(input('plese guess the number:'))
# while 1:
#     if i > x:
#         i = int(input('plese guess little:'))
#         continue
#     if i < x:
#         i = int(input('plese guess large:'))
#         continue
#     else:
#         print('you are very good! the number is : {0}'.format(i))
#         break


# 95. 字符串日期转换为易读的日期格式。(略过)

# 96. 计算字符串中子串出现的次数。(略过)

# # 97. 从键盘输入一些字符，逐个把它们写到磁盘文件上，直到输入一个 # 为止。
# # 写到磁盘用的是dump,读取用load.模块是pickle

# import pickle

# x = 'abcd#efg'
# for i in x:
#     if i != '#':
#         a = pickle.dumps(i)
#         continue
#     break
# print(pickle.loads(a))

# # 98. 从键盘输入一个字符串，将小写字母全部转换成大写字母，
# # 然后输出到一个磁盘文件"test"中保存。

# x = input('please input string:')

# with open(r'python100.txt', 'a') as f:
#     f.writelines(x.upper())


# 99. 有两个磁盘文件A和B,各存放一行字母,
# 要求把这两个文件中的信息合并(按字母顺序排列),
#  输出到一个新文件C中。
