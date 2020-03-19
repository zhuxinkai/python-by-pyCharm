#coding=utf-8
import threading
from time import ctime,sleep

loops = [11,2]

def loop(nloop,nsec):
    print 'start loop',nloop, 'at:',ctime()
    sleep(nsec)
    print 'loop',nloop ,'done at： ',ctime()


def main():
    print 'starting at :', ctime()
    treads = []
    nloops = range(len(loops))

    for i in nloops:

        #Tread 对象
        #对应 target 中函数的参数，其中参数对应的为数组的值。
        t = threading.Thread(target=loop,args=(i,loops[i]))
        # 将Tread 对象放在列表中

        treads.append(t)

    for i in nloops:
        treads[i].start()
# 等待所有线程结束后，或者在提供了超时时间的情况下，达到超时时间。 使用join()比等待锁释放的无限循环更加清晰。
    for i in nloops:
        treads[i].join()

    print 'ALL DONE AT :',ctime()


if __name__ == '__main__':
    main()
