#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   11-20.py
@Time    :   2019/03/29 22:58:12
@Author  :   Alec Shang
@Version :   1.0
@Contact :   shangjingweiwork@163.com
@License :   (C)Copyright 2019-2020
@Desc    :   None
'''

#######################

# # 11. 古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，
# # 小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
# # 问题分析：兔子的规律为，1,1,2,3,5,8,13,21,34,55 典型的迭代

# def iter(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#     return iter(n - 1) + iter(n - 2)

# iter(5)

# # 12. 判断101-200之间有多少个素数，并输出所有素数。

# for i in range(101, 200):
#     for j in range(2, i + 1):
#         if i % j == 0:
#             break
#         else:
#             print(i)
#             break

# # 12. 判断101-200之间有多少个素数，并输出所有素数。
# # 分析：
# # 1.从2开始遍历到当前数，如果遇到可以整除的数就直接返回执行下一个数的遍历
# # 2.如果不可以整除就执行判断是否遍历结束，如果结束就输出
# # 3.如果没有结束就继续进行遍历
# x = 0
# for i in range(101, 200):
#     for j in range(2, i + 1):
#         if i % j == 0 and i != j:
#             break
#         if i == j:
#             print(i)
#             x += 1
#             break
#         else:
#             continue
# print(x)

# # 13. 打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，
# # 其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，
# # 因为153=1的三次方＋5的三次方＋3的三次方。
# # 分析：
# # 1.所有三位数是从100循环到999，然后拿出个十百分别立方之后相加
# for i in range(100, 1000):
#     x = i // 100
#     y = i // 10 % 10
#     z = i % 10
#     if x**3 + y**3 + z**3 == i:
#         print(i)

# # 14. 将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
# # 解析：
# # 1.首先确定质数有哪些
# # 2.然后将给定数字分解，如果可以除尽，则保留继续循环除

# x = int(input('please input num:'))
# l, a = [], []
# for i in range(200):
#     for j in range(2, i + 1):
#         if i % j == 0 and i != j:
#             break
#         if i == j:
#             l.append(i)
#             break
#         else:
#             continue
# for z in l:
#     if x % z == 0:
#         a.append(z)
#         x = x // z

#     if z == l[-1]:
#         print('x', end=' ')
#         for t in a:
#             if t == a[0]:
#                 print('=', t, end='')
#             else:
#                 print('*', t, end='')
#         print('*', x, end='')
#         break

# # 15. 利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
# student_score = int(input('please input your score:'))

# if student_score >= 90:
#     print('A')
# elif 80 > student_score >= 60:
#     print('B')
# else:
#     print('C')

# # 16. 输出指定格式的日期。
# import time
# print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))

# # 17. 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

# a = input()
# a = list(a)
# adic = {}
# for i in a:
#     adic[i] = a.count(i)
# print(adic)

# # 18. 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。
# # 例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
# x = input('请输入要相加的数字')
# i = int(input('请输入要相加几次'))
# z = 0
# for j in range(1, i + 1):
#     print(x * j)
#     z += int(x * j)
# print(z)

# # 19. 一个数如果恰好等于它的因子之和，这个数就称为"完数"。
# # 例如6=1＋2＋3.编程找出1000以内的所有完数。

# for i in range(2, 1001):
#     x = 0
#     for j in range(2, i + 1):
#         if i % j == 0:
#             x += i // j
#     if x == i:
#         print(i)

# # 20. 一球从100米高度自由落下，每次落地后反跳回原高度的一半；
# # 再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
# x = 0
# high = 100
# z = 0
# while x < 10:
#     z += high
#     high = high / 2
#     z += high
#     x += 1
# z -= high
# print('共经历了{0},第10次反弹高度为{1}'.format(z, high))
