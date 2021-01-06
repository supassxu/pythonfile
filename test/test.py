'''import requests
url = 'www.test.org'
data = {'username': 'user', 'password': '123456'}
response = requests.post(url, data)'''
flag = True
mount = 1
list_a = []
while flag:
    s = input()
    if len(s) > 0:
        a = int(s)
        for i in range(a):
            flag_b = True
            t = int(input())
            if len(list_a) != 0:
                for j in range(len(list_a)):
                    if t == list_a[j]:
                        flag_b = False
                        break
                if flag_b:
                    list_a.append(t)
            else:
                list_a.append(t)
    else:
        flag = False
list_a.sort()
for i in range(len(list_a)): print(list_a[i])

'''if __name__ == '__main__':
    a = 314e-2
    a += 1
    print(a,type(a))
    b = round(a)
    print(b,type(b))'''