#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   21-30.py
@Time    :   2019/03/30 16:19:26
@Author  :   Alec Shang
@Version :   1.0
@Contact :   shangjingweiwork@163.com
@License :   (C)Copyright 2019-2020
@Desc    :   None
'''

#######################
# # 21. 猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，
# # 又多吃了一个第二天早上又将剩下的桃子吃掉一半，又多吃了一个。
# # 以后每天早上都吃了前一天剩下的一半零一个。
# # 到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。
# x = 9
# y = 1
# while x > 0:
#     y = (y + 1) * 2
#     x -= 1
#     print(x)
# print(y)

# 22. 两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。
# 已抽签决定比赛名单。有人向队员打听比赛的名单。
# a说他不和x比，c说他不和x,z比，请编程序找出两队赛手的名单。
# for i in range(ord('x'), ord('z') + 1):
#     for j in range(ord('x'), ord('z') + 1):
#         if i != j:
#             for k in range(ord('x'), ord('z') + 1):
#                 if (i != k) and (j != k):
#                     if (i != ord('x')) and (k != ord('x')) and (k != ord('z')):
#                         print('order is a -- %s\t b -- %s\tc--%s' %
#                               (chr(i), chr(j), chr(k)))

# 23. 打印出菱形:
# for i in range(6):
#     if i % 2 != 0:
#         print(' ' * int(6 / 2 - i // 2), '*' * i)
# for i in range(4):
#     if i % 2 != 0:
#         print(' ' * int(i % 2 + i // 2 + 1), '*' * (4 - i))

# 24. 有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
# 分析:分子等于前一个的分子加分母, 分母等于前一个的分子

# a = 2
# b = 1
# x = 0
# for i in range(20):
#     x += a / b
#     a, b = a + b, a
# print(x)

# 25. 求1+2!+3!+...+20!的和。
# 分析: 1+1*2+1*2*3+1*2*3*4

# def plus(x):
#     y = 1
#     for i in range(1, x + 1):
#         y = y * i
#     return y

# y = sum(map(plus, range(1, 21)))

# # s = sum(map(op, l))
# # print(s)
# print(y)

# 26. 利用递归方法求5!
# 分析:

# def iter(n):
#     if n == 1:
#         return n
#     return iter(n - 1) * n

# x = iter(5)
# print(x)

# # 27. 用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
# # 解析:

# def iter(n, i):
#     if n == '':
#         return
#     print(n[i - 1])
#     return iter(n[:-1], i - 1)

# l1 = 'abcde'
# iter(l1, len(l1))

# # 28. 有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。
# # 问第4个人岁数，他说比第3个人大2岁。问第三个人，又说比第2人大两岁。
# # 问第2个人，说比第一个人大两岁。最后问第一个人，他说是10岁。请问第五个人多大？
# # 分析:递归问题,f1=10,f2=f1+2 f3=f2+2

# def iter(n, p):
#     if p > 5:
#         return (n - 2)
#     return iter(n + 2, p + 1)

# y = iter(10, 1)
# print(y)

# # 29. 给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
# # 分析:和27类似.

# def iter(n, i):
#     if n == '':
#         return
#     print(n[i - 1])
#     return iter(n[:-1], i - 1)

# l1 = '12345'
# print(len(l1))
# iter(l1, len(l1))

# # 30. 一个5位数，判断它是不是回文数。
# # 即12321是回文数，个位与万位相同，十位与千位相同。
# # 分析: 类似29

# def iter(n, i, l2):
#     if n == '':
#         return
#     l2.append(n[i - 1])
#     return iter(n[:-1], i - 1, l2)

# l1, l2 = '12321', []
# print(len(l1))
# iter(l1, len(l1), l2)
# if l2[0] == l2[4] and l2[1] == l2[3]:
#     print('回文数')
# else:
#     print('No')