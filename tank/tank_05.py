"""
新增功能：
    左上角文字绘制：
    左上角输出：敌方坦克的数量
"""
import pygame
Screen_Width = 700
Screen_Height = 500
Bg_Color = pygame.Color(0,0,0)
Text_Color = pygame.Color(255,0,0)
class MainGame():
    window=None
    def __init__(self):
        pass
    # 开始游戏
    def startGame(self):
        # 加载主窗口
        # 初始化窗口
        pygame.display.init()
        # 设置窗口的大小及显示
        self.window = pygame.display.set_mode([Screen_Width, Screen_Height])
        # 设置窗口的标题
        pygame.display.set_caption('坦克大战1.01')
        while True:
            # 给窗口设置填充色
            self.window.fill(Bg_Color)
            self.getEvent()
            # 绘制左上角文字
            self.window.blit(self.getTextSuface('敌方剩余坦克数量%d'%6),(10,10))
            pygame.display.update()
    # 结束游戏
    def endGame(self):
        print('谢谢使用，欢迎下次使用！')
        exit()

    # 左上角文字的绘制
    def getTextSuface(self,text):
        # 初始化字体模块
        pygame.font.init()
        # 查看所有的字体
        #print(pygame.font.get_fonts())
        # 获取字体对象
        font = pygame.font.SysFont('kaiti', 18)
        textSurface = font.render(text,True,Text_Color)
        return textSurface

    def getEvent(self):
        # 获取所有事件
        eventList = pygame.event.get()
        # 遍历事件
        for event in eventList:
            # 判断按下的键是关闭还是键盘按下
            # 如果按下的是退出
            if event.type == pygame.QUIT:
                self.endGame()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print('按下左键，坦克向左移动')
                elif event.key == pygame.K_RIGHT:
                    print('按下左键，坦克向右移动')
                elif event.key == pygame.K_UP:
                    print('按下左键，坦克向上移动')
                elif event.key == pygame.K_DOWN:
                    print('按下左键，坦克向下移动')
                elif event.key == pygame.K_w:
                    print('按下左键，坦克向上移动')
                elif event.key == pygame.K_a:
                    print('按下左键，坦克向左移动')
                elif event.key == pygame.K_s:
                    print('按下左键，坦克向下移动')
                elif event.key == pygame.K_d:
                    print('按下左键，坦克向右移动')
            else:
                print('其他内容后续支持！')
class Tank():
    def __init__(self):
        pass
    # 移动
    def move(self):
        pass
    # 射击
    def shot(self):
        pass
    # 展示坦克的方法
    def displayTank(self):
        pass

class MyTank(Tank):
    def __init__(self):
        pass

class EnemyTank(Tank):
    def __init__(self):
        pass

class Bullet():
    def __init__(self):
        pass
    # 移动
    def move(self):
        pass
    def displayBullet(self):
        pass

class Wall():
    def __init__(self):
        pass
    # 展示墙壁的方法
    def displayWall(self):
        pass

class Explode():
    def __init__(self):
        pass
    # 展示爆炸效果的方法
    def displayExplode(self):
        pass

class Music():
    def __init__(self):
        pass
    #播放音乐
    def playMusic(self):
        pass

if __name__ == '__main__':
    MainGame().startGame()