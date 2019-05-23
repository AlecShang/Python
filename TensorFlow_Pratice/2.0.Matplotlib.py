#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   2.0.Matplotlib.py
@Time    :   2019/05/13 16:54:52
@Author  :   Alec Shang
@Version :   1.0
@Contact :   shangjingweiwork@163.com
@License :   (C)Copyright 2019-2020
@Desc    :   None
'''
#######################

import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

x = np.random.randint(0, 10, size=1000)
y = np.random.randint(-20, 20, size=1000)
z = np.random.randint(0, 30, size=1000)

# 此处fig是二维
fig = plt.figure()

# 将二维转化为三维
ax = Axes3D(fig)

# 数据数目
n = 256
# 定义x, y
x = np.arange(-4, 4, 0.25)
y = np.arange(-4, 4, 0.25)

# 生成网格数据
X, Y = np.meshgrid(x, y)

# 计算每个点对的长度
R = np.sqrt(X ** 2 + Y ** 2)
# 计算Z轴的高度
Z = np.sin(R)

# 绘制3D曲面
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'))
# 绘制从3D曲面到底部的投影
ax.contour(X, Y, Z, zdim='z', offset=-2, cmap='rainbow')

# 设置z轴的维度
ax.set_zlim(-2, 2)

plt.show()
