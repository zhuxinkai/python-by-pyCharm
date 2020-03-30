import tkinter as tk

windows = tk.Tk()

label = tk.Label(windows,text="Hello word")
label.pack()

button = tk.Button(windows,text="EXIT",command=windows.quit,bg='red',fg='white')
button.pack(fill=tk.X,expand=1)

button2 =tk.Button(windows,text='EXIT2',command=windows.quit,bg='blue',fg='white')
button2.pack()

windows.mainloop()