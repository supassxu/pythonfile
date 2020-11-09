#Python 练习实例12:判断101-200之间有多少个素数，并输出所有素数。
import math
s = input("请输入2个正整数，以英文逗号隔开，我们将计算并输出该数字段范围之间的所以素数：").split(',')
a = range(int(s[0]),int(s[1]))
b = []
for i in range(len(a)):
    x = 0
    for j in range(2,int(math.sqrt(a[i]))+1):
        if(a[i] % j == 0):
            x = 1
    if(x == 0):
        b.append(a[i])
print("输入的数字段范围%d-%d之间有%d个素数，具体如下：" % (a[0],a[-1],len(b)))
print(b)