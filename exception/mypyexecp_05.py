#coding=utf-8
#测试自定义异常类

class AgeError(Exception):
    def __init__(self,errorInfo):
        Exception.__init__(self)
        self.errorInfo = errorInfo
    def __str__(self):
        return str(self.errorInfo) + '年龄错误！应该在1-150之间'

if __name__ == '__main__':
    age = int(input('请输入一个年龄：'))
    if age<0 or age>150:
        raise AgeError
    else:
        print('正常的年龄：',age)