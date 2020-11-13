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
        """创建登录界面的组件"""
        self.canvas = Canvas(self, width=300, height=200, bg='green')
        self.canvas.pack()

        global photo
        photo = PhotoImage(file='a.gif')
        self.canvas.create_image(150, 170, image=photo)

        self.canvas.create_line(10, 10, 20, 30, 40, 50)
        self.canvas.create_rectangle(50, 50, 100, 100)
        self.canvas.create_oval(50, 50, 100, 100)

        Button(self,text="确定", command=self.draw50Recg).pack(side='left')

    def draw50Recg(self):
        for i in range(0,10):
            x1 = random.randrange(int(self.canvas['width'])/2)
            y1 = random.randrange(int(self.canvas['height'])/2)
            x2 = x1 + random.randrange(int(self.canvas['width'])/2)
            y2 = y1 + random.randrange(int(self.canvas['height'])/2)
            self.canvas.create_rectangle(x1, y1, x2, y2)

if __name__ == '__main__':
    root = Tk()
    root.geometry('400x300+200+300')
    root.title('一个经典的GUI程序类的测试')
    app = Application(master=root)
    root.mainloop()
