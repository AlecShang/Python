#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   example.py
@Time    :   2019/04/30 15:54:53
@Author  :   Alec Shang
@Version :   1.0
@Contact :   shangjingweiwork@163.com
@License :   (C)Copyright 2019-2020
@Desc    :   None
'''
#######################

import tensorflow as tf
import numpy as np

# 先创建一个原始的数据集,这里我先创建100个随机的数字
# 在原始案例当中创建的是一个[2,100]的二维随机数组
# 我这里先创建一个一维数组,看看是否可行.
x_raw_data = np.random.rand(1, 100)
# 在创建预定的y_raw_data,就是最终的训练集,主要是为了是x_raw_data到y_raw_data
# 无限的调整中间的def,使之能够不断的调整参数.在线性问题中主要用的就是y=W*x+b
# 所以在这里设置y_raw_data的时候就是要用到上边的公式,先设定一个W和一个b
# 然后通过不断的调整,训练,最后可以使设定的W和b和在这里输入的值无限接近.
y_raw_data = np.dot([2.0], x_raw_data) + 0.3

# 接下来就是设置需要不断调整的参数.W和b还有y_output_data
# W是一个随机数,且根据上边写的要求,这里我需要W是一个随机的数
W = tf.Variable(np.zeros([1, 1]))
b = tf.Variable(np.zeros([1]))
y_output_data = W * x_raw_data + b
loss = tf.reduce_mean(tf.square(y_output_data - y_raw_data))
train = tf.train.GradientDescentOptimizer(0.5).minimize(loss)
init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    for i in range(100):
        sess.run(train)
        print(i, sess.run(W), sess.run(b), sess.run(loss))
