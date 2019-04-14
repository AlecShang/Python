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
mnist_data = input_data.read_data_sets('MNIST.data', one_hot=True)
