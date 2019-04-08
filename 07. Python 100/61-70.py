#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   61-70.py
@Time    :   2019/04/05 23:15:08
@Author  :   Alec Shang
@Version :   1.0
@Contact :   shangjingweiwork@163.com
@License :   (C)Copyright 2019-2020
@Desc    :   None
'''
#######################
# # 61. 打印出杨辉三角形（要求打印出10行)
# l1 = [[0 for i in range(10)] for i in range(10)]
# for i in range(1, 11):
#     for j in range(1, i + 1):
#         if j == i or j == 1:
#             print(1, end=' ')
#             l1[i - 1][j - 1] = 1
#             l1[i - 1][i - 1] = 1
#             continue
#         else:
#             x = l1[i - 2][j - 2] + l1[i - 2][j - 1]
#             print(x, end=' ')
#             l1[i - 1][j - 1] = x
#     print('')

# # 62. 查找字符串。
# a = 'abcdafasfawfawf'
# print(a.find('daf'))

# # 63. 画椭圆。

# import tkinter

# canv = tkinter.Canvas(width=600, height=600, bg='green')
# # for i in range(10):
# #     canv.create_oval(11 + i * 10, 22 + i * 10, 111 + i * 10, 222 + i * 10)
# #     canv.pack()
# canv.create_oval(55, 111, 444, 555)
# canv.pack()
# canv.mainloop()

# 64. 65. (画图略)

# # 66. 输入3个数a,b,c，按大小顺序输出。
# a = int(input('a'))
# b = int(input('b'))
# c = int(input('c'))
# l1 = [a, b, c]
# l1.sort()
# for i in l1:
#     print(i)

# # 67. 输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。
# a = [41, 5, 16, 2, 74, 8, 5, 68, 67, 8, 67, 9679, 222, 566]
# b = a.index(max(a))
# c = a.index(min(a))
# a[0], a[b] = a[b], a[0]
# a[-1], a[c] = a[c], a[-1]
# print(a)

# # 68. 有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# b = a[-5:]
# c = a[:-5]
# a = b + c
# print(a)

# ***69. 有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），
# 凡报到3的人退出圈子，问最后留下的是原来第几号的那位。
# x = 23
# l1 = []
# y = 1
# for i in range(1, x + 1):
#     if i % 3 == 0:
#         l1.append(3)
#     elif i % 3 == 1:
#         l1.append(1)
#     elif i % 3 == 2:
#         l1.append(2)
# print(l1)
# for j in l1:
#     if j == 3:
#         l1[l1.index(j)] = 0
#         while l1[l1.index(j)+y] == 0:
#             y += 1
#         l1[l1.index(j)+y] = 3
#         print(l1, end='')


# # 70. 写一个函数，求一个字符串的长度，在main函数中输入字符串，并输出其长度。
# def cal_str(x):
#     return len(x)


# if __name__ == "__main__":
#     str = input('please input string:')
#     print(cal_str(str))
