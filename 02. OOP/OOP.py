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


class Student():
    def __init__(self):
        print('this is a Student init operation!')
        print('this is a student class!')


class PythonStudent(Student):
    name = None
    age = 18
    address = 'Yunnan university of finance and economics'

    __sex = '女'

    def __init__(self):
        self.name = 'shang'
        self.age = 20

        print('this is a PythonStudent init operation!')

    def say(self):
        print('my name is {0} and i am {1}'.format(self.name, __class__.age))
        return 1


python_student = PythonStudent()
print(python_student.age)
print(python_student.say())
print(python_student.__dict__)
print(PythonStudent.__dict__)
