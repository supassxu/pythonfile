#coding=utf-8

while True:
    try:
        x = int(input('请输入一个数字：'))
        print('输入的数字：',x)
        if x == 88:
            print('退出程序')
            break
    except BaseException as e:
        print(e)
        print(type(e))
        print('遇到异常！请重新输入。')
    else:
        print('输入的数字为:',x)
    finally:
        print('无论发生任何事情呢，这部分的语句块都会执行，就像现在一样！')

print('循环输入数字的程序结束！')