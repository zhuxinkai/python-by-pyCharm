#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

# 利用（？i）不区分大小写。
m = re.findall(r'(?i)the\w+','thead and Theod tHek')
print(m)
