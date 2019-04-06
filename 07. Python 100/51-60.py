#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   51-60.py
@Time    :   2019/04/04 14:29:52
@Author  :   Alec Shang
@Version :   1.0
@Contact :   shangjingweiwork@163.com
@License :   (C)Copyright 2019-2020
@Desc    :   None
'''

#######################
# # 51. 学习使用按位与 & 。
# # 0&0=0; 0&1=0; 1&0=0; 1&1=1
# print(bin(10))
# print(bin(12))
# print(10 & 12)

# 52. 学习使用按位或 | 。
# # 0&0=0; 0&1=1; 1&0=1; 1&1=1
# print(bin(10))
# print(bin(12))
# print(10 | 12)

# # 53. 学习使用按位异或 ^ 。
# # 0^0=0; 0^1=1; 1^0=1; 1^1=0
# print(bin(10))
# print(bin(12))
# print(10 ^ 12)

# # 54. 取一个整数a从右端开始的4〜7位。
# a = 123456781234455
# print(str(a)[-4:])

# # 55. 学习使用按位取反~。
# # ~0=1; ~1=0;
# # 所有正整数的按位取反是其本身+1的负数
# # 所有负整数的按位取反是其本身+1的绝对值
# print(bin(8))
# print(~-5)

# # 56. 画图，学用circle画圆形
# import tkinter
# if __name__ == "__main__":
#     canvas = tkinter.Canvas(width=800, height=600,
#              bg='green', cursor='cross')
#     canvas.pack()
#     oval = canvas.create_oval(200, 100, 600, 500, width=10)
#     canvas.mainloop()

#  # 57. 画图，学用line画直线。

# import tkinter
# if __name__ == "__main__":
#     canvas = tkinter.Canvas(width=800, height=600,
#              bg='green', cursor='cross')
#     canvas.pack()
#     oval = canvas.create_line(0, 0, 400, 600, 55, 44, width=30)
#     canvas.mainloop()

# # 58. 画图，学用rectangle画方形。
# import tkinter
# if __name__ == "__main__":
#     canvas = tkinter.Canvas(width=800, height=600,
#              bg='green', cursor='cross')
#     canvas.pack()
#     oval = canvas.create_rectangle(55, 66, 444, 555, width=20)
#     canvas.mainloop()

# 59. 画图，综合例子。 (略过)


# 60. 计算字符串长度。
def aaa():
    a = 'asdasfasgga'
    return len(a)


def bbb():
    return 'bbb'


if __name__ == "__main__":
    print('aaa')
    print('bbb')
