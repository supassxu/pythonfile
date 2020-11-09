#Python 练习实例10:暂停一秒输出，并格式化当前时间。
import time

for i in range(5):
    time.sleep(5)
    now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print(now_time)