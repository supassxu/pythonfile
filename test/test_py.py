#!/usr/bin/python
# -*- coding: UTF-8 -*-
from pip._vendor.distlib.compat import raw_input

if __name__ == '__main__':
    print("Welcome To Python World!")

    a = 3
    b = 6.7
    c = 3.14
    print('a:',a ,'; b:',b,'; c:',c)

#跨行加法，变更数值类型
    total = a + \
            b + \
            c
    print(total)

#星期几数组
    days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    print(days)

    raw_input("按下 enter 键退出，其他任意键显示...\n")