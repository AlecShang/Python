#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   01.Tensor.py
@Time    :   2019/04/18 14:13:35
@Author  :   Alec Shang
@Version :   1.0
@Contact :   shangjingweiwork@163.com
@License :   (C)Copyright 2019-2020
@Desc    :   None
'''
#######################
import tensorflow as tf
import collections
# 主要学习张量的分割
tf.InteractiveSession()
x = tf.constant([0, 1, 1, 2, 2])
y = tf.constant([[0, 1, 1, 2, 1],
                 [-1, 2, 4, 1, 2],
                 [5, 6, 32, 5, 1],
                 [6, 2, 3, 1, 1],
                 [-1, -2, -3, -4, -5]])
z = tf.constant([1, 2, 3, 4, 5, 6, 7, 8])
t = tf.constant([[True, False], [False, True]])
# print(tf.segment_sum(y, x).eval())  # 相同索引相加
# print(tf.segment_mean(y, x).eval())  # 相同索引求向前中值
# print(tf.segment_max(y, x).eval())  # 相同索引求最大值
# print(tf.segment_prod(y, x).eval())  # 相同索引相乘
# print(tf.segment_min(y, x).eval())  # 相同索引求最小值

# Tensor当中的序列问题.
# print(tf.math.argmax(y, 1).eval())  # 在y当中求最大值所在位置的索引
# print(tf.math.argmin(y, 1).eval())  # 在y当中求最小值所在位置的索引
# print(tf.sets.difference(x, z).eval())  # 此函数有问题,无法实现
# print(tf.where(t).eval())
# print(tf.unique(x)[0].eval())

# Tensor的形状变换
# print(tf.shape(y).eval())
# print(tf.size(y).eval())
# print(tf.rank(y).eval())  # tensor的维数一般可以看开头和结尾的中括号的数目
# print(tf.reshape(z, [2, 4]).eval())  # 重新将Tensor进行分割
# print(tf.squeeze(input=x).eval())  # 有问题,无法实现
# print(tf.shape(tf.expand_dims(x, 0)))  # 有问题,无法实现
# print(tf.slice(y, [1, 1], [2, 2]).eval())  # 分割input,起始位置和分割大小
# print(tf.split(z, 4))  # 将input几等分,要是input的约数
# print(tf.tile(z, [2]).eval())  # 将input进行成倍增长,倍数必须用中括号[]
# paddings当中第一个中括号为行前加后加,第二个中括号表示列前加后加,且input维度需满足要求
# print(tf.pad([[1]], paddings=[[1, 1], [2, 2]]).eval())
# Tensor拼接,axis代表维度,两个shape[2,3]拼接,0拼成shape[4,3],1拼成[2,6]
# print(tf.concat([x, z], 0).eval())
# print(tf.stack([[1, 2], [3, 4]]).eval())  # 将两个input组合,确保维度相同
# print(tf.unstack([[1, 2], [3, 4]]))  # 讲一个高维Tensor分解成低维Tensor
# print(tf.reverse(y, [0]).eval())  # 0代表根据横轴交换位置,1代表根据纵轴交换,也可以[0,1]
