#!/usr/bin/python
# -*- coding-utf8


import re
import os

lines = open("outnetip202002261333sh.txt",'r')
for line in lines:
    #print line
    result = re.match(r'((25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.){3}(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)"',line)
    if result is not None:
         print line