#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   mnist.py
@Time    :   2019/04/14 10:26:18
@Author  :   Alec Shang
@Version :   1.0
@Contact :   shangjingweiwork@163.com
@License :   (C)Copyright 2019-2020
@Desc    :   None
'''
#######################
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# 1.导入数据
# 导入数据MNIST,方式用one_hot(除了一个1其他为0的向量)
# 注释: 在此数据集当中,因为需要识别的是数字0-9,所以one_hot是一个10维的向量,
# [1,0,0,0,0,0,0,0,0,0]就是表示数字0.[0,0,0,0,0,0,0,0,0,1]表示9
mnist_data = input_data.read_data_sets('MNIST_data/', one_hot=True)

# 2.建立模型
# 可以先定义几个全局量,在这里可以称之为超参数
learning_rate = 0.5
epochs = 10
batch_size = 100

# 在placeholder当中的shape表示的是张量的形状,此位置表示一个二维向量
# 其中None表示的是第一维可以是任何值
x = tf.placeholder(tf.float32, [None, 784])
# 一般定义y为目标数据,即想要达成的数据.这里想要分析出来的是0-9数字.
y = tf.placeholder(tf.float32, [None, 10])
# W代表加权值 图片X是不是数字i可以表示为(Wi,j)*Xj+Bi, 其中j代表X图像的像素索引
# 因为计算公式一般为y=Wx+b所以定义W矩阵时也比较好思考,应该是W行*x列,即W[784,*]
W = tf.Variable(tf.zeros([784, 10]))
# b代表偏置值,shape=(10,)代表的是一维数组,数组中有10个元素.
b = tf.Variable(tf.zeros([10]))

# 利用softmax函数求值
y_ = tf.nn.softmax(tf.add(tf.matmul(x, W), b))


# 3.设置衡量模型参数
# 为了衡量模型的好坏,或者说是验证模型的loss或cost
# 一般用交叉熵(cross-entropy)来衡量.
# y_ = tf.placeholder(tf.float32, [None, 10])
cross_entropy = tf.reduce_sum(y_*tf.log(y))

# 4.设置学习算法,步骤和学习速率
# 这里是利用GradientDescentOptimizer算法以0.01的速率最小化(minimize)交叉熵(cross_entropy)
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

# 5.初始化
init = tf.global_variables_initializer()

# 6.启动模型
sess = tf.Session()
sess.run(init)

# 7.训练模型
for i in range(300):
    # batch_xs, batch_ys = mnist.train.next_batch(5)
    # sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})
    sess.run(train_step)

# # 8.评估模型
# correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
# accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
# print(sess.run(accuracy, feed_dict={
#       x: mnist.test.images, y_: mnist.test.labels}))
