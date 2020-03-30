import tkinter as tk

windows = tk.Tk()

button = tk.Button(windows,text="Hello word",command=windows.quit)
button.pack()

windows.mainloop()