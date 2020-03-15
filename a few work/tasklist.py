#!/usr/bin/env pthon
# -*- coding: utf-8 -*-

import re
import os


f = os.popen('tasklist /nh','r')
for eachline in f:
   # print eachline
    #print (re.findall(r'([\w.]+(?: [\w.]+)*)\s\s+(\d+) \w+\s\s+\d+\s\s+([\d,]+k)' , eachline.rstrip()))
   # print re.findall(r'(\w+.\w+)\s\s+(\d+)', eachline.rstrip())
   print(re.findall(r'([\w.]+(?:[\w.]+)*)\s\s+(\d+) \w+\s\s+\d+\s\s+([\d,]+ K)', eachline.rstrip()))
f.close()