#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   81-90.py
@Time    :   2019/04/08 16:00:20
@Author  :   Alec Shang
@Version :   1.0
@Contact :   shangjingweiwork@163.com
@License :   (C)Copyright 2019-2020
@Desc    :   None
'''
#######################

# # 81. 809*??=800*??+9*?? 其中??代表的两位数,
# # 809*??为四位数，8*??的结果为两位数，9*??的结果为3位数。
# # 求??代表的两位数，及809*??后的结果。
# # 解析:定义一个数字x,将所给条件依次带入即可.
# x = 10
# while x < 99:
#     if 809*x == 800*x+9*x and 9999 > 809*x > 1000 and 99 > 8*x > 10 and 999 > 9*x > 100:
#         print(x)
#         break
#     x += 1

# # 82. 八进制转换为十进制

# a = 16
# print(oct(a))
# b = 0o20
# print(int('0o20', 10))

# # 83. 求0—7所能组成的奇数个数。(慎用,风扇呼呼呼呼呼呼呼)
# x = 0
# i = 0
# while x < 100000000:
#     if x % 2 != 0:
#         print(x)
#         x += 1
#         i += 1
#     else:
#         x += 1
#         continue
# print(i)

# 84. 连接字符串。(略过)

# # 85. 输入一个奇数，然后判断最少几个 9 除于该数的结果为整数。()

# x = int(input('please input a odd number:'))
# y = 9
# while 1:
#     if y % x == 0:
#         print(y)
#         break
#     else:
#         y = y*10+9
#         continue

# 86. 两个字符串连接程序。(略过)

# 87. 结构体变量传递(略过)

# # 88. 读取7个数（1—50）的整数值，每读取一个值，程序打印出该值个数的＊。
# for _ in range(7):
#     i = int(input('please input a 1-50 number:'))
#     print('*'*i)

# 89. 某个公司采用公用电话传递数据，数据是四位的整数，
# 在传递过程中是加密的，加密规则如下：每位数字都加上5,
# 然后用和除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换。
# 分析:按照规则倒推即可得出答案(略过)

# 90. 列表使用实例。(略过)
