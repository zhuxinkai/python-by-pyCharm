#coding=utf-8
import threading
from time import ctime



class MyThread(threading.Thread):
#__init__构造器  func 函数，或者功能函数， args 参数 ， name 为执行时的函数名称
    def __init__(self,func,args,name=''):
        threading.Thread.__init__(self)
        self.name=name
        self.args=args
        self.func=func


# 工具类中获取结构的函数（方法），其中self.res 由run 方法赋值。
    def getResult(self):
        return self.res

# 工具类中实际的执行方法
    def run(self):
        print ('starting', self.name,'at:',ctime())
        self.res = self.func(*self.args)

        print (self.name,'finished at :' ,ctime())
