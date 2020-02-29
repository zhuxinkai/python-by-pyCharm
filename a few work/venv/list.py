#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
fred = 200
print(fred)

join = fred
print(join)

print(join + fred)

print("the result is %d" %(fred+join))

print(re.match('abc', 'abc').group())
#if m is not None: print(m.group())
m = re.match('abc','babc')
if m is not None: m.group()

patt = '\w+@\w+\.com'
paobject = 'zhuxinkai@126.com'
paobject2 = 'zhuxinkai@126.wyn88.com'
paobject3 = 'zhuxinkai@126.wyn88.cn'
paobject4 = 'zhuxinkai-liusha@126.wyn88.com'
patt2 = '\w+@\w+(\.\w+)?(\.com|\.cn)'

#测试中文注释  需要加入如下的coding 注释
# !/usr/bin/python
# -*- coding: utf-8 -*-

patt3 = '\w+(\W+)*\w+@\w+(\.\w+)?(\.com|\.cn)'

print(re.match(patt,paobject).group())
if(re.match(patt,paobject2) is not None): print(re.match(patt,paobject2).group())
print(re.match(patt2,paobject2).group())
print(re.match(patt2,paobject3).group())
if(re.match(patt2,paobject4) is not None): print(re.match(patt2,paobject4).group())
print("--------------")
if(re.match(patt3,paobject4) is not None): print(re.match(patt3,paobject4).group())


