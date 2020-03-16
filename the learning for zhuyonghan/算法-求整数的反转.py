# coding=utf-8
#This program is designed for plus calculations.
#!C:\Program Files\Python37



def reverse(x):
    num = 0
    if x == 0:
        return 0
# 如果数字未负数，则将其转换成正数。
    if x < 0:
        x = -x
        while x != 0:
            num = num * 10 + x % 10
            x = x / 10
# 结果返回前，将其重置未负数。
        num = -num
    else:
        while x != 0:
            num = num * 10 + x % 10
            x = x / 10

    if num>pow(2,31)-1 or num < pow(-2,31):
        return 0
    return num


print(reverse(-25466))
