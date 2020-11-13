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
        """创建组件"""
        self.bton01 = Button(self)
        self.bton01['text'] = '欢迎来到gui世界！'
        self.bton01.pack()
        self.bton01['command'] =self.songhua

        # 创建一个退出按钮
        self.btnQuit = Button(self, text='退出', command=root.destroy)
        self.btnQuit.pack()

    def songhua(self):
        messagebox.showinfo('Message', '送你一朵大红花')
        #print('送你999朵玫瑰花！')



root = Tk()
root.geometry('400x300+200+300')
root.title('一个经典的GUI程序类的测试')
app = Application(master=root)

root.mainloop()