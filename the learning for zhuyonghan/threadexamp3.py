#coding=utf-8
from time import ctime,sleep
from myThread import MyThread


def jisuan(x):
    sleep(0.005)
    if x < 2: return 1
    return (jisuan(x-2) + jisuan(x-1))



def jisuan2(x):
    sleep(0.1)
    if x <2: return 1
    return (x * jisuan2(x-1))



def jisuan3(x):
    sleep(0.1)
    if x < 2: return 1
    return (x + jisuan3(x-1))





func2 = [jisuan,jisuan2,jisuan3]
n = 12





def main():
    nfuncs = range(len(func2))
    print '***SINGLE THREAD*****'
    for i in nfuncs:
        print 'starting ', func2[i].__name__,'at: ',ctime()
        print func2[i](n)
        print func2[i].__name__,'finished at :', ctime()



    print 'MUTIL THREAD *****'
    threads = []
    for i in nfuncs:
        t = MyThread(func2[i],(n,),func2[i].__name__)
        threads.append(t)

    for i in nfuncs:
        threads[i].start()


    for i in nfuncs:
        threads[i].join()
        print threads[i].getResult()


    print 'all DONE'







if __name__ == '__main__':
    main()