#coding=utf-8
from SocketServer import (TCPServer as tcp , StreamRequestHandler as SRH)
from time import ctime

HOST = ''
PORT = 23745
ADDR = (HOST,PORT)


class MyRequestHandler(SRH):
    def handle(self):
        print '..........connected from :',self.client_address
        self.wfile.write('[%s] %s' % (ctime(),self.rfile.readline()))


tcpServ = tcp(ADDR, MyRequestHandler)
print 'waitring for connection .....'
tcpServ.serve_forever()