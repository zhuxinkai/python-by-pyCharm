#coding=utf-8
import socket
import struct
import sys
import threading
import re
#import Queue
import requests
import os
from myThread import MyThread





from netaddr import IPNetwork

pkt = b'\x00\x00\x00\xc0\xfeSMB@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00$\x00\x08\x00\x01\x00\x00\x00\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00x\x00\x00\x00\x02\x00\x00\x00\x02\x02\x10\x02"\x02$\x02\x00\x03\x02\x03\x10\x03\x11\x03\x00\x00\x00\x00\x01\x00&\x00\x00\x00\x00\x00\x01\x00 \x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\n\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00'

#subnet = sys.argv[1]
subnet = '10.9.0.0/12'
subnet2 = '10.1.15.0/24'

subnetlist = ('10.233.0.0/21','10.8.24.0/24','10.8.25.0/24','10.8.21.0/24','10.8.23.0/24','10.8.22.0/24','10.8.26.0/24')
subnetlistxinzhou = ('10.1.15.0/24',)





def funcscanner(args):
    #for subnet in subnetlist2:
        for ip in IPNetwork(args):
        #ip = 10.1.15.235
            sock = socket.socket(socket.AF_INET)
            sock.settimeout(1)

            try:
                sock.connect(( str(ip),  445 ))
            except:
                print (ip,"主机不存在")
                sock.close()
                continue

            try:
                sock.send(pkt)
            except:
                sock.close()
                continue
            try:

                nb, = struct.unpack(">I", sock.recv(4))
            except:
                sock.close()
                continue
            res = sock.recv(nb)
            #print (res)
            ok_f = open("vlunthread-xinzhou.txt","a+")
            if res[68:70] != b"\x11\x03" or res[70:72] != b"\x02\x00":
                print(f"{ip} Not vulnerable.")
                ok_f.write(f"{ip} Not vulnerable."+"\n")
            else:
                print(f"{ip} Vulnerable")
                ok_f.write(f"{ip} vulnerable."+"\n")
            ok_f.close()




subnetlist2 = ('10.9.2.1/16', '10.10.0.0/16', '10.11.0.0/16', '10.12.0.0/16', '10.13.0.0/16', '10.14.0.0/16', '10.15.0.0/16','10.16.0.0/16')
funcsn = range(len(subnetlistxinzhou))

def main():

    threads = []
    for i in funcsn:
        #使用过程中的方式。如果使用导入的类方式。比较利于
        t = threading.Thread(target=funcscanner,args=(subnetlistxinzhou[i],))
        #t = MyThread(funcscanner(subnetlistxinzhou[i]),(subnetlistxinzhou[i],),funcscanner().__name__)
        threads.append(t)

    for i in funcsn:
        threads[i].start()


    for i in funcsn:
        threads[i].join()



if __name__ == '__main__':
    main()
