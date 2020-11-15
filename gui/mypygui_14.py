# coding=utf-8

from tkinter import *
from tkinter.filedialog import *

root = Tk()
root.geometry('500x150')


def test1():
    with askopenfile(title='上传文件', initialdir='E:\\',
                         filetypes=[('记事本', '.txt')]) as f:
        show['text'] = f.read()


Button(root, text='选择读取的文本文件', command=test1).pack()

show = Label(root, width=40, height=3, bg='blue')
show.pack()

root.mainloop()
