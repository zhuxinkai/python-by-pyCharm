# coding=utf-8

#列表

list1 = [2,3,'zhuxinkai',123,'liusha']
print list1[2]
print list1[:3]
list1.append('zhuyonghan')
print len(list1)

'''
操作	解释
list.append():	追加成员
list.count(x):	计算列表中参数x出现的次数
list.extend(L):	向列表中追加另一个列表L
list.index(x):	获得参数x在列表中的位置
list.insert():	向列表中插入数据
list.pop():	删除列表中的成员（通过下标删除）
list.remove():	删除列表中的成员（直接删除）
list.reverse():	将列表中成员的顺序颠倒
list.sort():	将列表中成员排序


'''



# 元组  tuple()

# 5.元素的值一旦创建就不可修改!!!!!(这是区别与列表的一个特征）

tuple1 = ('zxk',123,392430,'tiantian')
print tuple1
'''

cmp(tuple1, tuple2)	比较两个元组元素。
len(tuple)	计算元组元素个数。
max(tuple)	返回元组中元素最大值。
min(tuple)	返回元组中元素最小值。
tuple(seq)	将列表转换为元组。

'''




#字典（Dictionary)

'''

1.元素由键（key）和值（value）组成 
2.可以用dict()函数或者方括号()创建，元素之间用逗号’,‘’分隔，键与值之间用冒号”:”隔开 
3.键必须是唯一的，但值则不必。值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组 
4.使用键（key）来访问元素


操作	解释
adict.keys()	返回一个包含字典所有KEY的列表；
adict.values()	返回一个包含字典所有value的列表；
adict.items()	返回一个包含所有（键，值）元祖的列表；
adict.clear()	删除字典中的所有项或元素；
adict.copy()	返回一个字典浅拷贝的副本；
adict.fromkeys(seq, val=None)	创建并返回一个新字典，以seq中的元素做该字典的键，val做该字典中所有键对应的初始值（默认为None）；
adict.get(key, default = None)	返回字典中key对应的值，若key不存在字典中，则返回default的值（default默认为None）；
adict.has_key(key)	如果key在字典中，返回True，否则返回False。 现在用 in 、 not in；
adict.iteritems() adict.iterkeys() adict.itervalues()	与它们对应的非迭代方法一样，不同的是它们返回一个迭代子，而不是一个列表；
adict.pop(key[,default])	和get方法相似。如果字典中存在key，删除并返回key对应的vuale；如果key不存在，且没有给出default的值，则引发keyerror异常；
adict.setdefault(key, default=None)	和set()方法相似，但如果字典中不存在Key键，由 adict[key] = default 为它赋值；
adict.update(bdict)	将字典bdict的键值对添加到字典adict中。

'''





#集合 set
'''
具有以下特点： 
1.可以用set()函数或者方括号{}创建，元素之间用逗号”,”分隔。 
2.与字典相比少了键 
3.不可索引，不可切片 
4.不可以有重复元素

# 两种方法创建
set1 = set('kydaa')
set2 = {'abc', 'jaja', 'abc', 'kyda'}
print(set1)
print(set2)


'''


'''
1.列表和元组

列表和元组有很多相似的地方，操作也差不多。不过列表是可变序列，元组为不可变序列。也就是说列表主要用于对象长度不可知的情况下，而元组用于对象长度已知的情况下，而且元组元素一旦创建变就不可修改。 
例如我们在打开一个文本时，并不知道里面有多少行文字，所以用列表来保存。

with open('test.txt', 'r') as f:
    print(f.readlines())
# 结果：
# ['hello world\n', 'hi kyda\n', 'this is my program']
1
1
2
3
4
而我们在储存一个人的信息（名字，年龄，性别，假定只需要这三种信息，所以对象长度为3）的时候，就可以用元组来实现。

id = ('kyda', 19, 'man')
print(id)
# 结果：
# ('kyda', 19, 'man')



'''


#集合可以用来有效去重。
#在海量数据中查找元素时，最好将数据创建为字典，或者是集合

#这是由于字典和集合背后的查找原理是散列（哈希）表。由于散列表在查找元素时的时间复杂度基本是O(1),这使查找时间很短。

#在我的一篇博客专门实验了列表，元组，字典，集合在查找元素时所用的时间：



'''
灵活利用推导来创建
'''

list2 = [x for x in range(1,10)]
print list2
#对于字典来说我们也可以运用双重推导（笛卡尔积）来创建：

liststr = ['name','age','sex']
listint = ['kide',19,'man']


ID = {x:y for x in liststr for y in listint}
print ID

ID = {x: y for x, y in zip(liststr,listint)}
print ID


coordinate = [(x,y) for x in range(10) for y in range(10)]
print coordinate


#枚举

setmyself = {'name','age','sex'}
for str in setmyself:
    print str



for index,temp in enumerate(setmyself):
    print index,temp



liststr = ['name','age','sex']
listint = ['kide',19,'man']

ID = {x:y for x,y in zip(listint,liststr)}
for temp in ID.items():
    print temp