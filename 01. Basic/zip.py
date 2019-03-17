#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

list_a = [1,2,3]
list_b = [4,5,6]
list_c = [7,8,9]

zip_a = zip(list_a,list_b,list_c)

print(list(zip_a))

zip_b, zip_c = zip(*zip(list_a,list_b))
print(list(zip_b))
print(list(zip_c))