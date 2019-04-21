#!/usr/local/bin/python3
# -*- encoding: utf-8 -*-
'''
@File    :   try.py
@Time    :   2019/03/16 10:39:23
@Author  :   Alec Shang
@Version :   1.0
@Contact :   shangjingweiwork@163.com
@License :   (C)Copyright 2019-2020
@Desc    :   None
'''

# here put the import lib



try:
    l = [1,2,3,4]
    print(l[4])
except Exception as e:
    print(e)
    print('error!!!')
finally:
    print('Done......')