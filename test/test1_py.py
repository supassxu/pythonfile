#!/usr/bin/python
# -*- coding: UTF-8 -*-

if __name__ == '__main__':
    import sys; x = 'runoob'; sys.stdout.write(x + '\n')

    a = b = c = 1
    e ,f ,g = 1 ,2.36 ,'supassxu'

    print(a ,id(b) ,type(c))
    print(type(e), type(f), type(g))

    str = "Welcome To Python World!"
    print(str)  # 输出完整字符串
    print(str[0]) # 输出字符串中的第一个字符
    print(str[2:5]) # 输出字符串中第三个至第六个之间的字符串
    print(str[2:]) # 输出从第三个字符开始的字符串
    print(str * 2)  # 输出字符串两次
    print(str + "TEST") # 输出连接的字符串