#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# TensorFlow产生数据的三种方式,1.自产生 2.占位符获取placeholder 3.文件读取(常用)
# 在数据读取方面,倾向于tf.data库
import tensorflow as tf
import numpy as np
#---------train.string_input_producer读取方式begin----------#
# # https://zhuanlan.zhihu.com/p/27238630 创建文件名队列
# filename_queue = tf.train.string_input_producer(
#     ["iris.csv"])  # TensorFlow的读取机制,epoch完全读取1次,shuffle文件是否被打乱.
# reader = tf.TextLineReader()  # 从文件名队列中读取数据到内存队列
# key, value = reader.read(filename_queue)
#---------train.string_input_producer读取方式end----------#

#---------tf.data读取方式begin----------#
# filenames = ["iris.csv"]
dataset = tf.data.Dataset.from_tensor_slices(
    # {
    #     "a": np.array([1.0, 2.0, 3.0, 4.0, 5.0]),
    #     "b": np.random.uniform(size=(5, 2))
    # }
    np.array([1, 2, 3, 4, 5])
)
# dataset = tf.data.TextLineDataset(filenames)  # 读取数据txt,csv
dataset = dataset.map(lambda x: x+1)
iterator = dataset.make_one_shot_iterator()  # 实例化一个iterator,数据从头到尾读取一次
# 从iterator当中取出一个元素,类型是Tensor,需要sess.run()读取
one_element = iterator.get_next()
with tf.Session() as sess:
    try:
        for i in range(150):
            print(sess.run(one_element))
    except tf.errors.OutOfRangeError:
        print("end!")
#---------tf.data读取方式end----------#

# record_defaults = [[1.0], [1.0], [1.0], [1.0], [""]]
# col1, col2, col3, col4, col5 = tf.decode_csv(
#     value, record_defaults=record_defaults)
# # features = tf.concat(0, [[col1], [col2], [col3], [col4], [col5]])
# features = tf.stack([col1, col2, col3, col4])  # 把上一行注释掉用这一行也可以


# init_op = tf.global_variables_initializer()
# local_init_op = tf.local_variables_initializer()

# with tf.Session() as sess:
#     coord = tf.train.Coordinator()
#     threads = tf.train.start_queue_runners(coord=coord)  # 执行文件名队列,开始往队列里放文件名
#     # print(sess.run([features]))
#     for i in range(90):
#         print(sess.run([features]))

#     coord.request_stop()
#     coord.join(threads)
