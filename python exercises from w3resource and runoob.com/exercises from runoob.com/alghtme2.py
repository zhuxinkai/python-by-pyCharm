#coding=utf-8

#求1000000内的对数。

i=0
while i <=1000000:

    j = i - i %10
    if (i == j):
        print(i)

    i = i+1