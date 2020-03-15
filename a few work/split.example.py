#!/usr/bin/python
# -*- coding: utf-8 -*-
import re

#result ['str1', 'str2', 'str3']
result =re.split(":",'str1:str2:str3')
print(result)

#记住 if ,for ,while 在Python中需要加：

DATA = ('Mountain View, CA 94040','Sunnyvale, CA', 'Los Altos, 94023', 'Cupertino 95014','Palo Alto CA',)
for datum in DATA:
    print '----------------'
#      ?:......表示匹配一个不用保存的分组           ?=... 正向前视断言

    print re.split(',| (?= (?: \d{5}|[A-Z]{2}))',datum)
