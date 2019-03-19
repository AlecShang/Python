#!/usr/local/bin/python3
# -*- encoding: utf-8 -*-
'''
@File    :   function.py
@Time    :   2019/03/18 16:14:07
@Author  :   Alec Shang
@Version :   1.0
@Contact :   shangjingweiwork@163.com
@License :   (C)Copyright 2019-2020
@Desc    :   None
'''
#######################
import collections
from collections import deque
# from collections import defaultdict
from collections import Counter

# zip; enumerate; collections(dequeue; defaultdict; Counter )

# zip case and zip(*)为解码

n = [1, 2, 3, 4]
m = [6, 7, 8, 9]
# print(list(zip(n, m)))

zipped = zip(n, m)
# print(list(zipped))
# # print zipped之后, 里边的内容为何会被清空?
# print(list(zip(*zipped)))

# enumerate case

i = [1, 2, 3, 4, 5, 6, 7]
l1 = enumerate(i)
# for j in l1:
#     print(j)

# collections case

Point = collections.namedtuple("Point", ['x', 'y', 'z'])
p = Point(11, 22, 33)
# print(p[2])

# deque case
q = deque(['a', 'b', 'c'])
# print(q)

# q.appendleft('d')
# print(q)

# q.insert(2, 'e')
# print(q)

# defaultdict case

dic1 = {'one': 1, 'two': 2, 'three': 3}
# func = lambda: '返回字典默认字符'
# dic1 = defaultdict(func)
# print(dic1['one'])

# counter case
c = Counter('asfoijsgisamviosdmioehwgnweiohgkwlengornher')
print(c)
