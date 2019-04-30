#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   1.4.LoadJPG.py
@Time    :   2019/04/23 16:10:12
@Author  :   Alec Shang
@Version :   1.0
@Contact :   shangjingweiwork@163.com
@License :   (C)Copyright 2019-2020
@Desc    :   None
'''
#######################
import matplotlib.pyplot as plt
import tensorflow as tf


image_value = tf.read_file('B.jpg')
img = tf.image.decode_jpeg(image_value, channels=3)

with tf.Session() as sess:
    img_ = img.eval()
    print(img_.shape)
    print(img_.dtype)

plt.figure(1)
plt.imshow(img_)
plt.show()
