
i = str(input('请输入某年某月某日：'))
a =[31,59,90,120,151,181,212,243,273,304,334,365]  #每个月累计天数
#b ={31,28,31,30,31,30,31,31,30,31,30,31}    #每个月单独天数
x = int(i.split('年')[0])
y = int(i.split('年')[1].split('月')[0])
z = int(i.split('年')[1].split('月')[1].split('日')[0])
total = 0
if(x % 4 ==0 and x % 100 !=0):
    total = a[y-2] + z +1
elif(x % 400 ==0):
    total = a[y - 2] + z + 1
else:
    total = a[y - 2] + z
print('输入的' + i + '为当年的第' + str(total) + '天')