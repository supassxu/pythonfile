#一球从100米高度自由落下，每次落地后反跳回原高度的一半；
# 再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
s = input('请输入下落高度和反弹次数，以英文逗号隔开，我们将计算累计反弹总距离和最后反弹高度：')
a = int(s.split(',')[0])
b = int(s.split(',')[1])
total = a
high = 0
def func01(x):
    global total
    global high
    x /= 2
    total += high

for i in range(b):
    func01(a)
    print('第{}次反弹高度为{}米，当前反弹至最高处总路程为{}米'.format(i+1,high,total))

print('下落高度{0}米,总共反弹{1}次，总共反弹经过路程{2}米，最后反弹高度{3}米'.format(a,b,total,high))