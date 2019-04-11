#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   example.py
@Time    :   2019/03/25 15:06:25
@Author  :   Alec Shang
@Version :   1.0
@Contact :   shangjingweiwork@163.com
@License :   (C)Copyright 2019-2020
@Desc    :   None
'''
#######################

# import tensorflow as tf
# # tensorflow graph 整个过程要执行a = (b+c)*(c+2)
# # 其中为了突显异步运算.要将b+c=e, c+2=d
# # 1.定义量 如常量constant,变量Variable
# # 2.定义运算 如operation,一般用函数代替运算如'+'用add()代替
# # 3.初始化
# # 4.建立会话,即输出

# # 1. 定义量
# # 第一步定义一个常量,一般用constant
# const = tf.constant(2.0, name='Const')
# # # 第二步定义两个变量,用Variable
# # b = tf.Variable(4.0, dtype=tf.float32, name='b')
# # # 可以将b设置成可接收任意值
# b = tf.placeholder(tf.float32, [None, 1], name='b')
# c = tf.Variable(1.0, dtype=tf.float32, name='c')

# # 2. 定义运算operation
# # 加法运算用add()来表示,如e=b+c
# e = tf.add(b, c, name='e')
# d = tf.add(c, const, name='c')
# # 定义乘法运算用multiply(),a=e*d
# a = tf.multiply(e, d, name='a')

# # 3. 初始化operation
# init_operation = tf.global_variables_initializer()


# # 4. 建立会话Session,即输出
# with tf.Session() as sess:
#     # 运行初始化
#     sess.run(init_operation)
#     # sess_output = sess.run(a)
#     # # 修改占位符之后需要修改sess.run(a)
#     sess_output = sess.run(
#         a, feed_dict={b: [[1, ], [2, ], [3, ], [4, ], [5, ]]})
#     print(sess_output)
#     # tensorboard 画图


# 神经网络的例子.
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
# one_hot=True表示对label进行one-hot编码，
# 比如标签4可以表示为[0, 0, 0, 0, 1, 0, 0, 0, 0, 0]。
# 这是神经网络输出层要求的格式。
mnist = input_data.read_data_sets('MNIST_data/', one_hot=True)

# 超参数
learning_rate = 0.5
epochs = 10
batch_size = 100

# 输入图片为28 x 28 像素 = 784
x = tf.placeholder(tf.float32, [None, 784], name='x')
# 输出为0-9的one-hot编码
y = tf.placeholder(tf.float32, [None, 10], name='y')

# hidden layer => w, b
W1 = tf.Variable(tf.random_normal([784, 300], stddev=0.03), name='W1')
b1 = tf.Variable(tf.random_normal([300]), name='b1')
# output layer => w, b
W2 = tf.Variable(tf.random_normal([300, 10], stddev=0.03), name='W2')
b2 = tf.Variable(tf.random_normal([10]), name='b2')


# hidden layer
hidden_out = tf.add(tf.matmul(x, W1), b1)
hidden_out = tf.nn.relu(hidden_out)

# 计算输出
y_ = tf.nn.softmax(tf.add(tf.matmul(hidden_out, W2), b2))

y_clipped = tf.clip_by_value(y_, 1e-10, 0.9999999)
cross_entropy = -tf.reduce_mean(tf.reduce_sum(y *
                                              tf.log(y_clipped) + (1 - y) * tf.log(1 - y_clipped), axis=1))

# 创建优化器，确定优化目标
optimizer = tf.train.GradientDescentOptimizer(
    learning_rate=learning_rate).minimizer(cross_entropy)

# init operator
init_op = tf.global_variables_initializer()

# 创建准确率节点
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

# 创建session
with tf.Session() as sess:
    # 变量初始化
    sess.run(init_op)
    total_batch = int(len(mnist.train.labels) / batch_size)
    for epoch in range(epochs):
        avg_cost = 0
        for i in range(total_batch):
            batch_x, batch_y = mnist.train.next_batch(batch_size=batch_size)
            _, c = sess.run([optimizer, cross_entropy],
                            feed_dict={x: batch_x, y: batch_y})
            avg_cost += c / total_batch
        print("Epoch:", (epoch + 1), "cost = ", "{:.3f}".format(avg_cost))
    print(sess.run(accuracy, feed_dict={
          x: mnist.test.images, y: mnist.test.labels}))
