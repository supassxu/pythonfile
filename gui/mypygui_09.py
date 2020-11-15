# encoding=utf-8
""" 一个经典的GUI程序 """
import random
from tkinter import *
from tkinter import messagebox


class Application(Frame):
    """一个经典的GUI程序的类的写法"""

    def __init__(self, master=None):
        super().__init__(master)  # 调用父类构造对象
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        """通过grid布局实现计算器的界面"""
        btnText = (('MC','M+','M-','MR'),
                   ('C','±','/','×'),
                   (7,8,9,'-'),
                   (4,5,6,'+'),
                   (1,2,3,'='),
                   (0,'.'))
        Entry(self).grid(row=0,column=0,columnspan=4,pady=10)
        for rindex,r in enumerate(btnText):
            for cindex,c in enumerate(r):
                if c == '=':
                    Button(self, text=c, width=2). \
                        grid(row=rindex + 1, column=cindex, rowspan=2, sticky=NSEW)
                elif c == 0:
                    Button(self, text=c, width=2). \
                        grid(row=rindex + 1, column=cindex, columnspan=2, sticky=NSEW)
                elif c== '.':
                    Button(self, text=c, width=2). \
                        grid(row=rindex + 1, column=cindex+1, sticky=NSEW)
                else:
                    Button(self,text=c,width=2).\
                    grid(row=rindex+1,column=cindex,sticky=NSEW)

    #def draw50Recg(self):


if __name__ == '__main__':
    root = Tk()
    root.geometry('220x220+200+300')
    root.title('计算器')
    app = Application(master=root)
    root.mainloop()
