#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   02.Tensorboard.py
@Time    :   2019/04/20 10:59:15
@Author  :   Alec Shang
@Version :   1.0
@Contact :   shangjingweiwork@163.com
@License :   (C)Copyright 2019-2020
@Desc    :   None
'''
#######################
import tensorflow as tf
import numpy as np

# 1.创建数据
with tf.name_scope('Input'):
    x = np.float32(np.random.rand(1, 100))
    # y = x*0.3+0.1
    y = np.dot([0.100], x) + 0.300
with tf.name_scope('Argument'):
    W = tf.Variable(tf.random_uniform(
        [1, 1], -1.0, 1.0), tf.float32, name='Arg_W')
    b = tf.Variable(tf.zeros([1]), tf.float32, name='Arg_b')
    y_ = tf.matmul(W, x)+b

with tf.name_scope('Loss'):
    loss = tf.reduce_mean(tf.math.square(y_-y))
optimizer = tf.train.GradientDescentOptimizer(0.6)
train = optimizer.minimize(loss)

init = tf.global_variables_initializer()
sess = tf.Session()

sess.run(init)
tf.summary.scalar('loss', loss)
merge = tf.summary.merge_all()
writer = tf.summary.FileWriter('logs/', sess.graph)
for i in range(200):
    summary, _ = sess.run([merge, train])
    if i % 20 == 0:
        writer.add_summary(summary)
        print(i, sess.run(W), sess.run(b))
