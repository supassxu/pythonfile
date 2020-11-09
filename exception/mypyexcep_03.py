#int a=3
#print(a)
#a = 3/0
#float('supassxu')
#123+'abc'
#a = 100
#a.sayhi()
#a=[4,5,7]
#print(a[7])
import traceback

try:
    a={'ame':'supassxu','age':28,'job':'tester'}
    a['salary']
except:
    with open('a_error.txt','a') as f:
        traceback.print_exc(file=f)