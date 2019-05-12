#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   1.9.TFRecord.py
@Time    :   2019/05/08 15:34:55
@Author  :   Alec Shang
@Version :   1.0
@Contact :   shangjingweiwork@163.com
@License :   (C)Copyright 2019-2020
@Desc    :   None
'''
#######################
import matplotlib as mpl
mpl.use('TkAgg')
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


def write_test(input, output):
    writer = tf.python_io.TFRecordWriter(output)
    # 读取图片进行解码
    image = tf.read_file(input)
    image = tf.image.decode_jpeg(image)
    with tf.Session() as sess:
        image = sess.run(image)
        shape = image.shape
        # 将图片转换成string格式
        image_data = image.tostring()
        print(type(image))
        print(len(image_data))
        name = bytes('cat', encoding='utf-8')
        print(type(name))

        # 创建对象,并将Feature填充进去,注意feature是列表
        example = tf.train.Example(features=tf.train.Features(
            feature={
                'name': tf.train.Feature(
                    bytes_list=tf.train.BytesList(value=[name])
                ),
                'shape': tf.train.Feature(
                    int64_list=tf.train.Int64List(value=[shape])
                ),
                'data': tf.train.Feature(
                    bytes_list=tf.train.BytesList(value=[image_data])
                )
            }
        )
        )
        # 将example序列化成string类型,然后写入操作
        writer.write(example.SerializeToString())  # 序列化操作
        writer.close()


write_test('cat.jpg', 'cat.tfrecord')


def _parse_record(example_proto):
    features = {
        'name': tf.FixedLenFeature((), tf.string),
        'shape': tf.FixedLenFeature([3], tf.string),
        'data': tf.FixedLenFeature((), tf.string)
    }
    parsed_features = tf.parse_single_example(example_proto, features=features)
    return parsed_features


def read_test(input_file):
    dataset = tf.data.TFRecordDataset(input_file)
    dataset = dataset.map(_parse_record)
    iterator = dataset.make_one_shot_iterator()
    # tf.data.Dataset.make_one_shot_iterator()

    with tf.Session() as sess:
        features = sess.run(iterator.get_next())
        name = features['name']
        name = name.decode()
        img_data = features['data']
        shape = features['shape']

        # 从bytes数组中加载图片原始数据,并重新reshape.结果为ndarray数组
        img_data = np.fromstring(img_data, dtype=np.uint8)  # 获取解析后的数据
        img_data = np.reshape(img_data, shape)

        plt.figure()
        plt.imshow(img_data)
        plt.show()

        # 将数据重新编码成jpg图片并保存
        img = tf.image.encode_jpeg(img_data)  # 将图片数据编码成jpeg格式
        tf.gfile.GFile('***.jpg', 'wb').write(img.eval())  # 将图片数据保存到本地


read_test()
