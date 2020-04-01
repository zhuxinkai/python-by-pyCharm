#encoding=utf-8


'''3.打印OptionMenu的值'''
# -*- coding: utf-8 -*-
from tkinter import *

root = Tk()
v = StringVar(root)
v.set('Tkinter')


def printOption(event):
    print(v.get())


# 创建一个OptionMenu控件
om = OptionMenu(root,
                v,
                'Python',
                'PHP',
                'CPP',
                'C',
                'Java',
                'JavaScript',
                'VBScript'
                )
om.bind('<Button-1>', printOption)
om.pack()

root.mainloop()
# 每次点击OptionMenu程序打印出上次选中的项值