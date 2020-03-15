#!/usr/bin/python
# -*- coding: utf-8 -*-


#reuslt ['car', 'car', 'car', 'car'], 这与 re.match ,和 re.search 不同，直接返回包含一个值的数组。
import re
print(re.findall('car','this car is a bigcar .and find inn the car house .and carhouse is a buiding'))

# re.I 不区分大小写。
s ='this and that'
print(re.findall(r'(th\w+) and (th\w+)' ,s,re.I))

print(re.finditer(r'(th\w+) and (th\w+)',s,re.I).next().groups())

print(re.finditer(r'(th\w+)',s,re.I).next().group(1))

it=re.finditer(r'(th\w+)',s,re.I)
g = it.next()
print("---------------------")

print(g.groups(1))
print("---------------------")
g = it.next()
print(g.groups(1))

