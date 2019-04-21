#!/usr/local/bin/python3
# -*- encoding: utf-8 -*-
'''
@File    :   func_programing.py
@Time    :   2019/03/19 10:50:05
@Author  :   Alec Shang
@Version :   1.0
@Contact :   shangjingweiwork@163.com
@License :   (C)Copyright 2019-2020
@Desc    :   None
'''
#######################

import time

# lambda case
# aaa = lambda x: x * 10
# print(aaa(10))

# map case
l1 = [1, 2, 3, 4, 5]


def mult(x):
    return x * 10


l2 = map(mult, l1)
# print(list(l2))

# reduce case remember that reduce(func,sequence) ,func needs 2 arrguments
# from functools import reduce
l3 = [1, 2, 3, 4, 5]


def mult1(x, y):
    return x * y


# l4 = reduce(mult1, l3)
# print(l4)

# filter case as map
l5 = [1, 2, 3, 4, 5]


def filter1(x):
    return x % 2 == 0


l6 = filter(filter1, l1)
# print(list(l6))

# list sorted case
l7 = [-43, 23, 45, 6, -23, 2, -4345]
l8 = sorted(l7, key=abs, reverse=True)

# print(l8)

# closure case


def clouser_func(x):
    y = x

    def re_func():
        return y * 10

    return re_func


cl = clouser_func(5)

# print(cl())

# cl2 = clouser_func(7)
# print(cl2())

# print('*' * 20)
# print(cl())
# print(cl2())


# clouser typical error case1
def count():
    # 定义列表，列表里存放的是定义的函数
    fs = []
    for i in range(1, 4):
        # 定义了一个函数f
        # f是一个闭包结构
        def f():
            return i * i

        fs.append(f)
    return fs


# f1, f2, f3 = count()
# print(f1())
# print(f2())
# print(f3())


# typical error case2 (modify case1 code)
# this key is create a new def containing the original def
def count2():
    def f(j):
        def g():
            return j * j

        return g

    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs


# f1, f2, f3 = count2()
# print(f1())
# print(f2())
# print(f3())

# Decrator case


def PrintTime(f):
    def wapper(*args, **kwargs):
        print('now time is {0}'.format(time.ctime()))
        return f(*args, **kwargs)

    return wapper


@PrintTime
def hello():
    print('hello, world!')


# hello()

# Partial function case

# from functools import partial
# j = int('i', base=2)
# print(int('12345', base=8))
