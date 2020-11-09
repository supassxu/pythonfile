#Python 练习实例9:暂停一秒输出。
import time

for i in range(1,10):
    for j in range(i,10):
        #print(str(i) + '*' + str(j) + '=' + str(i*j),end='\t')
        print("%d*%d=%d" % (i, j, i*j),end='\t')
    print()
    time.sleep(5)