#coding=utf-8
from atexit import register
from random import randrange
from threading import Thread,Lock,currentThread
from time import sleep,ctime
import random

class CleanOutputSet(set):
    def __str__(self):
        return ', '.join(x for x in self)


lock = Lock
loops = (randrange(2,5) for x in range(randrange(3,7)))
for i in loops:
    print(i)
print (loops)
