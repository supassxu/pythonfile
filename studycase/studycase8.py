#Python 练习实例8:输出 9*9 乘法口诀表。

for i in range(1,10):
    for j in range(i,10):
        #print(str(i) + '*' + str(j) + '=' + str(i*j),end='\t')
        print("%d*%d=%d" % (i, j, i*j),end='\t')
    print()