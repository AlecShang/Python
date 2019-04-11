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

# # 74. 列表排序及连接。
# l1 = [1, 3, 2]
# l1.sort()
# print(l1)

# l2 = [4, 5, 6]
# l1.extend(l2)
# print(l1)

# 75. 略过。

# # 76. 编写一个函数，
# # 输入n为偶数时，调用函数求1/2+1/4+...+1/n,
# # 当输入n为奇数时，调用函数1/1+1/3+...+1/n


# def func_oddnumber(x):
#     y = 1.0
#     for i in range(1, x+1, 2):
#         # 每次分母都是奇数加1
#         y /= i
#     return y


# def func_evennumber(x):
#     y = 1.0
#     for i in range(1, x+1, 2):
#         # 每次分母都是偶数加1
#     return y


# if __name__ == "__main__":
#     x = int(input('please input number:'))
#     if x % 2 != 0:
#         print(func_oddnumber(x))
#     else:
#         print(func_evennumber(x))


# # 77. 循环输出列表

# l1 = ['aaa', 'bbb', 'ccc']
# for i in l1:
#     print(i)

# # 78. 找到年龄最大的人，并输出。
# if __name__ == '__main__':
#     person = {"li": 18, "wang": 50, "zhang": 20, "sun": 22}
#     m = 'li'
#     for key in person.keys():
#         if person[m] < person[key]:
#             m = key
#     print('{0},{1}'.format(m, person[m]))

# 79. 字符串排序。(略过)

# 80.海滩上有一堆桃子，五只猴子来分。
# 第一只猴子把这堆桃子平均分为五份，多了一个，
# 这只猴子把多的一个扔入海中，拿走了一份。
# 第二只猴子把剩下的桃子又平均分成五份，又多了一个，
# 它同样把多的一个扔入海中，
# 拿走了一份，第三、第四、第五只猴子都是这样做的，
# 问海滩上原来最少有多少个桃子？

# 分析:假设原来海滩上有x个桃子.经过5次循环之后
# # 假如还有6个桃子,最后求出结果.3121
# y = 1
# for i in range(1, 6):
#     y = y*5+1
#     print(y)
