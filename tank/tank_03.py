"""
新增功能：
    加载主窗口
    pygame官方网址：www.pygame.org
"""
import pygame
Screen_Width = 700
Screen_Height = 500
Bg_Color = pygame.Color(0,0,0)
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
            pygame.display.update()
    # 结束游戏
    def endGame(self):
        pass

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