#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   1.8.TensorflwDataset.py
@Time    :   2019/05/05 11:04:14
@Author  :   Alec Shang
@Version :   1.0
@Contact :   shangjingweiwork@163.com
@License :   (C)Copyright 2019-2020
@Desc    :   None
'''
#######################
import tensorflow as tf
import numpy as np
import tensorflow.contrib.eager as tfe  # 使用tf.eager()模式

tfe.enable_eager_execution()

# 先创建,再实例化,再迭代
dataset = tf.data.Dataset.from_tensor_slices(np.arange(5))
for i in tfe.Iterator(dataset):
    print(i + 1)
