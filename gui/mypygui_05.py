# encoding=utf-8
""" 一个经典的GUI程序 """

from tkinter import *
from tkinter import messagebox


class Application(Frame):
    """一个经典的GUI程序的类的写法"""

    def __init__(self,master=None):
        super().__init__(master)        # 调用父类构造对象
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        """创建登录界面的组件"""
        self.label01 = Label(self, text="用户名")
        self.label01.pack()

        # StringVar变量绑定到指定的组件。
        # StringVar变量的值发生变化，组件内容也发生变化。
        # 组件内容发生变化，StringVar变量的值也发生变化。
        v1 = StringVar()
        self.entry01 = Entry(self, textvariable=v1)
        self.entry01.pack()
        v1.set('admin')
        print(v1.get());print(self.entry01.get())

        self.label02 = Label(self, text="密码")
        self.label02.pack()

        v2 = StringVar()
        self.entry02 = Entry(self, textvariable=v2, show='*')
        self.entry02.pack()
        v2.set('root@123')
        print(v2.get());
        print(self.entry02.get())

        # 创建一个登录按钮
        self.btn01 = Button(self, text='登录', command=self.login)
        self.btn01.pack()

    def login(self):
        print("用户名：" + self.entry01.get())
        print("密码：" + self.entry02.get())
        messagebox.showinfo('登陆成功', '登陆成功，欢迎开始学习！')


if __name__ == '__main__':
    root = Tk()
    root.geometry('400x300+200+300')
    root.title('一个经典的GUI程序类的测试')
    app = Application(master=root)
    root.mainloop()