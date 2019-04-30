#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   1.5.numpy.py
@Time    :   2019/04/27 14:30:28
@Author  :   Alec Shang
@Version :   1.0
@Contact :   shangjingweiwork@163.com
@License :   (C)Copyright 2019-2020
@Desc    :   None
'''
#######################
import numpy as np
a = np.arange(15).reshape(3, 5)
print('轴为:', a.ndim)
print('维度为:', a.shape)
print('所有元素的数目为:', a.size)
print('元素类型为:', a.dtype)
print('所有元素的字节数为:', a.itemsize)

b = np.array([[1, 2], [3, 4]], dtype=complex)
print(b)

c = np.zeros([3, 4])
print(c)

d = np.ones([2, 2])
print(d)

e = np.empty([3, 3])
print(e)

f = np.linspace(-1, 1, 10)
print(f)
