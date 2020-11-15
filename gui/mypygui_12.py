# coding=utf-8
# 测试键盘和鼠标事件

from tkinter import *

root = Tk();root.geometry('500x150')


def test1(value):
    print('滑块的值：',value)
    newFont = ('楷体',value)
    a.config(font=newFont)

s1 =Scale(root,from_=10,to=50,length=200,tickinterval=5,orient=HORIZONTAL,command=test1)
s1.pack()

a = Label(root,text='测试工程师',width=10,height=1,bg='black',fg='white')
a.pack()


root.mainloop()