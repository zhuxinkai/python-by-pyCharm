import thread
from time import ctime,sleep

def loop0():
    print 'loop 0 start at ',ctime()
    sleep(4)
    print 'loop 0 end at ',ctime()



def loop1():
    print 'loop 1 start at ',ctime()
    sleep(2)
    print 'loop 1 end at ',ctime()



def main():
    print 'start at ',ctime()
    loop0()
    loop1()
    print 'end at ',ctime()


if __name__ == '__main__':
   main()

