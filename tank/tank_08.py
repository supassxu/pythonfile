"""
新增功能：
    优化我方坦克移动的方法
"""
import pygame
Screen_Width = 700
Screen_Height = 500
Bg_Color = pygame.Color(0,0,0)
Text_Color = pygame.Color(255,0,0)
class MainGame():
    window=None
    my_tank=None
    def __init__(self):
        pass
    # 开始游戏
    def startGame(self):
        # 加载主窗口
        # 初始化窗口
        pygame.display.init()
        # 设置窗口的大小及显示
        MainGame.window = pygame.display.set_mode([Screen_Width, Screen_Height])
        # 初始化我方坦克
        MainGame.my_tank = Tank(350, 250)
        # 设置窗口的标题
        pygame.display.set_caption('坦克大战1.01')
        while True:
            # 给窗口设置填充色
            MainGame.window.fill(Bg_Color)
            self.getEvent()
            # 绘制左上角文字
            MainGame.window.blit(self.getTextSuface('敌方剩余坦克数量%d'%6),(10,10))
            # 调用坦克显示的方法
            MainGame.my_tank.displayTank()
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
                    # 获取坦克方向
                    MainGame.my_tank.direction = 'L'
                    MainGame.my_tank.move()
                    print('按下左键，坦克向左移动')
                elif event.key == pygame.K_RIGHT:
                    # 获取坦克方向
                    MainGame.my_tank.direction = 'R'
                    MainGame.my_tank.move()
                    print('按下左键，坦克向右移动')
                elif event.key == pygame.K_UP:
                    # 获取坦克方向
                    MainGame.my_tank.direction = 'U'
                    MainGame.my_tank.move()
                    print('按下左键，坦克向上移动')
                elif event.key == pygame.K_DOWN:
                    # 获取坦克方向
                    MainGame.my_tank.direction = 'D'
                    MainGame.my_tank.move()
                    print('按下左键，坦克向下移动')
                """elif event.key == pygame.K_w:
                    print('按下左键，坦克向上移动')
                elif event.key == pygame.K_a:
                    print('按下左键，坦克向左移动')
                elif event.key == pygame.K_s:
                    print('按下左键，坦克向下移动')
                elif event.key == pygame.K_d:
                    print('按下左键，坦克向右移动')"""
            else:
                print('其他内容后续支持！')
class Tank():
    # 添加距离左边left，距离上边top
    def __init__(self, left, top):
        # 保存加载的图片
        self.images = {
            'U':pygame.image.load('img/tank_U.jpg'),
            'D': pygame.image.load('img/tank_D.jpg'),
            'L': pygame.image.load('img/tank_L.jpg'),
            'R': pygame.image.load('img/tank_R.jpg'),
        }
        # 方向
        self.direction = 'U'
        #根据当前图片的方向获取图片
        self.image = self.images[self.direction]
        #根据图片获取区域
        self.rect = self.image.get_rect()
        # 设置区域的left和top
        self.rect.left = left
        self.rect.top = top
        #速度，决定移动的快慢
        self.speed = 10



    # 移动
    def move(self):
        # 判断坦克移动的方向，来进行移动
        if self.direction == 'L':
            if self.rect.left > 0:
                self.rect.left -= self.speed
        elif self.direction == 'U':
            if self.rect.top > 0:
                self.rect.top -= self.speed
        elif self.direction == 'R':
            if self.rect.left + self.rect.height < Screen_Width:
                self.rect.left += self.speed
        elif self.direction == 'D':
            if self.rect.top + self.rect.width < Screen_Height:
                self.rect.top += self.speed
    # 射击
    def shot(self):
        pass
    # 展示坦克的方法
    def displayTank(self):
        # 获取展示的对象
        self.image = self.images[self.direction]
        # 调用blit方法展示
        MainGame.window.blit(self.image, self.rect)
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