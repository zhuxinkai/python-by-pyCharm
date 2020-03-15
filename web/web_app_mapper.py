# coding：<encoding name> ： # coding: utf-8
import Queue
import threading
import os
import urllib2

threads = 10

target = "www.wordpress.com"
directory = "C:\inetpub\wordpress"
filters = [".jgp",".gif",".png",".css"]
# os.getcwd 获取当前路径
#retval = os.getcwd()
print "当前的工作目录是 %s" % os.getcwd()
#os.chdir change dir 的缩写，os.chdir 改变当前路径。
os.chdir(directory)
print "更改后的工作目录是 %s " % os.getcwd()

#队列
web_paths = Queue.Queue()
#os.walk 用于查询当前路径下的路径，目录，及文件名。其中的参数“.”，表示

for r,d,f in os.walk("."):
    #print f
    for files in f:
        #print files
       # print os.path.splitext(files)[1]
        remote_path = "%s/%s" % (r,files)
        #print remote_path
        if remote_path.startswith("."):
            remote_path = remote_path[1:]
            #print remote_path
        if os.path.splitext(files)[1] not in filters:
            web_paths.put(remote_path)




def test_remote():
    while not web_paths.empty():
        path = web_paths.get()
        #print path
        url ="%s%s" % (target,path)
        print url
        request = urllib2.Request(url)
        try:
            response = urllib2.urlopen(request)
            content =response.read()
            print path
            print "[%d] => %s" % (response.code,path)
            response.close()
        except urllib2.HTTPError as error:
            print "Failed %s" % error.code
            pass


for i in range(threads):
    print "Spawning thread : %d" % i
    t = threading.Thread(target=test_remote)
    t.start()