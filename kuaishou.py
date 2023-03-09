#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   kuaishou.py
@Time    :   2020/04/12 16:36:41
@Author  :   Alec Shang
@Version :   1.0
@Contact :   shangjingweiwork@163.com
@License :   (C)Copyright 2019-2020
@Desc    :   None
'''
#######################

#coding=utf-8
    # 1.如果发现左括号，则等待匹配右括号，左括号依然可以进入匹配，每匹配到一组括号则输出一组括号。
    # 2.如果先发现右括号，则输出落单右括号+1
    # 3.遍历完整个数组后，输出落单的左右括号，

arr=input('')
left=[]
right=[]
leftNum=0
rightNum=0
indexArr=0
# 传入所有字符
for i in arr:
    left.append(i)
leftLen=int(len(left))
for i in range(leftLen):
    if left[i]=='(':
        for j in range(i+1,leftLen):
            if left[j]==')':
                indexArr+=1
                break
    elif left[i]==')':
        rightNum+=1
print(indexArr,' ',leftNum,' ',rightNum)