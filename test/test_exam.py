import calendar
import math
import random
import time
import turtle
from collections import Counter
from tkinter.ttk import Style

from click._compat import raw_input
from colorama import Back, Fore
from tkinter import *

'''1、有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？'''


def test_exam_01():
    list_x = []
    for a in range(1, 5):
        for b in range(1, 5):
            if a != b:
                for c in range(1, 5):
                    if a != c and b != c:
                        list_x.append(a * 100 + b * 10 + c)
    print("四个数字：1、2、3、4，能组成{0}个互不相同且无重复数字的三位数".format(str(len(list_x))))
    print(list_x)


'''2、企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元
的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的
部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？'''


def test_exam_02():
    total = 0
    s = int(input("请输入当月利润(单位：万元)，将计算出发放奖金总数："))
    if s <= 10:
        total += s * 0.1
    elif s <= 20:
        total += (s - 10) * 0.075 + 10 * 0.1
    elif s <= 40:
        total += (s - 40) * 0.05 + (20 - 10) * 0.075 + 10 * 0.1
    elif s <= 60:
        total += (s - 60) * 0.03 + (40 - 20) * 0.05 + (20 - 10) * 0.075 + 10 * 0.1
    elif s <= 100:
        total += (s - 60) * 0.015 + (60 - 40) * 0.03 + (40 - 20) * 0.05 + (20 - 10) * 0.075 + 10 * 0.1
    else:
        total += (s - 100) * 0.01 + + (100 - 60) * 0.015 + (60 - 40) * 0.03 + (40 - 20) * 0.05 + (
                20 - 10) * 0.075 + 10 * 0.1
    print("输入的当月利润是%.2f万元，计算出来的发放奖金总数为%.2f万元" % (s, total))


def test_exam_02x():
    total = 0
    s = int(input("请输入当月利润(单位：万元)，将计算出发放奖金总数："))
    a = [10, 20, 40, 60, 100]
    b = [0.1, 0.075, 0.05, 0.03, 0.015, 0.01]
    for i in range(len(b)):
        if i != len(a):
            if s <= a[i]:
                total += (s - a[i - 1]) * b[i]
                break
            else:
                if i == 0:
                    total += a[i] * b[i]
                elif i < len(a):
                    total += (a[i] - a[i - 1]) * b[i]
        else:
            total += (s - a[-1]) * b[i]
    print("输入的当月利润是%.2f万元，计算出来的发放奖金总数为%.2f万元" % (s, total))


'''3、一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？'''


def test_exam_03():
    for i in range(1000):
        for h in range(1000):
            if i + 100 == math.pow(h, 2):
                for j in range(1000):
                    if i + 168 == math.pow(j, 2):
                        print(str(i) + " + 100 = " + str(h) + "^2")
                        print(str(i) + " + 168 = " + str(j) + "^2")
                        print(i)
                        break


'''4、输入某年某月某日，判断这一天是这一年的第几天？'''


def test_exam_04():
    str1 = input("输入某年某月某日格式为{年-月-日}，程序判断这一天是这一年的第几天？\n").split("-")
    x = list(map(int, str1))
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total = 0
    if x[1] == 1:
        total = x[2]
    elif 1 < x[1] < 13:
        total += x[2]
        for i in range(x[1] - 1):
            total += days[i]
        if x[0] % 4 == 0 and x[0] % 100 != 0:
            total += 1
    else:
        print("输入的月份不规范，请重新执行程序！")
    print(total)
    print("输入的日期为：{0}年{1}月{2}日，这一天是这一年的第{3}天。".format(str1[0], str1[1], str1[2], str(total)))


'''5、输入三个整数x,y,z，请把这三个数由小到大输出。'''


def test_exam_05():
    str1 = input("输入三个整数x，y，z以空格隔开，程序将把这3个数有小到大输出。\n").split(" ")
    x = list(map(int, str1))
    x.sort()
    print(x)


'''6、斐波那契数列。'''


def test_exam_06():
    x = int(input("请输入整数x，程序将输出长度为x的斐波那契数列。\n"))
    list_x = [0, 1]
    for i in range(2, x):
        list_x.append(list_x[i - 2] + list_x[i - 1])
    print("长度为{0}的斐波那切数列如下：".format(str(x)))
    print(list_x)


'''7、将一个列表的数据复制到另一个列表中。'''


def test_exam_07():
    x = int(input("请输入整数x，程序将输出长度为x的斐波那契数列。\n"))
    list_x = [0, 1]
    for i in range(2, x):
        list_x.append(list_x[i - 2] + list_x[i - 1])
    list_y = list_x[0:20:2]
    print(list_y)


'''8、输出 9*9 乘法口诀表。'''


def test_exam_08():
    for i in range(1, 10):
        for j in range(i, 10):
            print("{0}*{1}={2}".format(str(i), str(j), str(i * j)), end="\t")
        print()


'''9、暂停一秒输出。'''


def test_exam_09():
    for i in range(1, 10):
        for j in range(i, 10):
            print("{0}*{1}={2}".format(str(i), str(j), str(i * j)), end="\t")
        print()
        time.sleep(1)


'''10、暂停一秒输出，并格式化当前时间。'''


def test_exam_10():
    time.sleep(1)
    # 格式化成2016-03-20 11:45:39形式
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    # 格式化成Sat Mar 28 22:24:24 2016形式
    print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))


'''11、古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？'''


def test_exam_11():
    x = int(input("请输入月份整数x，程序将输出第x月的兔子总数。\n"))
    list_x = [1, 1]
    total = list_x[0] + list_x[1]
    for i in range(2, x):
        list_x.append(list_x[i - 2] + list_x[i - 1])
        total += list_x[i]
    print("请输入月份整数为{0}，第{1}月的兔子总数为{2}。".format(str(x), str(x), str(total)))
    print(list_x)


'''12、判断101-200之间有多少个素数，并输出所有素数。'''


def test_exam_12():
    list_x = []
    for i in range(101, 201):
        flag = True
        for j in range(2, int(math.pow(i, 1 / 2))):
            if i % j == 0:
                flag = False
        if flag:
            list_x.append(i)
    print("101-200之间有{0}个素数，所有素数如下所示：".format(len(list_x)))
    print(list_x)


'''13、打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。'''


def test_exam_13():
    list_x = []
    for i in range(101, 1000):
        if i == math.pow(int(i / 100), 3) + math.pow(int((i % 100) / 10), 3) + math.pow(i % 10, 3):
            list_x.append(i)
    print("所有的水仙花数如下所示：")
    print(list_x)


'''14、将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。'''


def test_exam_14():
    x = int(input("将一个正整数x，程序将分解质因数。\n"))
    list_x = []
    t = x
    i = 2
    flag = True
    print("输入的正整数为{0}，程序将分解质因数如下：".format(str(x)))
    print(str(x), end="")
    while 2 <= i < int(x):
        if t % i == 0:
            list_x.append(i)
            if flag:
                print("=" + str(i), end="")
            else:
                print("*" + str(i), end="")
            t /= i
            i = 2
            flag = False
        else:
            i += 1
    if len(list_x) == 0:
        print("，该正整数为素数，不能被质因数分解。")


'''15、利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。'''


def test_exam_15():
    x = int(input("请输入学生成绩（正整数：0-100之间）x，程序将输出成绩类别。\n"))
    if 100 >= x >= 90:
        print("该生成绩：A")
    elif x > 60:
        print("该生成绩：B")
    elif x > 0:
        print("该生成绩：C")
    else:
        print("输入的成绩有误，不在0-100之间，请重新执行程序，重新输入正确范围内的学生成绩。")


'''16、输出指定格式的日期。（本题写的时候不太熟悉时间控件，所以基本为模仿编写。）'''


def test_exam_16():
    localtime1 = time.localtime(time.time())
    print("本地时间为：", localtime1)

    localtime2 = time.asctime(time.localtime(time.time()))
    print("本地时间为：", localtime2)
    # 格式化成2021-01-01 08:43:50形式"
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    # 格式化成Mon Jun 01 08:43:50形式"
    print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))
    # 将格式字符串转换为时间戳"
    a = "Fri Jan 01 08:49:15 2021"
    print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))

    # 日历模块使用的方法
    cal = calendar.month(2020, 1)
    print("如下输出2020年1月份的日历：")
    print(cal)
    # 判断是否闰年的方法
    print(calendar.isleap(2020))
    print(calendar.isleap(2021))


'''17、输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。'''


def test_exam_17():
    s = input("请输入一行字符，程序将分别统计出其中英文字母、空格、数字和其他字符的个数。\n")
    list_x = [0, 0, 0, 0]
    for i in range(len(s)):
        # print(str(i) + "\t" + s[i]) # 帮助调试查看每次跑循环的字符是哪个
        if s[i].isalpha():
            list_x[0] += 1
        elif s[i].isspace():
            list_x[1] += 1
        elif s[i].isnumeric():
            list_x[2] += 1
        else:
            list_x[3] += 1
    print("输入的一行字符中，共包含英文字母{0}个，空格{1}个，数字{2}个，"
          "其他字符{3}个。".format(str(list_x[0]), str(list_x[1]), str(list_x[2]), str(list_x[3])))
    print(list_x)


'''18、求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。'''


def test_exam_18():
    s = input("请输入一行共2个正整数（第1个表示表达式中的a，第2个表示最后相加数a的位数），由空格隔开，程序将计算s=a+aa+aaa+aaaa+aa...a的值。\n").split(" ")
    x = list(map(int, s))
    list_x = []
    total = 0
    for i in range(1, x[1] + 1):
        str1 = ""
        for j in range(1, i + 1):
            str1 += s[0]
        list_x.append(int(str1))
        total += int(str1)
    print(list_x)
    print("程序计算s=a+aa+aaa+aaaa+aa...a的值为：" + str(total))


'''19、一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。'''


def test_exam_19():
    list_x = []
    # flag = True
    for i in range(1, 1001):
        total = 0
        for j in range(1, i):
            if i % j == 0:
                total += j
        if total == i:
            list_x.append(i)
    if len(list_x) == 0:
        print("1000以内的没有找完数。")
    else:
        print("1000以内的所有完数如下所示：")
        print(list_x)


'''20、一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？'''


def test_exam_20():
    address = 100
    high = 100
    for i in range(1, 11):
        high = high / 2
        address += high
    print("它在第10次落地时，共经过{0}米？第10次反弹{1}米高".format(str(address), str(high)))


'''21、猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个第二天早上又将剩下的桃子吃掉一半，又多吃了一个。以后每天早上
都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。'''


def test_exam_21():
    total = 1
    x = 1
    for i in range(9, 0, -1):
        if i == 9:
            x = 2 * (1 + 1)
            total += x
        else:
            x = 2 * (x + 1)
            total += x
    print("第一天共摘了{0}个桃子。".format(str(total)))


'''22、两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他
不和x,z比，请编程序找出三队赛手的名单。（这道题不会，写的是自己做工逻辑处理的代码，而非完全用程序做的处理的代码）'''


def test_exam_22():  # 下方为菜鸟提供的实现方式
    for i in range(ord('x'), ord('z') + 1):
        for j in range(ord('x'), ord('z') + 1):
            if i != j:
                for k in range(ord('x'), ord('z') + 1):
                    if (i != k) and (j != k):
                        if (i != ord('x')) and (k != ord('x')) and (k != ord('z')):
                            print('order is a -- %s\t b -- %s\tc--%s' % (chr(i), chr(j), chr(k)))

    """pa = {'a': '', 'b': '', 'c': ''}
    pb = ['x', 'y', 'z']
    for i in range(len(pb)):
        if pb[i] == 'x':
            pa['b'] = pb[i]
        elif pb[i] == 'y':
            pa['c'] = pb[i]
        else:
            pa['a'] = pb[i]
    print("三队参赛选手名单如下所示：")
    print(pa)"""


'''23、打印出如下图案（菱形）:
   *
  ***
 *****
*******
 *****
  ***
   *'''


def test_exam_23():
    listx = [1, 3, 5, 7, 5, 3, 1]
    for i in range(1, 8):
        for j in range((i - 4).__abs__()):
            print(" ", end="")
        for x in range(listx[i - 1]):
            print("*", end="")
        print()


'''24、有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。'''


def test_exam_24():
    s = int(input("请输入一个正整数x，程序将计算分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前x项之和。\n"))
    list_x = ['2/1']
    print(list_x[0])
    total = 2 / 1
    for i in range(1, s):
        x = list_x[i - 1].split('/')
        list_x.append(str(int(x[0]) + int(x[1])) + '/' + x[0])
        print(list_x[i])
        total += (int(x[0]) + int(x[1])) / int(x[0])
    print(list_x)
    print("输入的正整数为{0}，程序将计算分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前{1}项之和为：{2}。".format(s, s, total))


'''25、题目：求1+2!+3!+...+20!的和。'''


def test_exam_25():
    total = 0
    for i in range(1, 20):
        t = 1
        for j in range(1, i + 1):
            t *= j
        total += t
    print('1! + 2! + 3! + ... + 20! = %d' % total)


"""26、利用递归方法求5!。"""


def test_exam_26():
    total = 1
    for i in range(1, 5):
        total *= i
    print('5! = %d' % total)


'''27、利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。'''


def test_exam_27():
    s1 = input("请输入一个5个字符的字符串，程序将以相反顺序打印出来。\n")
    print(exchange(s1))


def exchange(s2):
    s = list(s2)
    for i in range(int(len(s) / 2)):
        t = s[i]
        s[i] = s[len(s) - 1 - i]
        s[len(s) - 1 - i] = t
    return "".join(s)


'''28、有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。问第4个人岁数，他说比第3个人大2岁。问第三个人，又说比第2人大两岁。问第2个人，
说比第一个人大两岁。最后问第一个人，他说是10岁。请问第五个人多大？'''


def test_exam_28():
    five_age = 10
    for i in range(5 - 1):
        five_age += 2
    print("第五个人{0}岁".format(five_age))


'''29、给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。'''


def test_exam_29():
    s1 = input("请输入一个不多于5位的正整数，程序将求它是几位数，并且逆序打印出各位数字。\n")
    x = int(s1)
    for i in range(4, -1, -1):
        if x % math.pow(10, i):
            print("输入的数是{0}位数，逆序打印的数字如下：".format(str(i + 1)))
            break
    print(exchange(s1))


'''30、一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。'''


def test_exam_30():
    s1 = input("请输入一个不多于5位的正整数，程序将求它是几位数，并且逆序打印出各位数字。\n")
    if int(s1) == int(exchange(s1)):
        print("输入的数为{0}，该数逆序处理之后为{1}，它是回文数。".format(s1, exchange(s1)))
    else:
        print("输入的数为{0}，该数逆序处理之后为{1}，它不是回文数。".format(s1, exchange(s1)))


'''31、请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。'''


def test_exam_31():
    s = input("请输入一个星期的英文单词，程序将判断并输出英文全称。\n")
    week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    for i in range(len(week)):
        if s[0].upper() == week[i][0] and s[0].upper() != 'T' and s[0].upper() != 'S':
            print("输入的日期为{0}，程序判断输出的日期为：{1}".format(s, week[i]))
            break
        elif (s[0].upper() == 'T' or s[0].upper() == 'S') and s[1].lower() == week[i][1]:
            print("输入的日期为{0}，程序判断输出的日期为：{1}".format(s, week[i]))
            break


'''32、按相反的顺序输出列表的值。'''


def test_exam_32():
    s2 = input("请输入一个5个字符的字符串，程序将以相反顺序打印出来。\n")
    s = list(s2)
    print("转换前列表具体如下：")
    print(s)
    for i in range(int(len(s) / 2)):
        t = s[i]
        s[i] = s[len(s) - 1 - i]
        s[len(s) - 1 - i] = t
    print("转换后列表具体如下：")
    print(s)


'''33、按逗号分隔列表。(没理解这道题，然后是模仿的一道题)'''


def test_exam_33():
    l1 = [1, 2, 3, 4, 5]
    s1 = ','.join(str(n) for n in l1)
    print(s1)


'''34、练习函数调用。使用函数，输出三次 SUPASSXU 字符串。'''


def test_exam_34():
    print_3_time("SUPASSXU")


def print_3_time(str1):
    for i in range(3):
        print(str1)


'''35、文本颜色设置。（本题为网上搜索寻找，对这块不太熟悉。）'''


def test_exam_35():
    # 方法一：
    print('\033[1;31;40m')
    print('*' * 50)
    print('\033[7;31m错误次数超限，用户已经被永久锁定，请联系管理员！\033[1;31;40m')
    print('*' * 50)
    print('\033[0m')
    print('\033[0m这是显示方式0')
    print('\033[1m这是显示方式1')
    print('\033[4m这是显示方式4')
    print('\033[5m这是显示方式5')
    print('\033[7m这是显示方式7')
    print('\033[8m这是显示方式8')
    print('\033[30m这是前景色0')
    print('\033[31m这是前景色1')
    print('\033[32m这是前景色2')
    print('\033[33m这是前景色3')
    print('\033[34m这是前景色4')
    print('\033[35m这是前景色5')
    print('\033[36m这是前景色6')
    print('\033[37m这是前景色7')
    print('\033[40m这是背景色0')
    print('\033[41m这是背景色1')
    print('\033[42m这是背景色2')
    print('\033[43m这是背景色3')
    print('\033[44m这是背景色4')
    print('\033[45m这是背景色5')
    print('\033[46m这是背景色6')
    print('\033[47m这是背景色7')
    # 方法二：
    print(Fore.RED + "some red text")
    print(Back.GREEN + "and with a green background")
    print(Style.DIM + "and in dim text")
    print(Style.RESET_ALL)
    print("back to normal now!!")


'''36、求100之内的素数。'''


def test_exam_36():
    list_x = []
    for i in range(2, 101):
        flag = True
        for j in range(2, int(math.pow(i, 1 / 2)) + 1):
            if i % j == 0:
                flag = False
        if flag:
            list_x.append(i)
    print("1-100之间有{0}个素数，所有素数如下所示：".format(len(list_x)))
    print(list_x)


'''37、对10个数进行排序。'''


def test_exam_37():
    str1 = input("请输入10个整数，以空格隔开的字符串，程序将排列顺序打印出来。\n").split(" ")
    x = list(map(int, str1))
    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            if x[i] >= x[j]:
                t = x[i]
                x[i] = x[j]
                x[j] = t
    print("排列顺序后的10个数如下：")
    print(x)


'''38、求一个3*3矩阵主对角线元素之和。'''


def test_exam_38():
    x = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
    total = 0
    for i in range(x.__len__()):
        for j in range(x[i].__len__()):
            if i == j:
                total += x[i][j]
            elif i + j == 2:
                total += x[i][j]
    print("程序所给3*3数组如下：")
    print(x)
    print("3*3矩阵主对角线元素之和为{0}".format(str(total)))


'''39、有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。'''


def test_exam_39():
    str1 = int(input("请输入1个整数，程序将按照排列顺序插入数组之中。\n"))
    x = [1, 3, 6, 8, 13, 15, 24, 33, 51]
    print("插入输入的整数{0}前，数组排序如下：".format(str(str1)))
    print(x)
    address = 0
    # x.append(str1)
    for i in range(x.__len__()):
        if str1 >= x[i]:
            address += 1
    x.append(0)
    for i in range(x.__len__() - 1, address, -1):
        x[i] = x[i - 1]
    x[address] = str1
    print("插入输入的整数{0}后，数组排序如下：".format(str(str1)))
    print(x)


'''40、将一个数组逆序输出。'''


def test_exam_40():
    s = [1, 3, 6, 8, 13, 15, 24, 33, 51]
    print("逆序转换前数组具体如下：")
    print(s)
    for i in range(int(len(s) / 2)):
        t = s[i]
        s[i] = s[len(s) - 1 - i]
        s[len(s) - 1 - i] = t
    print("转换后列表具体如下：")
    print(s)


'''41、模仿静态变量的用法。(该题为宽泛性问题，模仿跟着题目做的)'''

'''class Static:
    StaticVar = 5

    def test_exam_41(self):
        self.StaticVar += 1
        print(self.StaticVar)


print(Static.StaticVar)
a = Static()
for i in range(3):
    a.test_exam_41()'''


def test_exam_41():
    var = 0
    print('var = %d' % var)
    var += 1


'''42、学习使用auto定义变量的用法。（自定义方法）'''


def auto_func():
    print("调用方法并返回从1加到10的和")
    total = 0
    for i in range(10):
        total += i
    return total


def test_exam_42():
    print("调用字符串逆序方法")
    print(exchange("0123456789"))
    print(auto_func())


'''43、模仿静态变量(static)另一案例。(参考)'''


class Num:
    nNum = 1

    def test_exam_43(self):
        self.nNum += 1
        print('nNum = %d' % self.nNum)


'''44、两个 3 行 3 列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵：
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]'''


def test_exam_44():
    x = [[12, 7, 3],
         [4, 5, 6],
         [7, 8, 9]]
    y = [[5, 8, 1],
         [6, 7, 3],
         [4, 5, 9]]
    z = [[0 for col in range(3)] for row in range(3)]
    for i in range(3):
        for j in range(3):
            z[i][j] = x[i][j] + y[i][j]
    print("2个3行3列的数组对应元素相加之后得到的数组如下：")
    print(z)


'''45、统计 1 到 100 之和。'''


def test_exam_45():
    total = 0
    for i in range(1, 101):
        total += i
    print("1 到 100 之和为%d" % total)


'''46、求输入数字的平方，如果平方运算后小于 50 则退出。'''


def test_exam_46():
    x = int(input("请输入一个数字，程序将计算并输出大于等于50的数字和它的平方运算值。\n"))
    y = math.pow(x, 2)
    if y < 50:
        exit()
    else:
        print("输入的数为{0}，计算得出的平方值为{1}".format(x, y))


'''47、两个变量值互换。'''


def test_exam_47():
    a = 3
    b = 'abcdefg'
    print("转换前变量a为{0}，变量b为{1}".format(str(a), b))
    t = a
    a = b
    b = t
    print("转换前变量a为{0}，变量b为{1}".format(str(a), str(b)))


'''48、数字比较。'''


def test_exam_48():
    a = int(input("请输入第1个数字，程序将比对并输出和第2个数的大小结果。\n"))
    b = int(input("请输入第2个数字，程序将比对并输出和第1个数的大小结果。\n"))
    if a == b:
        print("{0}等于{1}".format(str(a), str(b)))
    elif a < b:
        print("{0}小于{1}".format(str(a), str(b)))
    else:
        print("{0}大于{1}".format(str(a), str(b)))


'''49、使用lambda来创建匿名函数。'''


def test_exam_49():
    print("使用lambda函数传入参数创建并初始化2维数组！")
    x = lambda a, b: [[0 for col in range(a)] for row in range(b)]
    print(x(5, 5))


'''50、输出一个随机数。'''


def test_exam_50():
    print("程序将输出0-100之间的随机数。")
    print(random.randint(0, 100))           # 产生n--m范围内的一个随机数
    print(random.random())                  # 产生0到1之间的一个随机数
    print(random.uniform(1.3, 3.6))         # 产生n--m范围内的一个浮点数
    print(random.randrange(0, 100, 5))      # 产生n--m范围内间隔为k的整数
    print(random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))  # 序列中随机选取一个元素
    print(random.shuffle([1, 3, 5, 7, 9]))                # 在一些特殊的情况下可能对序列进行一次打乱操作


'''51、学习使用按位与 & 。'''


def test_exam_51():
    a = 58      # a = 0011 1010
    b = 11      # b = 0000 1011
    c = 0       # c = 0000 0000
    c = a & b   # c = 0000 1010 = 10（ten）
    print(c)


'''52、学习使用按位或 |。'''


def test_exam_52():
    a = 58      # a = 0011 1010
    b = 11      # b = 0000 1011
    c = 0       # c = 0000 0000
    c = a | b   # c = 0011 1011 = 59（ten）
    print(c)


'''53、学习使用按位异或 ^ 。'''


def test_exam_53():
    a = 58      # a = 0011 1010
    b = 11      # b = 0000 1011
    c = 0       # c = 0000 0000
    c = a ^ b   # c = 0011 0001 = 49（ten）
    print(c)


'''54、取一个整数a从右端开始的4〜7位。'''


def test_exam_54():
    s = input("请输入7位数以上的整数，程序将取从右端开始的4〜7位并输出该数\n")
    if len(s) >= 7:
        str1 = s[-4: -8: -1]
        print(str1)
    else:
        print("整数的长度小于7，请重新输入位数大于7的整数。")


'''55、学习使用按位取反~。'''


def test_exam_55():
    a = 58      # a = 0011 1010
    c = 0       # c = 0000 0000
    c = ~a      # c = 1100 0101 = -59（ten）
    print(c)


'''56、画图，学用circle画圆形。'''


def test_exam_56():
    x1, y1 = 100, 100
    x2, y2 = 100, -100
    x3, y3 = -100, -100
    x4, y4 = -100, 100

    # 绘制折线
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.circle(10)
    turtle.goto(x2, y2)
    turtle.circle(20)
    turtle.goto(x3, y3)
    turtle.circle(30)
    turtle.goto(x4, y4)
    turtle.circle(50)
    turtle.done()


'''57、画图，学用line画直线。'''


def test_exam_57():
    x1, y1 = 100, 100
    x2, y2 = 100, -100
    x3, y3 = -100, -100
    x4, y4 = -100, 100

    # 绘制折线
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()

    turtle.goto(x2, y2)
    turtle.goto(x3, y3)
    turtle.goto(x4, y4)
    turtle.done()


'''58、画图，学用rectangle画方形。(这题不会，模仿学习的代码)'''


def test_exam_58():
    tk = Tk()
    tk.title('rectangle')
    canvas = Canvas(tk, width=400, height=400, bg='red')
    x0 = 263
    y0 = 263
    x1 = 275
    y1 = 275
    for i in range(19):
        canvas.create_rectangle(x0, y0, x1, y1)
        x0 -= 5
        y0 -= 5
        x1 += 5
        y1 += 5
    canvas.pack()
    tk.mainloop()


'''59、画图，综合例子。(程序分析：利用for循环控制100-999个数，每个数分解出个位，十位，百位。)'''


def test_exam_59():
    canvas = Canvas(width=300, height=300, bg='green')
    canvas.pack(expand=YES, fill=BOTH)
    x0 = 150
    y0 = 100
    canvas.create_oval(x0 - 10, y0 - 10, x0 + 10, y0 + 10)
    canvas.create_oval(x0 - 20, y0 - 20, x0 + 20, y0 + 20)
    canvas.create_oval(x0 - 50, y0 - 50, x0 + 50, y0 + 50)
    b = 0.809
    for i in range(16):
        a = 2 * math.pi / 16 * i
        x = math.ceil(x0 + 48 * math.cos(a))
        y = math.ceil(y0 + 48 * math.sin(a) * b)
        canvas.create_line(x0, y0, x, y, fill='red')
    canvas.create_oval(x0 - 60, y0 - 60, x0 + 60, y0 + 60)

    for k in range(501):
        for i in range(17):
            a = 2 * math.pi / 16 * i + (2 * math.pi / 180) * k
            x = math.ceil(x0 + 48 * math.cos(a))
            y = math.ceil(y0 + 48 * math.sin(a) * b)
            canvas.create_line(x0, y0, x, y, fill='red')
        for j in range(17):
            a = 2 * math.pi / 16 * j + (2 * math.pi / 180) * k
            x = math.ceil(x0 + 48 * math.cos(a))
            y = math.ceil(y0 + 48 * math.sin(a) * b)
            canvas.create_line(x0, y0, x, y, fill='red')
    mainloop()


'''60、计算字符串长度。'''


def test_exam_60():
    s = input("请输入一行字符串，程序将计算并输出该字符串的长度\n")
    print("输入字符串的长度为：{0}".format(len(s)))


'''61、打印出杨辉三角形（要求打印出10行如下图）。'''


def test_exam_61():
    s = int(input("请输入一个正整数，程序将输出包含输入整数行的杨辉三角\n"))
    a = [[0 for col in range(s)] for row in range(s)]
    a[0][0] = 1
    for i in range(1, s):
        for j in range(i):
            if j == 0:
                a[i][j] = 1
                print("1", end="\t")
            elif j == i - 1:
                a[i][j] = 1
                print("1", end="")
            else:
                a[i][j] = a[i-1][j-1] + a[i-1][j]
                print(str(a[i][j]), end="\t")
        print()


'''62、查找字符串。'''


def test_exam_62():
    s = input("请输入1个字符串，作为查找样本字符串\n")
    x = input("请输入1个字符串，程序将从上一个字符串中找出本字符串所在的位置\n")
    index = s.find(x) + 1
    if index != -1:
        print("第二行输入的字符串在第一行输入字符串的第{0}个字母位置".format(str(index)))
    else:
        print("第二行输入的字符串在第一行输入字符串中找不到")


'''63、画椭圆。（完全不会，跟着搜索出来的题目模仿，模仿完好像也不会，哈哈）'''


def test_exam_63():
    import matplotlib.pyplot as plt
    from matplotlib.patches import Ellipse

    fig = plt.figure(0)
    ax = fig.add_subplot(111, aspect='equal')
    e = Ellipse(xy=(0, 2), width=1.81*2, height=0.94*2, angle=27.6)
    ax.add_artist(e)

    e.set_facecolor("green")
    plt.xlim(-2, 2)
    plt.ylim(0.5, 3.5)
    ax.grid(True)
    plt.title("50% Probablity Contour - Homework 4.2")
    plt.show()


'''64、利用ellipse 和 rectangle 画图。（完全不会，跟着搜索出来的题目模仿）'''


def test_exam_64():
    canvas = Canvas(width=400, height=600, bg='white')
    left = 20
    right = 50
    top = 50
    num = 15
    for i in range(num):
        canvas.create_oval(250 - right, 250 - left, 250 + right, 250 + left)
        canvas.create_oval(250 - 20, 250 - top, 250 + 20, 250 + top)
        canvas.create_rectangle(20 - 2*i, 20 - 2*i, 10 * (i+2), 10 * (i+2))
        right += 5
        left += 5
        top += 10
    canvas.pack()
    mainloop()


'''65、一个最优美的图案。(开放性问题没有参考答案，本题解题参考题目平台)'''


class PTS:
    def __init__(self):
        self.x = 0
        self.y = 0
points = []


def test_exam_65():
    screen_x = 400
    screen_y = 400
    canvas = Canvas(width=screen_x, height=screen_y, bg='white')

    AspectRatio = 0.85
    MAXPTS = 15
    h = screen_y
    w = screen_x
    xcenter = w / 2
    ycenter = h / 2
    radius = (h - 30) / (AspectRatio * 2) - 20
    step = 360 / MAXPTS
    angle = 0.0
    for i in range(MAXPTS):
        rads = angle * math.pi / 180.0
        p = PTS()
        p.x = xcenter + int(math.cos(rads) * radius)
        p.y = ycenter + int(math.sin(rads) * radius * AspectRatio)
        angle += step
        points.append(p)
    canvas.create_oval(xcenter - radius, ycenter - radius, xcenter + radius, ycenter + radius)
    for i in range(MAXPTS):
        for j in range(i, MAXPTS):
            canvas.create_line(points[i].x, points[i].y, points[j].x, points[j].y)
    canvas.pack()
    mainloop()


'''66、输入3个数a,b,c，按大小顺序输出。'''


def test_exam_66():
    s = input("请输入3个数，空格隔开，程序将比较后按从小到大顺序输出。\n").split(" ")
    x = list(map(int, s))
    x.sort()
    for i in range(x.__len__()):
        print(x[i], end="\t")


'''67、输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。'''


def test_exam_67():
    s = input("请输入一组数，空格隔开，程序将最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。\n").split(" ")
    x = list(map(int, s))
    min = max = x[0]
    a = b = 0
    for i in range(1, x.__len__()):
        if x[i] >= max:
            max = x[i]
            a = i
        elif x[i] < min:
            min = x[i]
            b = i
    t = x[0]
    x[0] = x[a]
    x[a] = t
    t = x[-1]
    x[-1] = x[b]
    x[b] = t
    for i in range(x.__len__()):
        print(x[i], end="\t")


'''68、有 n 个整数，使其前面各数顺序向后移 m 个位置，最后 m 个数变成最前面的 m 个数。'''


def test_exam_68():
    s = input("请输入n个整数，空格隔开，之后根据提示输入整数m，程序将使其前面各数顺序向后移 m 个位置，最后 m 个数变成最前面的 m 个数。\n").split(" ")
    m = int(input("请输入整数m，程序将使其前面各数顺序向后移 m 个位置，最后 m 个数变成最前面的 m 个数，并输入该内容。\n"))
    for i in range(-m, 0):
        s.insert(i+m, s[i])
        s.pop(i)
    for i in range(s.__len__()):
        print(s[i], end="\t")


'''69、有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位。'''


def test_exam_69():
    s = int(input("请输入1个整数n，程序从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，计算最后留下的是原来第几号的那位。\n"))
    x = [i for i in range(1, s+1)]
    # print(x)  # 用于生成对应的数据在notepad++文档中手动调试
    i = t = 0
    while len(x) > 1:
        t += 1
        if t == 4:
            t = 1
        i += 1
        if i > len(x):
            i = 1
        if t == 3:
            x.pop(i-1)
            i -= 1
    print("从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，计算最后留下的是原来第{0}号的那位".format(str(x[0])))


'''70、写一个函数，求一个字符串的长度，在main函数中输入字符串，并输出其长度。'''


def test_exam_70(s):
    print("该字符串长度为：{0}".format(len(s)))


'''71、编写input()和output()函数输入，输出5个学生的数据记录。（开放性题目，跟着模仿写的代码）'''
n = 3
student = []


def test_exam_71_input_stu(str1):
    for i in range(5):
        student.append(['', '', []])
    for i in range(n):
        str1[i][0] = raw_input('input student num:\n')
        str1[i][1] = raw_input('input student name:\n')
        for j in range(3):
            str1[i][2].append(int(raw_input('score:\n')))


def test_exam_71_output_stu(str1):
    for i in range(n):
        print('%-6s%-10s' % (str1[i][0], str1[i][1]))
        for j in range(3):
            print('%-8d' % str1[i][2][j])


'''72、创建一个链表。(跟着平台模仿写的代码)'''


def test_exam_72():
    ptr = []
    for i in range(5):
        num = int(raw_input('请输入1个数字：\n'))
        ptr.append(num)
    print(ptr)


'''73、反向输出一个链表。'''


def test_exam_73():
    ptr = []
    for i in range(5):
        num = int(raw_input('请输入1个数字：\n'))
        ptr.append(num)
    for i in range(len(ptr)-1, -1, -1):
        print(ptr[i], end='\t')


'''74、列表排序及连接。'''


def test_exam_74():
    str1 = input("输入一组整数数组a，以空格隔开。\n").split(" ")
    str2 = input("输入一组整数数组b，以空格隔开，程序将把这2个数组进行连接后排序输出。\n").split(" ")
    a = list(map(int, str1))
    b = list(map(int, str2))
    a.extend(b)
    print(a)
    a.sort()
    print(a)


'''75、放松一下，算一道简单的题目。'''
'''while True:
    a = input('请输入Q或q退出当前程序：')
    if(a.__eq__('q') or a=='Q'):
        print('程序循环结束，退出！')
        break
print(a)'''


def test_exam_75():
    salarySum = 0
    salarys = []
    for i in range(4):
        s = input('请输入一共4位同事的薪资（按q或Q中途结束）：')
        if s.upper() == 'Q':
            print('录入完成，退出')
            break
        if float(s) < 0:
            continue
        salarys.append(float(s))
        salarySum += float(s)
    else:
        print('您已经全部录入一共4位同事的薪资')
    print('录入薪资：', salarys)
    print('平均薪资{0}'.format(salarySum / 4))


'''76、编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n。'''


def test_exam_76():
    n = int(input("输入1个数a，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n。\n"))
    total = 0
    if n % 2 == 0:
        for i in range(2, n+1, 2):
            total += 1/i
    else:
        for i in range(1, n+1, 2):
            total += 1/i
    print("输入的数为{0}，计算的结果为{1}。".format(n, total))


'''77、循环输出列表。'''


def test_exam_77():
    str1 = input("输入一组整数数组a，以空格隔开，程序将输出这个数组的内容。\n").split(" ")
    for i in range(len(str1)):
        print(str1[i], end="\t")


'''78、找到年龄最大的人，并输出。请找出程序中有什么问题。（使用了2个数组）'''


def test_exam_78():
    str1 = input("输入一组代表一群人年龄的整数，以空格隔开，程序将输出这群人中年龄最大的年龄。\n").split(" ")
    x = list(map(int, str1))
    max = x[0]
    for i in range(1, len(str1)):
        if max <= x[i]:
            max = x[i]
    print("这群人中年龄最大的是{0}岁".format(str(max)))


'''79、字符串排序。'''


def test_exam_79():
    str1 = input("请输入一串字符串，程序将进行字符串排序并输出排序后的字符串。\n")
    ls = list(str1)
    ls.sort()
    str2 = "".join(ls)
    print(str2)


'''80、海滩上有一堆桃子，五只猴子来分。第一只猴子把这堆桃子平均分为五份，多了一个，这只猴子把多的一个扔入海中，拿走了一份。
第二只猴子把剩下的桃子又平均分成五份，又多了一个，它同样把多的一个扔入海中，拿走了一份，第三、第四、第五只猴子都是这样做的，
问海滩上原来最少有多少个桃子？(第5只猴子可以操作时，则最少有6个桃子，第5只猴子最少拿到1个桃子，所剩的桃子为前1只面对桃子总数-1的3/4)'''


def test_exam_80():
    i = 1
    while True:
        total5 = 5 * i + 1
        total = total5
        for j in range(4):
            total = 5 * total / 4 + 1
            if total != int(total):
                break
        if total == int(total):
            print("海滩上原来最少有个{0}桃子，第5只猴子拿到了{1}个桃子。".format(str(total), str(i)))
            break
        i += 1


'''81、809*??=800*??+9*?? 其中??代表的两位数, 809*??为四位数，8*??的结果为两位数，9*??的结果为3位数。求??代表的两位数，及809*??后的结果。'''


def test_exam_81():
    for i in range(11, 100):
        if 10000 > 809 * i > 999 and 8 * i < 100 and 99 < 9 * i < 1000:
            print("??代表的两位数为{0}，809*??后的结果为{1}。".format(str(i), str(809 * i)))
            break


'''82、八进制转换为十进制。'''


def test_exam_82():
    a = input("请输入八进制数(整数)，程序将转为十进制数并输出。\n")
    b = int(a, 8)
    print("输入的八进制数为{0}，转换的十进制数为{1}。".format(str(a), str(b)))


def test_exam_82x():
    s = input("请输入八进制数(整数)，程序将转为十进制数并输出。\n")
    sum = 0
    for i in range(len(s)):
        sum += int(s[i]) * (8 ** (len(s)-i - 1))
    print("输入的八进制数为{0}，转换的十进制数为{1}。".format(s, str(sum)))


'''83、求0—7所能组成的奇数个数。（没弄懂题目为啥没限制小数位，跟着题目学习模仿写代码）'''


def test_exam_83():
    # x = [0, 1, 2, 3, 4, 5, 6, 7]
    total = 4
    s = 4
    for i in range(2, 9):
        print(total)
        if i <= 2:
            s *= 7
        else:
            s *= 8
        total += s
    print("0-7所能组成的奇数的个数为：{0}".format(str(total)))


'''84、连接字符串。'''


def test_exam_84():
    str1 = input("请输入第1个字符串。\n")
    str2 = input("请输入第2个字符串，程序将这2个字符串进行连接并输出。\n")
    print(str1 + str2)
    a = ['abc', '123', 'efgh', '4567658']
    print(','.join(a))


'''85、输入一个奇数，然后判断最少几个 9 除于该数的结果为整数。'''


def test_exam_85():
    str1 = int(input("请输入1个奇数，程序将判断最少几个 9 除于该数的结果为整数。\n"))
    a = 1
    if str1 % 2 != 0:
        while True:
            if (math.pow(10, a)-1) % str1 == 0:
                print("输入的奇数为{0}，最少需要{1}个9除于该数的结果为整数。".format(str(str1), str(a)))
                break
            a += 1
    else:
        print("输入的数为{0}，不是奇数，不进行计算，请重新执行程序后输入奇数。".format(str(str1)))


'''86、两个字符串连接程序。'''


def test_exam_86():
    str1 = input("请输入第1个字符串。\n")
    str2 = input("请输入第2个字符串，程序将这2个字符串进行连接并输出。\n")
    a = str1 + str2
    print(a)


'''87、回答结果（结构体变量传递）。(没看明白，跟着题目模仿写代码)'''


class students:
    count = 0
    score = 0


def func(stu):
    stu.count = 20
    stu.score = 'c'


def test_exam_87():
    a = students()
    a.count = 3
    a.score = 'b'
    func(a)
    print(a.count, a.score)


'''88、读取7个数（1—50）的整数值，每读取一个值，程序打印出该值个数的＊。'''


def test_exam_88():
    print("请依次输入7个数（1—50），每读取一个值，程序打印出该值个数的＊")
    for i in range(7):
        a = int(input("请输入第{0}个数：\n".format(str(i+1))))
        for j in range(a):
            print("＊", end="")
        print()


'''89、某个公司采用公用电话传递数据，数据是四位的整数，在传递过程中是加密的，加密规则如下：每位数字都加上5,然后用和除以10的余数代替该数字，
再将第一位和第四位交换，第二位和第三位交换。'''


def test_exam_89():
    str1 = input("请输入四位的整数，程序将输出加密之后的数。\n")
    a = list(str1)
    for i in range(len(a)):
        a[i] = str((int(a[i]) + 5) % 10)
    for i in range(int(len(a) / 2)):
        t = a[i]
        a[i] = a[len(a) -1 - i]
        a[len(a) - 1 - i] = t
    print("加密规则：每位数字都加上5,然后用和除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换。输入的数字加密后输出如下：")
    print("".join(a))


'''90、列表使用实例。'''


def test_exam_90():
    str1 = input("请输入一行字符串，程序将进行列表处理并输出。\n")
    a = list(str1)
    print("列表的长度为%d" % len(a))
    print(a[1:])
    print(a[-5:])
    a.extend([1, 3, 5])
    print(a)
    a.pop(1)
    print(a)
    a.clear()
    print(a)


'''91、时间函数举例1。'''


def test_exam_91():
    localtime = time.localtime(time.time())
    print("本地时间为：", localtime)
    print("本地时间为：", time.asctime(localtime))


'''92、时间函数举例2。'''


def test_exam_92():
    # 格式化成2021-01-17 11:45:39形式
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    # 格式化成Sat Mar 28 09:24:24 2021形式
    print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))
    # 将格式字符串转换为时间戳
    a = "Sun Jan 17 10:59:09 2021"
    print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))


'''93、时间函数举例3。'''


def test_exam_93():
    cal1 = calendar.month(2021, 1)
    print("以下输出2021年1月份的日历：")
    print(cal1)
    # 判断是否闰年
    print(calendar.isleap(2020))
    time.sleep(3)
    print(calendar.isleap(2021))


'''94、时间函数举例4,一个猜数游戏，判断一个人反应快慢。(不会，跟着题目模仿写代码)'''


def test_exam_94():
    play = input("你想玩这个游戏么？（\'y\' 或者 \'n\'）\n")
    while play == 'y':
        # c = input("请输入一个字符：\n")
        i = random.randint(0, 101)
        # print("请输入你要猜的数：")
        # start_time = time.clock()
        a = time.time()
        print(a)
        guess = int(input("请输入你猜的数：\n"))
        while guess != i:
            if guess > i:
                print("请输入一个更小的数：")
                guess = int(input("请输入你猜的数：\n"))
            else:
                print("请输入一个更大的数：")
                guess = int(input("请输入你猜的数：\n"))
        # end_time = time.clock()
        b = time.time()
        print(b)
        # var = (end_time - start_time) / 18.2
        # print(var)
        var = b - a
        print('这次猜数游戏花费了你{:.2f}秒的时间。'.format(var))
        if var < 15:
            print("不错哟，15s内猜出来了！")
        elif var < 25:
            print("还可以，15-25s内猜出来了！")
        else:
            print("速度有点落后了，25s以上猜出来了！")
        print("Congradulations, The number you guess is {0}".format(i))
        play = input("你还想再次玩这个游戏么？（\'y\' 或者 \'n\'）\n")


'''95、字符串日期转换为易读的日期格式。(跟着题目模仿写代码)'''


def test_exam_95():
    from dateutil import  parser
    dt1 = parser.parse("Jan 17 2021 10:58AM")
    print(dt1)


'''96、计算字符串中子串出现的次数。'''


def test_exam_96():
    str1 = input("请输入一行字符串：\n")
    str2 = input("请输入上面一行字符串的一部分，程序将计算该子串出现在上一行字符串中的次数：\n")
    print("统计第一行字符串中全部字符出现的次数：")
    print(Counter(str1))
    print("统计第一行字符串中单个字符a出现的次数：")
    print(str1.count('a'))
    print("统计第一行字符串中第2行子串出现的次数：")
    print(str1.count(str2))


'''97、从键盘输入一些字符，逐个把它们写到磁盘文件上，直到输入一个 # 为止。'''


def test_exam_97():
    f = open("E:/testfile.txt", "w+")
    print("请从键盘输入一些字符，逐个把它们写到磁盘文件上，直到输入一个 # 为止。")
    while True:
        a = input()
        if a.find('#') != -1:
            str1 = a[:a.index('#')]
            f.write(str1)
            break
        else:
            f.write(a)
    f.close()


'''98、从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个磁盘文件"test"中保存。'''


def test_exam_98():
    str1 = input("请输入一行英文字母，程序将转换成大写后输出到磁盘文件test中。\n")
    str2 = str1.upper()
    print(str2)
    f = open("E:/test.txt", "w+")
    f.write(str2)
    f.close()


'''99、有两个磁盘文件A和B,各存放一行字母,要求把这两个文件中的信息合并(按字母顺序排列), 输出到一个新文件C中。'''


def test_exam_99():
    fa = open("E:/testA.txt", 'r')
    a = list(fa.readline())
    print(a)
    fa.close()
    fb = open("E:/testB.txt", 'r')
    b = list(fb.readline())
    print(b)
    fb.close()
    a.extend(b)
    a.sort()
    str1 = "".join(a)
    print(str1)
    fc = open("E:/testC.txt", "w+")
    fc.write(str1)
    fc.close()


'''100、列表转换为字典。'''


def test_exam_100():
    a = [1, 2, 3, 4, 5, 'a', 'b', 'c', 'd', 'e']
    dt = {}
    for i in range(len(a)):
        dt[str(i)] = a[i]
    print(dt)


if __name__ == '__main__':
    # test_exam_01()
    # test_exam_02()
    # test_exam_02x()
    # test_exam_03()
    # test_exam_04()
    # test_exam_05()
    # test_exam_06()
    # test_exam_07()
    # test_exam_08()
    # test_exam_09()
    # test_exam_10()
    # test_exam_11()
    # test_exam_12()
    # test_exam_13()
    # test_exam_14()
    # test_exam_15()
    # test_exam_16()
    # test_exam_17()
    # test_exam_18()
    # test_exam_19()
    # test_exam_20()
    # test_exam_21()
    # test_exam_22()
    # test_exam_23()
    # test_exam_24()
    # test_exam_25()
    # test_exam_26()
    # test_exam_27()
    # test_exam_28()
    # test_exam_29()
    # test_exam_30()
    # test_exam_31()
    # test_exam_32()
    # test_exam_33()
    # test_exam_34()
    # test_exam_35()
    # test_exam_36()
    # test_exam_37()
    # test_exam_38()
    # test_exam_39()
    # test_exam_40()
    '''for i in range(3):
        test_exam_41()'''
    # test_exam_42()
    '''nNum = 2
    inst = Num()
    for i in range(3):
        nNum += 1
        print('The num = %d' % nNum)
        inst.test_exam_43()'''
    # test_exam_44()
    # test_exam_45()
    # test_exam_46()
    # test_exam_47()
    # test_exam_48()
    # test_exam_49()
    # test_exam_50()
    # test_exam_51()
    # test_exam_52()
    # test_exam_53()
    # test_exam_54()
    # test_exam_55()
    # test_exam_56()
    # test_exam_57()
    # test_exam_58()
    # test_exam_59()
    # test_exam_60()
    # test_exam_61()
    # test_exam_62()
    # test_exam_63()
    # test_exam_64()
    # test_exam_65()
    # test_exam_66()
    # test_exam_67()
    # test_exam_68()
    # test_exam_69()
    # str1 = input("请输入1行字符串，程序将输入该字符串长度。\n")
    # test_exam_70(str1)
    '''test_exam_71_input_stu(student)
    print(student)
    test_exam_71_output_stu(student)'''
    # test_exam_72()
    # test_exam_73()
    # test_exam_74()
    # test_exam_75()
    # test_exam_76()
    # test_exam_77()
    # test_exam_78()
    # test_exam_79()
    # test_exam_80()
    # test_exam_81()
    # test_exam_82()
    # test_exam_82x()
    # test_exam_83()
    # test_exam_84()
    # test_exam_85()
    # test_exam_86()
    # test_exam_87()
    # test_exam_88()
    # test_exam_89()
    # test_exam_90()
    # test_exam_91()
    # test_exam_92()
    # test_exam_93()
    # test_exam_94()
    # test_exam_95()
    # test_exam_96()
    # test_exam_97()
    # test_exam_98()
    # test_exam_99()
    test_exam_100()