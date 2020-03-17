#coding= utf-8
from twisted.internet import protocol,reactor
from time import ctime


PORT = 21568

class TSServProtocol(protocl.Protocol):
    