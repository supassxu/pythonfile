# coding=utf-8

from tkinter import *
from tkinter.colorchooser import *
from tkinter.filedialog import *

# 窗口的宽度和高度
win_width=900
win_height=450
class Application(Frame):

    def __init__(self,master=None):
        super().__init__(master)        # 调用父类构造对象
        self.master = master
        self.bg='black'
        self.x = 0
        self.y = 0
        self.fgcolor = 'green'
        self.lastDraw = 0
        self.startDrawFlag = False
        self.pack()
        self.createWidget()

    def createWidget(self):
        # 创建绘图区
        self.drawPad = Canvas(root,width=win_width,height=win_height-30,bg=self.bg)
        self.drawPad.pack()

        # 创建按钮
        btn_start = Button(root,text='开始',name='start')
        btn_start.pack(side='left',padx='10')
        btn_pen = Button(root, text='画笔', name='pen')
        btn_pen.pack(side='left', padx='10')
        btn_rect = Button(root, text='矩形', name='rect')
        btn_rect.pack(side='left', padx='10')
        btn_clear = Button(root, text='清屏', name='clear')
        btn_clear.pack(side='left', padx='10')
        btn_earsor = Button(root, text='橡皮擦', name='earsor')
        btn_earsor.pack(side='left', padx='10')
        btn_line = Button(root, text='直线', name='line')
        btn_line.pack(side='left', padx='10')
        btn_lineArrow = Button(root, text='箭头直线', name='lineArrow')
        btn_lineArrow.pack(side='left', padx='10')
        btn_color = Button(root, text='颜色', name='color')
        btn_color.pack(side='left', padx='10')

        #事件处理
        btn_pen.bind_class('Button', '<1>', self.eventManager)
        self.drawPad.bind('<ButtonRelease-1>', self.stopDraw)

    def eventManager(self,event):
        name = event.widget.winfo_name()
        print(name)
        if name == 'line':
            self.drawPad.bind('<B1-Motion>', self.myline)
        elif name == 'lineArrow':
            self.drawPad.bind('<B1-Motion>', self.mylineArrow)
        elif name == 'rect':
            self.drawPad.bind('<B1-Motion>', self.myRect)
        elif name == 'earsor':
            self.drawPad.bind('<B1-Motion>', self.myEarsor)
        elif name == 'clear':
            self.drawPad.delete('all')
        elif name == 'pen':
            self.drawPad.bind('<B1-Motion>', self.myPen)
        elif name == 'color':
            s1 = askcolor(color='red', title='选择画笔颜色')
            print(s1)  # s1的值是：((0.0, 255.99609375, 0.0), '#00ff00')
            self.fgcolor = s1[1]
    def myline(self, event):
        self.startDraw(event)
        self.lastDraw = self.drawPad.create_line(self.x, self.y, event.x, event.y, fill=self.fgcolor)

    def mylineArrow(self, event):
        self.startDraw(event)
        self.lastDraw = self.drawPad.create_line(self.x, self.y, event.x, event.y, arrow=LAST, fill=self.fgcolor)

    def myRect(self, event):
        self.startDraw(event)
        self.lastDraw = self.drawPad.create_rectangle(self.x, self.y, event.x, event.y, outline=self.fgcolor)

    def myPen(self, event):
        self.startDraw(event)
        self.drawPad.create_line(self.x, self.y, event.x, event.y, fill=self.fgcolor)
        self.x = event.x
        self.y = event.y

    def myEarsor(self, event):
        self.startDraw(event)
        self.drawPad.create_line(event.x-4, event.y-4, event.x+4, event.y+4, fill=self.bg)
        self.x = event.x
        self.y = event.y

    def startDraw(self,event):
        self.drawPad.delete(self.lastDraw)
        if not self.startDrawFlag:
            self.startDrawFlag = True
            self.x = event.x
            self.y = event.y

    def stopDraw(self, event):
        self.startDrawFlag = False
        self.lastDraw = 0

if __name__ == '__main__':
    root = Tk()
    root.geometry(str(win_width) + 'x' + str(win_height) + '+200+300')
    app = Application(master=root)
    root.mainloop()
