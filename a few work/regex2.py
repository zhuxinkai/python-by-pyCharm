#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
m = re.search('^end','endand')
print(m.group())

m2 = re.search(r'\bbit','bitsecond')
if m2 is not None: print(m2.group())

m3 = re.search(r'(\bbit)','secondbit and')
# groups must have the () ,sub collection;
if m3 is not None: print(m3.groups())
if m3 is None: print("m3 is None")


# no boundary
# 需要对匹配的时候，进行
# r 表示后面的为非bashell 方式，而是普通的字符。（这个解释好像不行）。
m4 = re.search(r'(\Bbit)','secondbit and')
if m4 is not None: print(m4.groups())
if m4 is None: print("m4 is None")

