#Python 练习实例6:斐波那契数列
i = int(input("斐波那契数列的长度："))
a = [0,1]
if(i > 2):
    for i in range(2,i):
        a.append(a[i-1] + a[i-2])
elif(i < 2):
    a = [0]
print(a)