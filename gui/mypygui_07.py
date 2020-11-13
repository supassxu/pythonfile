# encoding=utf-8
""" 一个经典的GUI程序 """
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
        """创建登录界面的组件"""
        self.v = StringVar()
        self.v.set("F")

        self.r1 = Radiobutton(self, text='男性', value='M', variable=self.v)
        self.r2 = Radiobutton(self, text='女性', value='F', variable=self.v)
        self.r1.pack(side='left');self.r2.pack(side='left')

        Button(self,text="确定", command=self.confirm).pack(side='left')

    def confirm(self):
        messagebox.showinfo('测试', '您选择的性别是：' + self.v.get())


if __name__ == '__main__':
    root = Tk()
    root.geometry('400x300+200+300')
    root.title('一个经典的GUI程序类的测试')
    app = Application(master=root)
    root.mainloop()
