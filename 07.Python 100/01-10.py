#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   01-10.py
@Time    :   2019/03/27 11:16:05
@Author  :   Alec Shang
@Version :   1.0
@Contact :   shangjingweiwork@163.com
@License :   (C)Copyright 2019-2020
@Desc    :   None
'''

#######################

# 01. 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# n = 0
# for i in range(1, 5):
#     for j in range(1, 5):
#         for k in range(1, 5):
#             if i != j and i != k and j != k:
#                 print(i, j, k)
#                 n += 1
# print('the count print is {0} numbers'.format(n))

# 02. 企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
# 20万到40万之间时，高于20万元的部分，可提成5%；
# 40万到60万之间时高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%，
# 高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
# I = int(input('please input profits:'))
# I = 12
# x = 0
# if 100 < I:
#     x += (I - 100) * 0.01
#     I = 100
# if 60 < I <= 100:
#     x += (I - 60) * 0.015
#     I = 60
# if 40 < I <= 60:
#     x += (I - 40) * 0.003
#     I = 40
# if 20 < I <= 40:
#     x += (I - 20) * 0.005
#     I = 20
# if 10 < I <= 20:
#     x += (I - 10) * 0.075
#     I = 10
# if 0 < I <= 10:
#     x += I * 0.1
# print(x)

# 优化解决方案
# I = int(input('please input income:'))
# I = 120000
# x, j = 0, 0
# income = [0, 100000, 200000, 400000, 600000, 1000000]
# rate = [0.1, 0.075, 0.05, 0.03, 0.015, 0.01]
# income.reverse()
# rate.reverse()
# for i in range(6):
#     if I > income[i]:
#         x += (I - income[i]) * rate[i]
#         I = income[i]
# print(x)

# 03. 一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
# l1 = []
# for x in range(1, 85):
#     for y in range(-100, 2000):
#         if x**2 == (y + 100):
#             l1.append(y)

# for i in range(1, 85):
#     for z in l1:
#         if i**2 == (z + 100 + 168):
#             print(z)

# 04. 输入某年某月某日，判断这一天是这一年的第几天？
# 04. 输入某年某月某日，判断这一天是这一年的第几天？
# 解析：输入时最重要的是先判断这一年是否是闰年，如果是2月将会是几天，
# 接下来需要知道30天和31天的月份。
# import time
# year = int(input('year:'))
# month = int(input('month:'))
# day = int(input('day:'))
# d = 0
# month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# # 闰年，能被4整除，不能被100整除，能被400整除
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     month_list[1] = 29
# for i in range(month - 1):
#     d += month_list[i]
# print(d + day)

# 05. 输入三个整数x,y,z，请把这三个数由小到大输出。
# i = int(input('please input number 1:'))
# j = int(input('please input number 2:'))
# k = int(input('please input number 3:'))
# l = [i, j, k]
# l.sort()
# for a in l:
#     print(a)

# 06. 斐波那契数列
# 斐波那契数列（Fibonacci sequence），又称黄金分割数列，
# 指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
# 此问题是典型的迭代问题,首先f0 = 0, f1 = 1, f2 = f1 + f0 以此类推可得迭代函数.
# def fib(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fib(n - 1) + fib(n - 2)

# fib(7)

# 07. 将一个列表的数据复制到另一个列表中。
# l1 = [1, 2, 3, 4, 5]
# l2 = l1
# print(l2)

# l3 = [1, 2, 3]
# l4 = l3[:]
# print(l4)

# 08. 输出 9*9 乘法口诀表。
# 1*1
# 2*1 2*2
# 3*1 3*2 3*3
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(i, 'x', j, '=', i * j, end='  ')
#     print('', end='\n')

# 09. 暂停一秒输出。
# import time
# i = 0
# while (i < 10):
#     print(time.time())
#     time.sleep(1)
#     print(time.time())
#     time.sleep(1)
#     i += 1

# 10. 暂停一秒输出，并格式化当前时间。
# import time
# i = 0
# while (i < 3):
#     print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
#     time.sleep(1)
#     print(time.localtime(time.time()))
#     time.sleep(1)
#     i += 1


#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   01-10.py
@Time    :   2019/10/16 16:30:56
@Author  :   Alec Shang
@Version :   1.0
@Contact :   shangjingweiwork@163.com
@License :   (C)Copyright 2019-2020
@Desc    :   None
'''
#######################

# 给定一个包含非负整数的 M x N 迷宫，请找出一条从左上角到右下角的路径，
# 使得路径上的数字总和最小。每次只能向下或者向右移动一步。

# 第一行包含两个整数M和N，以空格隔开，1≤N≤10，1≤M≤10。
# 接下来的M行中，每行包含 N个数字 。

# 找出总和最小的路径，输出路径上的数字总和。


# 此处M代表行,N代表列.
def minSum(M, N):
    sum = 0
    # 按列走加在一起,从0索引开始,即1到N
    for i in range(1, N):
        N[i] += N[i - 1]
    # 按行走加在一起,求总和
    for j in range(1, M):
        M[j] += M[j - 1]
    # 求最小和
    for i in range(1, M):
        for j in range(1, N):
            sum = min(M[i - 1], N[j - 1])
    return sum


# 近期某商场由于周年庆，开启了“0元购”活动。活动中，消费者可以通过组合手中的代金券，实现0元购买指定商品。
# 聪明的小团想要用算法来帮助他快速计算：对于指定价格的商品，使用代金券凑出其价格即可，
# 但所使用的代金券总面额不可超过商品价格。由于代金券数量有限，使用较少的代金券张数则可以实现价值最大化，即最佳优惠。
# 假设现有100元的商品，而代金券有50元、30元、20元、5元四种，则最佳优惠是两张50元面额的代金券；
#
# 而如果现有65元的商品，则最佳优惠是两张30元代金券以及一张5元代金券。
# 请你帮助小团使用一段代码来实现代金券计算。
