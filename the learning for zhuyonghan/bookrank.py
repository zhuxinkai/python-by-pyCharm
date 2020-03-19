#coding=utf-8
# 用 atexit.register() 函数来告知脚本何时结束。
from atexit import register
# 使用正则表达式的re.compile()函数，用于匹配Amazon 商品页总图书排名的模式。
from re import compile

from threading import Thread
from time import ctime
# 为访问每个链接
from urllib2 import urlopen as uopen


REGEX = compile('#([\d],)+ in Books ')
AMZN = 'https://www.amazon.com/-/zh/dp/'

ISBNs = {
    '1491946008': 'Core Python Programming',
    '1491957662': 'Python Web Development with Django',
    '1593279280': 'Python Fundamentals',
}



def getRanking(isbn):
    print ("%s%s"%(AMZN,isbn))
    #通过这个方式，形成完整的URL
    page = uopen('%s%s' % (AMZN,isbn))
    data = page.read()
    page.close()
    return REGEX.findall(data)[0]



def _showRanking(isbn):
    print '- %r randed %s ' % (ISBNs[isbn],getRanking(isbn))


def main():
    print 'At', ctime(),'on Amazon...'
    for isbn in ISBNs:
        _showRanking(isbn)


@register
def _atexit():
    print 'ALL DONE at : ', ctime()



if __name__ == '__main__':
    main()

