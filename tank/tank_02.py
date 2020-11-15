"""
坦克大战项目的主类
"""

class MainGame():
    def __init__(self):
        pass
    # 开始游戏
    def startGame(self):
        pass

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