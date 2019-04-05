#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   31-40.py
@Time    :   2019/04/03 10:42:01
@Author  :   Alec Shang
@Version :   1.0
@Contact :   shangjingweiwork@163.com
@License :   (C)Copyright 2019-2020
@Desc    :   None
'''

#######################
# # 31. 请输入星期几的第一个字母来判断一下是星期几，
# # 如果第一个字母一样，则继续判断第二个字母。
# # 分析:首先 MON,TUES,WEDNES,THURS,FRI,SATUR,SUN

# day = input('please input alphabet:')
# if day == 'M':
#     print('MON')
# if day == 'T':
#     day1 = input('please input second alphabet:')
#     if day1 == 'U':
#         print('TUES')
#     if day1 == 'H':
#         print('THURS')
# if day == 'W':
#     print('WEDNES')
# if day == 'F':
#     print('FRI')
# if day == 'S':
#     day2 = input('please input second alphabet:')
#     if day2 == 'A':
#         print('SATUR')
#     if day2 == 'U':
#         print('SUN')

# 32. 按相反的顺序输出列表的值。
# def iter(n, i):
#     if i == 0:
#         return
#     print(n[i - 1])
#     return iter(n[:-1], i - 1)

# l1 = ['1', '2', '3', '4', '5']
# iter(l1, len(l1))

# 第二种方法
# l1 = ['1', '2', '3', '4', '5']
# l1.reverse()
# for i in l1:
#     print(i)

# # 33. 按逗号分隔列表。

# l1 = ['1', '2', '3', '4', '5']
# s1 = ','.join(n for n in l1)
# print(s1)

# # 34. 练习函数调用。

# def p():
#     print('this is a function')

# if __name__ == "__main__":
#     p()

# 35. 文本颜色设置。
# \033[1;31;40m    <!--1-高亮显示 31-前景色红色  40-背景色黑色-->
# print('\033[0;31;41masdasdasdas')

# # 36. 求100之内的素数。
# # 解析: 100间的素数指的是除了本身和1之外不能够被其他数整除

# for i in range(2, 101):
#     for j in range(2, i + 1):
#         if i % j == 0 and i != j:
#             break
#         if i == j:
#             print(i)
#         continue

# # 37. 对10个数进行排序。

# l1 = [5, 3, 7, 8, 0, 2, 4, 11, 23, 55]
# l1.sort()
# print(l1)

# # 38. 求一个3*3矩阵主对角线元素之和

# l1 = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
# x = 1
# j = 0
# print(l1)
# for i in l1:
#     x *= i[j]
#     j += 1
# print(x)

# # 39. 有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。

# a = [1, 4, 6, 9, 13, 16, 19, 28, 40, 100, 0]
# a.append(3)
# a.sort()
# print(a)

# 40.将一个数组逆序输出。

if __name__ == "__main__":
    a = [9, 6, 5, 4, 1]
    a.sort()
    print(a)
