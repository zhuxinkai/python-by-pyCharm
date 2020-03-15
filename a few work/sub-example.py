#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
#result attn: Mr. Smith

#Dear Mr. Smith,
print(re.sub('X','Mr. Smith' , 'attn: X\n\nDear X, \n'))

#result ('attn: Mr. Smith\n\nDear Mr. Smith, \n', 2) ,参数1 ，替换代替位置。 参数2 ，实参， 参数3 实际的文本
#subn 和sub的区别在于， subn 返回2个元素的数组，其中一个元素是替换的个数。

print(re.subn('X','Mr. Smith' , 'attn: X\n\nDear X, \n'))

#大括号里面的数字，表示的是数字的位数，{1,2}表示的是1-2位数字。
print(re.sub(r'(\d{1,2})/(\d{1,2)/(\d{2}|\d{4})',r'\3/\2/\1','02/20/91'))