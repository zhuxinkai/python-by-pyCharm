#utfcoding=utf-8
# 导入time.ctime() 和 socket 模块的所有属性

from socket import *
from time import ctime


HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST,PORT)



# 面向连接的通信提供序列化， 可靠的，和不重复的数据交付，而没有记录边界。

tcpSerSock =  socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)


#低廉，无需，不可靠的数据报服务
#udpsocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    print 'wiating for connection......'
    tcpClinetSocket,addr = tcpSerSock.accept()
    print'....connected from :',addr

    while True:
        data = tcpClinetSocket.recv(BUFSIZE)
        print data
        if not data:
            break
        tcpClinetSocket.send('[%s] %s'%(ctime(),data))
    tcpClinetSocket.close()


    tcpSerSock.close()


