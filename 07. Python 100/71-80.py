#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   71-80.py
@Time    :   2019/04/07 10:55:03
@Author  :   Alec Shang
@Version :   1.0
@Contact :   shangjingweiwork@163.com
@License :   (C)Copyright 2019-2020
@Desc    :   None
'''
#######################
# # 71. 编写input()和output()函数输入，输出5个学生的数据记录。
# stu_list = [[] for j in range(5)]
# print(stu_list)


# def stu_input(i):
#     stu_num = input('please input student num:')
#     stu_score = int(input('please input student score:'))
#     stu_list[i].append(stu_num)
#     stu_list[i].append(stu_score)


# def stu_output():
#     pass


# if __name__ == "__main__":
#     for i in range(5):
#         stu_input(i)
#     print(stu_list)


# ***72. 创建一个链表。

# 73. 反向输出一个链表。

# 74. 列表排序及连接。
l1 = [1, 3, 2]
l1.sort()
print(l1)

l2 = [4, 5, 6]
l1.extend(l2)
print(l1)
