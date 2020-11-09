#ython 练习实例12:打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和
# 等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
import math
#s = input("请输入2个正整数，以英文逗号隔开，我们将计算并输出该数字段范围之间的所以s水仙花数：").split(',')
a = range(101,999)
b = []
for i in range(len(a)):
    x,y,z=int(str(a[i])[0]),int(str(a[i])[1]),int(str(a[i])[2])
    if(a[i] == x**3 + y**3 + z**3):
        b.append(a[i])
print("所有的水仙花数%d个，具体如下：" % (len(b)))
print(b)