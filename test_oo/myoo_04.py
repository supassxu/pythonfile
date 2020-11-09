from copy import deepcopy, copy


class Man:
    def eat(self):
        print('饿了，吃饭了！')

class Chinese(Man):
    def eat(self):
        print('使用筷子吃饭！')

class English(Man):
    def eat(self):
        print('使用刀叉吃饭！')

class Indian(Man):
    def eat(self):
        print('使用手吃饭！')

c = Chinese()
c1 = copy(c)
print(id(c))
print(id(c1))
c2 = deepcopy(c1)
print(id(c2))
e = English()
i = Indian()
c.eat()
e.eat()
i.eat()
print(Man.mro())
print(Chinese.mro())

def manEat(m):
    if isinstance(m,Man):
        m.eat()
    else:
        print('不能吃饭！')
#manEat(c)
#manEat(i)
#manEat(e)
print(dir(c))
print(c.__dict__)
print(c.__class__)