#coding= utf-8
from time import ctime,sleep
import threading

loops = [4,2]

# 添加 TreadFunc 类，我们使得这个类更加通用（类似于JAVA接口），让这个类保存了函数的参数，函数自身以及函数名的字符串。
#构造函数__init__ 用来设定上述这些值。 类似于java 的构造器。

class TreadFunc(object):
    def __init__(self,func,args,name = ''):
        self.name = name
        self.func = func
        self.args = args

# 调用 TreadFunc 对象，此时会调用__call__()这个特殊方法。
    def __call__(self):
        self.func(*self.args)




def loop(nloop,nsleep):
    print nloop,'start at ',ctime()
    sleep(nsleep)
    print nloop, 'stop at ', ctime()



def main():
    print 'starting at: ', ctime()
    treads = []
    nloop = range(len(loops))

    for i in nloop:
        t = threading.Thread(target=TreadFunc(loop,(i,loops[i]),loop.__name__))
        treads.append(t)


    for i in nloop:
        treads[i].start()

    for i in nloop:
        treads[i].join()


if __name__ == '__main__':
    main()




