#!/usr/local/bin/python3
# -*- encoding: utf-8 -*-
'''
@File    :   OOP.py
@Time    :   2019/03/16 10:45:00
@Author  :   Alec Shang
@Version :   1.0
@Contact :   shangjingweiwork@163.com
@License :   (C)Copyright 2019-2020
@Desc    :   None
'''

#######################

# import sys

# print('aaa')
# class StudentPython():
#     student_number = '001'
#     student_age = '18'
#     student_major = 'computer'

#     def DoHomework(self):
#         print('please do homework!')
#         print('then you can play!')

#         return None

# shang = StudentPython()
# print(shang.student_age)
# print(shang.DoHomework())
# print(StudentPython.__dict__)

# class A():
#     self._name = 'AAAA'
#     def __init__(self):
#         print('is print A?')
#         pass

# class B(A):
#     # def __init__(self):
#     #     pass
#     #     print('just see is it print?')
#     pass

# b = B()
# print(b._name)

# class Student():
#     _name = 'shangjingwei'

#     def __init__(self):
#         print('this is a Student init operation!')
#         print('this is a student class!')

#     def work(self):
#         print('need working...')

# class PythonStudent(Student):
#     name = None
#     age = 18
#     address = 'Yunnan university of finance and economics'

#     __sex = '女'

#     def __init__(self):
#         self.name = 'shang'
#         self.age = 20

#         print('this is a PythonStudent init operation!')

#     def say(self):
#         print('my name is {0} and i am {1}'.format(self.name, __class__.age))
#         return 1

#     def work(self):
#         super().work()
#         self.say()

# python_student = PythonStudent()
# print(issubclass(Student, PythonStudent))
# print(PythonStudent._name)
# print(python_student.age)
# print(python_student.say())
# print(python_student.__dict__)
# print(PythonStudent.__dict__)

# property(fget, fset, fdel, fdoc)的使用
# 无论输入什么类型的数字,都将其转换为整数

# class Person():
#     # _name = None
#     _name = 'aaa'

#     def fget(self):
#         return self._name * 2

#     def fset(self, name):
#         self._name = name.upper()

#     def fdel(self):
#         del self._name

#     def fdoc(self):
#         print('this is a property')

#     x = property(fget, fset, fdel, fdoc)

# # p.x 将触发 getter,p.x = value 将触发 setter ， del p.x 触发 deleter。

# p = Person()
# p.x = "shang"
# print(p.x)

# 三种方法的实现,实例方法;类方法;静态方法
# class Student():
#     # 实例方法
#     def A(self):
#         pass

#     # 类方法
#     def B(cls):
#         pass

#     # 静态方法
#     def C():
#         pass

# 抽象类的实现
import abc


# 声明一个元类,并且指定当前类的元类
class Human(metaclass=abc.ABCMeta):
    # 定义一个抽象方法
    @abc.abstractmethod
    def eating(self):
        pass
