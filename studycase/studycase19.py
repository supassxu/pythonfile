#Python 练习实例19:一个数如果恰好等于它的因子之和，这个数就称为"完数"。
# 例如6=1＋2＋3.编程找出1000以内的所有完数。

import math
a = int(input("请输入1个正整数，我们将计算并输出该数字段范围之间的所以完数："))
b = []
for i in range(a):
    x,y,z=int(str(a[i])[0]),int(str(a[i])[1]),int(str(a[i])[2])
    if(a[i] == x**3 + y**3 + z**3):
        b.append(a[i])
print("所有的水仙花数%d个，具体如下：" % (len(b)))
print(b)