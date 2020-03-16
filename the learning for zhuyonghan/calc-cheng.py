#This program is designed for plus calculations.
#!C:\Program Files\Python37
# -*- coding: UTF-8 -*-

import tkinter as tk
root=tk.Tk()
root.geometry=("600x400+%d+%d"%(600,600))
root.title("欢迎使用朱永涵乘法计算器")

entry_plus1=tk.Entry(root)
entry_plus1.grid(row=0,column=0)
entry_plus2=tk.Entry(root)



entry_plus2.grid(row=0,column=2)

varstr=tk.StringVar()
varstr.set("0")
label_plus=tk.Label(root,text="+")
label_plus.grid(row=0,column=1)
label_plus=tk.Label(root,text="=")
label_plus.grid(row=0,column=3)
label_sum=tk.Label(root,textvariable=varstr)
label_sum.grid(row=0,column=4)

def btn_Click():
    summer=int(entry_plus1.get())*int(entry_plus2.get())
    varstr.set(summer)
button_plus1=tk.Button(root,text="求积",command=btn_Click)
button_plus1.grid(row=1,column=3)
root.mainloop()