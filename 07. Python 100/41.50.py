#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   41.50.py
@Time    :   2019/04/04 10:57:13
@Author  :   Alec Shang
@Version :   1.0
@Contact :   shangjingweiwork@163.com
@License :   (C)Copyright 2019-2020
@Desc    :   None
'''

#######################
# # 41. 模仿静态类
# def varfunc():
#     var = 0
#     print('var = {0}'.format(var))
#     var += 1

# if __name__ == '__main__':
#     for i in range(3):
#         varfunc()

# # 类的属性
# # 作为类的一个属性吧
# class Static:
#     StaticVar = 5

#     def varfunc(self):
#         self.StaticVar += 1
#         print(self.StaticVar)

# print(Static.StaticVar)
# a = Static()
# for i in range(3):
#     a.varfunc()

# 42. 学习使用auto定义变量的用法。
# num = 2

# def autofunc():
#     num = 1
#     print('internal block num = {0}'.format(num))
#     num += 1

# for i in range(3):
#     print('The num = {0}'.format(num))
#     num += 1
#     autofunc()

# # 43. 模仿静态变量(static)另一案例。

# class Num:
#     nNum = 1

#     def inc(self):
#         self.nNum += 1
#         print('nNum = {0}'.format(self.nNum))

# if __name__ == '__main__':
#     nNum = 2
#     inst = Num()
#     for i in range(3):
#         nNum += 1
#         print('The num = {0}'.format(nNum))
#         inst.inc()

# # 44. 两个 3 行 3 列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵：

# l1 = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
# l2 = [[4, 4, 4], [5, 5, 5], [6, 6, 6]]
# l3 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# for i in range(len(l3)):
#     for j in range(3):
#         l3[i][j] = l1[i][j] + l2[i][j]
# print(l3)

# # 45. 统计 1 到 100 之和。
# x = 0
# for i in range(1, 101):
#     x += i
# print(x)

# # 46. 求输入数字的平方，如果平方运算后小于 50 则退出。

# x = 10
# if x**2 >= 50:
#     print(x**2)
# else:
#     print(x**2, 'need exit!')

# # 47. 两个变量值互换。

# x = 1
# y = 2
# print(x, y)
# x, y = y, x
# print(x, y)

# # 48. 数字比较。

# if __name__ == "__main__":
#     x = 101
#     y = 200
#     if x > y:
#         print(x, '>', y)
#     elif x < y:
#         print(x, '<', y)
#     else:
#         print(x, '=', y)

# # 49. 使用lambda来创建匿名函数。

# if __name__ == "__main__":
#     a = 10
#     b = 20
#     x = (lambda a, b: a + b)
#     print(x(a, b))

# 50. 输出一个随机数。
from random import randrange
print(randrange(1, 100, 2))
