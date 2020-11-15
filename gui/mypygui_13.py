# coding=utf-8

from tkinter import *
from tkinter.colorchooser import *

root = Tk();
root.geometry('500x150')


def test1():
    s1 = askcolor(color='green', title='选择背景色')
    print(s1)
    # s1的值是：((0.0, 255.99609375, 0.0), '#00ff00')
    root.config(bg=s1[1])


Button(root, text='选择背景色', command=test1).pack()

root.mainloop()
