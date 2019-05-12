#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   1.7.MINIST.py
@Time    :   2019/05/04 15:04:24
@Author  :   Alec Shang
@Version :   1.0
@Contact :   shangjingweiwork@163.com
@License :   (C)Copyright 2019-2020
@Desc    :   None
'''
#######################
import tensorflow as tf
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets('../MNIST_data', one_hot=True)

# x_raw = tf.placeholder(tf.float32, shape=[None, 784])
# y_raw = tf.placeholder(tf.float32, shape=[None, 10])

x_raw = tf.constant(mnist.train.images, dtype=tf.float32)
y_raw = tf.constant(mnist.train.labels, dtype=tf.float32)

W_hidden1 = tf.Variable(tf.random_normal([784, 300], stddev=0.03))
b_hidden1 = tf.Variable(tf.random_normal([300]))
W = tf.Variable(tf.random_normal([300, 10], stddev=0.03))
b = tf.Variable(tf.random_normal([10]))
y_hidden1 = tf.nn.relu(tf.add(tf.matmul(x_raw, W_hidden1), b_hidden1))
y_output = tf.nn.softmax(tf.add(tf.matmul(y_hidden1, W), b))
# 可以用很多种不同的计算损失的公式,例如交叉熵
loss = tf.reduce_mean(tf.square(y_output - y_raw))
train = tf.train.GradientDescentOptimizer(0.1).minimize(loss)
init = tf.global_variables_initializer()

# 创建准确率节点
correct_prediction = tf.equal(tf.argmax(y_raw, 1), tf.argmax(y_output, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

with tf.Session() as sess:
    sess.run(init)
    for i in range(100):
        if i % 10 == 0:
            sess.run(train)
            print(sess.run(loss))
