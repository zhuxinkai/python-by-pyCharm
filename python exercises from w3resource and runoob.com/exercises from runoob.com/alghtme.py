#coding=utf-8

#有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

#程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。
for i in range(1,5):
    for j in range(1,5):
        for x in range(1,5):
            for t in range(1,5):
                if(i != j and x !=j and i != x and t != i and t != j and t != x):
                    print(i*1000 + j*100 + x*10 + t)
