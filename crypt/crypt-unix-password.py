#coding=utf-8
#AES-demo
"""
    @author: zhuxinkai

    @file: python_AES.py

    @time: 2020/03/31

    @desc: 图形化常用的加密方式 AES ,MD5, RSA ,DES , 3DES ,
"""
from tkinter import *

from Crypto.Cipher import AES
import base64
import hashlib
from binascii import b2a_hex,a2b_hex


m = hashlib.new("md5")
m.update("zxk".encode("utf-8"))
print(m.hexdigest())

print(base64.b64encode(b"123456"))



def MD5encode():
    m = hashlib.md5()
#此处的 get(),如果不采用1.end 会导致将末尾的换行符加入了计算，导致结果不一致情况。 1.end 表示为第一行的结尾。
    md5front = publicKeyText.get("0.0", "1.end").encode(encoding="utf-8")
    m.update(md5front)
    privateKeyText.delete(0.0, END)
    privateKeyText.insert(END,m.hexdigest())



def Base64encode():
    base64result = base64.b64encode(base64frontText.get("0.0", "1.end").encode(encoding="utf-8"))
    base64backText.delete(0.0,END)
    base64backText.insert(END,base64result)

def Base64decode():
    base64result = base64.b64decode(base64backText.get("0.0", "1.end").encode(encoding="utf-8"))
    base64frontText.delete(0.0,END)
    base64frontText.insert(END,base64result)





def AesEncode():


    # 秘钥,此处需要将字符串转为字节
    aesfornt = aesfrontText.get("0.0","1.end").encode(encoding="utf-8")
    key = cipherText.get("0.0","1.end").encode(encoding="utf-8")




    def add_to_16(s):
        while len(s) % 16 != 0:
            #print(type(s))

            s += b'\0'
        return s  # 返回bytes



    # AES的区块长度固定为 128比特，密钥长度可以是128，192或256比特。   密钥长度必须为16、24或32位，分别对应AES-128、AES-192和AES-256
    aes = AES.new(add_to_16(key), AES.MODE_ECB)  # 初始化加密器，本例采用ECB加密模式
    encrypted_text = str(base64.encodebytes(aes.encrypt(add_to_16(aesfornt))), encoding='utf8').replace('\n', '')





    aesbackText.delete(0.0, END)
    aesbackText.insert(END, encrypted_text)


#AES解密函数


def AesDecode():


    # 秘钥,此处需要将字符串转为字节
    encrypted_text = aesbackText.get("0.0","1.end").encode(encoding="utf-8")
    key = cipherText.get("0.0","1.end").encode(encoding="utf-8")




    def add_to_16(s):
        while len(s) % 16 != 0:
            #print(type(s))

            s += b'\0'
        return s  # 返回bytes



    # AES的区块长度固定为 128比特，密钥长度可以是128，192或256比特。   密钥长度必须为16、24或32位，分别对应AES-128、AES-192和AES-256
    aes = AES.new(add_to_16(key), AES.MODE_ECB)  # 初始化加密器，本例采用ECB加密模式


    #decrypted_text = str(aes.decrypt(base64.b64decode(encrypted_text).rstrip(b'\0').encode("utf-8")))

    decrypted_text = str(aes.decrypt(base64.decodebytes(bytes(encrypted_text))).rstrip(b'\0').decode("utf8"))  # 解密

    aesfrontText.delete(0.0, END)
    aesfrontText.insert(END, decrypted_text)





'''
    # 此处是为了验证是否能将字节转为字符串后，进行解密成功
    # 实际上a 就是 encrypted_text ，也就是加密后的内容
    a = b'\xb9K\xe8_.q\x1c!\x9f\xa2\xc8\x06\xf5\xc1\xd07'
    # 用aes对象进行解密，将字节类型转为str类型，错误编码忽略不计
    de = str(aes.decrypt(a), encoding='utf-8', errors="ignore")
    # 获取str从0开始到文本内容的字符串长度。
    print(de[:len(text)])
'''

window = Tk()
window.title("各种加密算法测试软件")

frame = Frame(window)
frame.pack()

label = Label(frame, text = "MD5加密前：")
label.grid(row = 1, column = 1,columnspan= 4)

publicKeyText = Text(frame,width=50,height=2)
publicKeyText.grid(row = 2, column = 1,columnspan = 4)

label = Label(frame, text = "MD5加密后：")
label.grid(row = 3, column = 1,columnspan= 4)

privateKeyText = Text(frame,width=50,height=2)
privateKeyText.grid(row = 4, column = 1,columnspan = 4)

btGenerateKey = Button(frame, text = "md5加密",command=MD5encode,bg='blue',fg='white')
btGenerateKey.grid(row = 5, column = 1,columnspan = 4)


# row 为行数， column 为列数， 你同样可以指定控件跨越一个或者多个网格。columnspan选项可以指定控件跨越多列显示，
# 而rowspan选项同样可以指定控件跨越多行显示。

labelbase64 = Label(frame, text = "BASE64编码前：")
labelbase64.grid(row = 1, column = 8,columnspan=10 )

base64frontText = Text(frame,width=50,height=2)
base64frontText.grid(row = 2, column = 8,columnspan = 10)

labelbase64 = Label(frame, text = "BASE64编码后：")
labelbase64.grid(row = 3, column = 8,columnspan= 15)

base64backText = Text(frame,width=50,height=2)
base64backText.grid(row = 4, column = 8,columnspan = 10)

base64GenerateKey = Button(frame, text = "BASE64编码",bg='red',fg='white',command=Base64encode)
base64GenerateKey.grid(row = 5, column = 4,columnspan = 15)

base642GenerateKey = Button(frame, text = "BASE64解码",bg='red',fg='white',command=Base64decode)
base642GenerateKey.grid(row = 5, column = 13,columnspan = 15)








labelaes = Label(frame, text = "AES加密前：")
labelaes.grid(row = 6, column = 1,columnspan=4 )

aesfrontText = Text(frame,width=50,height=2)
aesfrontText.grid(row = 7, column = 1,columnspan = 4)

labelaes = Label(frame, text = "AES加密密钥：")
labelaes.grid(row = 8 ,column = 1,columnspan= 4)

cipherText = Text(frame,width=50,height=2)
cipherText.grid(row = 9, column = 1,columnspan = 4)

labelaes = Label(frame, text = "AES加密后：")
labelaes.grid(row = 10,column = 1,columnspan= 4)

aesbackText = Text(frame,width=50,height=2)
aesbackText.grid(row = 11, column = 1,columnspan = 4)

aesGenerateKey = Button(frame, text = "AES加密",bg='yellow',fg='red',command=AesEncode)
aesGenerateKey.grid(row = 12, column = 1,columnspan = 2)

aesGenerateKey2 = Button(frame, text = "AES解密",bg='yellow',fg='red',command=AesDecode)
aesGenerateKey2.grid(row = 12, column = 3,columnspan = 4)





'''
btEncryptionByPublickey = Button(frame, text = "公钥加密",#command=EncryptionByPublickey)
btEncryptionByPublickey.grid(row = 8, column = 1,pady = 10)

btDeryptionByPublickey = Button(frame, text = "公钥解密",#command=DeryptionByPublickey)
btDeryptionByPublickey.grid(row = 8, column = 2)

btEncryptionByPrivatekey = Button(frame, text = "私钥加密",#command=EncryptionByPrivatekey)
btEncryptionByPrivatekey.grid(row = 8, column = 3)

btDecryptionByPrivatekey = Button(frame, text = "私钥解密",#command=DecryptionByPrivatekey)
btDecryptionByPrivatekey.grid(row = 8, column = 4)
'''


print("欢迎使用本软件……")
#GenerateKey();
mainloop()

print("欢迎再次使用本软件……")