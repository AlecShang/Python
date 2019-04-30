#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   1.6.K-means.py
@Time    :   2019/04/28 10:07:28
@Author  :   Alec Shang
@Version :   1.0
@Contact :   shangjingweiwork@163.com
@License :   (C)Copyright 2019-2020
@Desc    :   None
'''
#######################
# K-means简介,不断的寻找质心和改变质心来进行分类,目的是将数据分配到不同的组别当中
import tensorflow as tf
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

plt.figure()
plt.subplot(2, 1, 1)  # 表示整个图像分割成2行2列，当前位置为1
plt.plot([0, 1], [0, 1])  # 横坐标变化为[0,1] 竖坐标变化为[0,2]

plt.subplot(2, 3, 4)
plt.plot([0, 1], [0, 2])

plt.subplot(2, 3, 5)
plt.plot([0, 1], [0, 3])

plt.subplot(2, 3, 6)
plt.plot([0, 1], [0, 4])
plt.show()
