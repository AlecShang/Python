#!/usr/local/bin/python3
# -*- encoding: utf-8 -*-
'''
@File    :   generator.py
@Time    :   2019/03/19 19:49:37
@Author  :   Alec Shang
@Version :   1.0
@Contact :   shangjingweiwork@163.com
@License :   (C)Copyright 2019-2020
@Desc    :   None
'''

#######################

# https://www.cnblogs.com/wj-1314/p/8490822.html

# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n += 1
#     return 'Done'

# try:
#     g = fib(5)
#     for i in range(6):
#         rst = next(g)
#         print(rst)

# except Exception as e:
#     print(e)


# coroutine case
def simple_coroutine(a):
    print('-> start')

    b = yield a
    print('-> recived', a, b)

    c = yield a + b
    print('-> recived', a, b, c)


# runc
sc = simple_coroutine(5)

aa = next(sc)
print(aa)
bb = sc.send(6)  # 5, 6
print(bb)
cc = sc.send(7)  # 5, 6, 7
print(cc)