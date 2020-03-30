#coding=utf-8

import tkinter as tk

from tkinter import *

def resize(ev=None):
    label.config(font='Helvetica -%d bold' % scale.get())
windows =tk.Tk()
#指定了窗口的大小，其中 550x350 是字符x而不是乘法符号。
windows.geometry('550x350')




windows.title("this is a test program with tkinter")
label = tk.Label(windows,text="hello world",font='Helvetica -12 bold')
label.pack(fill=Y,expand=1)

#回调resize ，resize 的功能为label的设置，其中label的大小值，通过scale.get()函数获取。

scale = Scale(windows,from_=10,to=100,orient=HORIZONTAL,command=resize)
scale.set(12)
scale.pack(fill=tk.X,expand=1)




button = tk.Button(windows,text="EXIT",command=windows.quit,activeforeground='white',activebackground='red')
button.pack()
#注意最后的 mainloop 关系到整个程序能否循环的执行下去。
windows.mainloop()



