#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Kears.py
@Time    :   2019/05/11 15:27:50
@Author  :   Alec Shang
@Version :   1.0
@Contact :   shangjingweiwork@163.com
@License :   (C)Copyright 2019-2020
@Desc    :   None
'''
#######################
import tensorflow as tf

mnist = tf.keras.datasets.mnist

print(mnist.load_data())
