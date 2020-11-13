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
        self.label01 = Label(self, text='label程序员', width=10, height=2, bg='black', fg='white')
        self.label01.pack()
        self.label02 = Label(self, text='label2老师', width=10, height=2, bg='blue', fg='red',font='楷体')
        self.label02.pack()

        # 显示图像
        global photo
        photo = PhotoImage(file='a.gif')
        self.label03 = Label(self, image=photo)
        self.label03.pack()

        self.label04 = Label(self, text='label程序员\nlabel1李老师\n老高被媳妇儿\n欢迎来到GUI世界',
                             borderwidth=5, relief='groove', justify='right')
        self.label04.pack()

        # 创建一个退出按钮
        self.btnQuit = Button(self, text='退出', command=root.destroy)
        self.btnQuit.pack()

    def songhua(self):
        messagebox.showinfo('Message', '送你一朵大红花')
        #print('送你999朵玫瑰花！')



root = Tk()
root.geometry('400x800+200+300')
root.title('一个经典的GUI程序类的测试')
app = Application(master=root)

root.mainloop()