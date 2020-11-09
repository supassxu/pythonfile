#测试工厂模式

class CarFactory:

    __obj = None
    __init_flag = True
    def __new__(cls, *args, **kwargs):
        if cls.__obj == None:
            cls.__obj = object.__new__(cls)
        return cls.__obj

    def __init__(self):
        if CarFactory.__init_flag:
            print('init CarFactory......')
            CarFactory.__init_flag = False

    def create_car(self,brand):
        if brand == '奔驰':
            return Benz()
        elif brand == '宝马':
            return BMW()
        elif brand == '比亚迪':
            return BYD()
        else:
            print('未知品牌，不能造车！')
class Benz:
    pass
class BMW:
    pass
class BYD:
    pass
factory = CarFactory()
c1 = factory.create_car('奔驰')
factory1 = CarFactory()
c2 = factory1.create_car('比亚迪')
print(factory,factory1)
print(c1)
print(c2)
