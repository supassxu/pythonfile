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
        self.t1 = Text(root, width=40,height=12,bg='white')
        # 宽度20个字母（10个汉字）,高度一个行高
        self.t1.pack()

        self.t1.insert(1.0,"0123456789\nabcdefghijklmnopqrstuvwxyz")
        self.t1.insert(2.3,"锄禾日当午，汗滴禾下土。谁知盘中餐，粒粒皆辛苦\n")
        Button(self,text="重复插入文本",command=self.insertText()).pack(side='left')

        # 创建一个登录按钮
        # self.btn01 = Button(self, text='登录', command=self.login)
        # self.btn01.pack()

    def insertText(self):
        self.t1.insert(INSERT,'SupassXu')
        self.t1.insert(END,'[xcc]')
        #print("密码：" + self.entry02.get())
        #messagebox.showinfo('登陆成功', '登陆成功，欢迎开始学习！')


if __name__ == '__main__':
    root = Tk()
    root.geometry('400x300+200+300')
    root.title('一个经典的GUI程序类的测试')
    app = Application(master=root)
    root.mainloop()
