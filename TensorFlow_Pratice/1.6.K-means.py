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

fig = plt.figure()
# 创建数据
x = [1, 2, 3, 4, 5, 6, 7]
y = [1, 3, 4, 2, 5, 8, 6]

# 绘制大图：假设大图的大小为10，那么大图被包含在由(1,1)开始，宽8高8的坐标系之中。
left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
ax1 = fig.add_axes([left, bottom, width, height])  # main axes
ax1.plot(x, y, 'r')  # 绘制大图，颜色为red
ax1.set_xlabel('x')  # 横坐标名称为x
ax1.set_ylabel('y')
ax1.set_title('title')  # 图名称为title

# 绘制小图，注意坐标系位置和大小的改变
ax2 = fig.add_axes([0.2, 0.6, 0.25, 0.25])
ax2.plot(y, x, 'b')  # 颜色为buue
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('title inside 1')

# 绘制第二个小兔
plt.axes([0.6, 0.2, 0.25, 0.25])
plt.plot(y[::-1], x, 'g')  # 将y进行逆序
plt.xlabel('x')
plt.ylabel('y')
plt.title('title inside 2')
plt.show()
