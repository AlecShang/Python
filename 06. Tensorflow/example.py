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


# 官方的新手入门
import tensorflow as tf
import numpy as np
from matplotlib import pyplot as plt

# 使用 NumPy 生成假数据(phony data), 总共 100 个点.
with tf.name_scope('input'):
    x_data = np.float32(np.random.rand(2, 100))  # 随机输入
    y_data = np.dot([0.100, 0.200], x_data) + 0.300


# 构造一个线性模型
with tf.name_scope('BBBBBB'):
    b = tf.Variable(tf.zeros([1]))
    W = tf.Variable(tf.random_uniform([1, 2], -1.0, 1.0))
    y = tf.matmul(W, x_data) + b


# # 使用matplotlib 画图
# fig = plt.figure()  # 先生成一个图片框
# ax = fig.add_subplot(1, 1, 1)
# ax.scatter(x_data, y_data)
# plt.show()
# 最小化方差
with tf.name_scope('loss-model'):
    loss = tf.reduce_mean(tf.square(y - y_data))
    tf.summary.scalar('loss', loss)
optimizer = tf.train.GradientDescentOptimizer(0.6)
train = optimizer.minimize(loss)

# 初始化变量
# init = tf.initialize_all_variables()
init = tf.global_variables_initializer()

# 启动图 (graph)
sess = tf.Session()
sess.run(init)

# 收集操作数据
merged = tf.summary.merge_all()
# 写入文件
writer = tf.summary.FileWriter('logs/', sess.graph)


# 拟合平面
for step in range(0, 201):
    summary, _ = sess.run([merged, train])
    writer.add_summary(summary, step)
    if step % 20 == 0:
        print(step, sess.run(W), sess.run(b))


# # 高级模型
# # 建立特征向量
# feature_columns = [tf.feature_column.numeric_column('x', [1])]

# # 创建训练器
# estimator = tf.estimator.LinearRegressor(feature_columns=feature_columns)
