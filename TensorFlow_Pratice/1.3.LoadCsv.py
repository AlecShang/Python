#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   1.3.LoadCsv.py
@Time    :   2019/04/20 16:05:38
@Author  :   Alec Shang
@Version :   1.0
@Contact :   shangjingweiwork@163.com
@License :   (C)Copyright 2019-2020
@Desc    :   None
'''
#######################
# import tensorflow as tf
# # 读取csv文件内容
# sess = tf.Session()
# filename = tf.train.string_input_producer(
#     tf.train.match_filenames_once('./*.csv'))
# reader = tf.TextLineReader(skip_header_lines=1)
# key, value = reader.read(filename)
# record_defaults = [[0.], [0.], [0.], [0.], ['']]
# col1, col2, col3, col4, col5 = tf.decode_csv(value, record_defaults)
# features = tf.stack([col1, col2, col3, col4])

# sess.run(tf.global_variables_initializer())
# coord = tf.train.Coordinator()
# threads = tf.train.start_queue_runners(coord=coord, sess=sess)

# for i in range(0, 5):
#     example = sess.run([features])
#     print(example)
#     coord.request_stop()
#     coord.join(threads)


# TensorFlow产生数据的三种方式,1.自产生 2.占位符获取placeholder 3.文件读取(常用)
import tensorflow as tf

filename_queue = tf.train.string_input_producer(["iris.csv"])

reader = tf.TextLineReader()
key, value = reader.read(filename_queue)

record_defaults = [[1.0], [1.0], [1.0], [1.0], [""]]
col1, col2, col3, col4, col5 = tf.decode_csv(
    value, record_defaults=record_defaults)
# features = tf.concat(0, [[col1], [col2], [col3], [col4], [col5]])
features = tf.stack([col1, col2, col3, col4])  # 把上一行注释掉用这一行也可以


init_op = tf.global_variables_initializer()
local_init_op = tf.local_variables_initializer()

with tf.Session() as sess:
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(coord=coord)
    # print(sess.run([features]))
    for i in range(90):
        print(sess.run([features]))

    coord.request_stop()
    coord.join(threads)
