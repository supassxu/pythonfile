#coding=utf-8
# Traceback追溯，追根溯源。most recent call last 最后一次调用
try:
    print('step 1')
    a = 3/2
    print('step 2')
except BaseException as e:
    print('step3')
    print(e)
    print((type(e)))
print('程序结束！')