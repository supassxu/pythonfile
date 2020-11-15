"""
新增功能：
    优化：1、如果子弹碰到墙壁，就让子弹消失
         2、最多可以发射3颗子弹，不能一直发送
"""
import pygame, time, random

Screen_Width = 700
Screen_Height = 500
Bg_Color = pygame.Color(0,0,0)
Text_Color = pygame.Color(255,0,0)
class MainGame():
    window=None
    my_tank=None
    # 存储敌方坦克的列表
    enemyTankList = []
    # 定义敌方坦克的数量
    enemyTankNum = 5
    # 存储我方坦克子弹的列表
    myBulletList = []
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
        #初始化敌方坦克
        self.createEnemmyTank()

        # 设置窗口的标题
        pygame.display.set_caption('坦克大战1.01')
        while True:
            # 给窗口设置填充色
            MainGame.window.fill(Bg_Color)
            self.getEvent()
            # 绘制左上角文字
            MainGame.window.blit(self.getTextSuface('敌方剩余坦克数量%d'%len(self.enemyTankList)),(10,10))
            # 调用坦克显示的方法
            MainGame.my_tank.displayTank()
            # 循环遍历展示敌方坦克，展示敌方坦克
            self.blitEnemyTank()
            # 循环遍历我方坦克的子弹
            self.blitMyBullet()
            if not MainGame.my_tank.stop:
                MainGame.my_tank.move()
            #if not MainGame.myBullet.stop:
                #MainGame.myBullet.move()
            time.sleep(0.05)
            pygame.display.update()

    # 初始化敌方坦克
    def createEnemmyTank(self):
        top = 50
        # 循环生成敌方坦克
        for i in range(MainGame.enemyTankNum):
            left = random.randint(0, 600)
            speed = random.randint(1, 4)
            enemy = EnemyTank(left, top, speed)
            MainGame.enemyTankList.append(enemy)
    # 循环遍历展示敌方坦克，展示敌方坦克
    def blitEnemyTank(self):
        for enemyTank in MainGame.enemyTankList:
            enemyTank.displayTank()
            enemyTank.randMove()
    # 循环遍历展示敌方坦克，展示敌方坦克
    def blitMyBullet(self):
        for myBullet in MainGame.myBulletList:
            # 判断当前的子弹是否是或者的状态，如果是则进行显示及移动，
            if myBullet.live:
                myBullet.displayBullet()
                # 调用子弹的移动方法
                myBullet.move()
            else:
                MainGame.myBulletList.remove(myBullet)
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
                    # 修改坦克的开关状态
                    MainGame.my_tank.stop = False
                    #MainGame.my_tank.move()
                    print('按下左键，坦克向左移动')
                elif event.key == pygame.K_RIGHT:
                    # 获取坦克方向
                    MainGame.my_tank.direction = 'R'
                    # 修改坦克的开关状态
                    MainGame.my_tank.stop = False
                    #MainGame.my_tank.move()
                    print('按下左键，坦克向右移动')
                elif event.key == pygame.K_UP:
                    # 获取坦克方向
                    MainGame.my_tank.direction = 'U'
                    # 修改坦克的开关状态
                    MainGame.my_tank.stop = False
                    #MainGame.my_tank.move()
                    print('按下左键，坦克向上移动')
                elif event.key == pygame.K_DOWN:
                    # 获取坦克方向
                    MainGame.my_tank.direction = 'D'
                    # 修改坦克的开关状态
                    MainGame.my_tank.stop = False
                    #MainGame.my_tank.move()
                    print('按下左键，坦克向下移动')
                elif event.key == pygame.K_SPACE:
                    # 如果我方当前子弹列表的大小小于等于3时，才可以创建
                    if len(MainGame.myBulletList) < 3:
                        print('我方坦克发射子弹')
                        myBullet = Bullet(MainGame.my_tank)
                        MainGame.myBulletList.append(myBullet)
                    """elif event.key == pygame.K_a:
                    print('按下左键，坦克向左移动')
                elif event.key == pygame.K_s:
                    print('按下左键，坦克向下移动')
                elif event.key == pygame.K_d:
                    print('按下左键，坦克向右移动')"""
            #else:
                #print('其他内容后续支持！')

            # 松开方向键，坦克停止移动，修改移动开关
            if event.type == pygame.KEYUP:
                # 判断宋凯的键是上、下、坐、右键才停止坦克移动
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    MainGame.my_tank.stop = True
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
        self.speed = 3
        self.stop = True


    # 移动
    def move(self):
        # 判断坦克移动的方向，来进行移动
        if self.direction == 'L':
            if self.rect.left > 0:
                self.rect.left -= self.speed
            else:
                pass
        elif self.direction == 'U':
            if self.rect.top > 0:
                self.rect.top -= self.speed
            else:
                pass
        elif self.direction == 'R':
            if self.rect.left + self.rect.height < Screen_Width:
                self.rect.left += self.speed
            else:
                pass
        elif self.direction == 'D':
            if self.rect.top + self.rect.width < Screen_Height:
                self.rect.top += self.speed
            else:
                pass
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
    def __init__(self, left, top, speed):
        # 加载图片集
        self.images = {
            'U': pygame.image.load('img/E_tank_U.jpg'),
            'D': pygame.image.load('img/E_tank_D.jpg'),
            'L': pygame.image.load('img/E_tank_L.jpg'),
            'R': pygame.image.load('img/E_tank_R.jpg'),
        }
        # 随机生成敌方坦克的方向
        self.direction = self.randDirection()
        # 根据当前图片的方向获取图片
        self.image = self.images[self.direction]
        # 根据图片获取区域
        self.rect = self.image.get_rect()
        # 设置区域的left和top
        self.rect.left = left
        self.rect.top = top
        # 速度，决定移动的快慢
        self.speed = speed
        # 移动开关键
        self.flag = True
        # 步数变量
        self.step = 60

    # 随机生成敌方坦克的方向
    def randDirection(self):
        i = random.randint(1, 4)
        if i == 1:
            return 'U'
        elif i == 2:
            return 'D'
        elif i == 3:
            return 'L'
        elif i == 4:
            return 'R'
    # 敌方坦克随机移动的方法
    def randMove(self):
        if self.step <= 0:
            # 修改方向
            self.direction = self.randDirection()
            self.step = 60
        else:
            self.move()
            self.step -= self.speed

class Bullet():
    def __init__(self, tank):
        # 加载子弹图片
        self.image = pygame.image.load('img/buttle.jpg')
        # 坦克的方向决定了子弹的方向
        self.direction = tank.direction
        # 获取区域
        self.rect = self.image.get_rect()
        # 子弹的left和top与方向有关
        if self.direction == 'U':
            self.rect.left = tank.rect.left + tank.rect.width/2 - self.rect.width/2
            self.rect.top = tank.rect.top - self.rect.height
        elif self.direction == 'D':
            self.rect.left = tank.rect.left + tank.rect.width / 2 - self.rect.width / 2
            self.rect.top = tank.rect.top + tank.rect.height
        elif self.direction == 'L':
            self.rect.left = tank.rect.left - self.rect.width
            self.rect.top = tank.rect.top + tank.rect.height / 2 - self.rect.width/2
        elif self.direction == 'R':
            self.rect.left = tank.rect.left + tank.rect.width
            self.rect.top = tank.rect.top + tank.rect.height / 2 - self.rect.width/2

        # 子弹的速度
        self.speed = 6
        # 子弹的状态，是否碰到墙壁，如果碰到墙壁，修改此状态
        self.live = True
    # 移动
    def move(self):
        if self.direction == 'U':
            if self.rect.top > 0:
                self.rect.top -= self.speed
            else:
                self.live = False
        elif self.direction == 'D':
            if self.rect.top +self.rect.height < Screen_Height:
                self.rect.top += self.speed
            else:
                self.live = False
        elif self.direction == 'L':
            if self.rect.left > 0:
                self.rect.left -= self.speed
            else:
                self.live = False
        elif self.direction == 'R':
            if self.rect.left +self.rect.width < Screen_Width:
                self.rect.left += self.speed
            else:
                self.live = False
    # 展示子弹的方法
    def displayBullet(self):
        # 将图片surface加载到窗口
        MainGame.window.blit(self.image, self.rect)
        # 否则进行删除

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