'''while True:
    a = input('请输入Q或q退出当前程序：')
    if(a.__eq__('q') or a=='Q'):
        print('程序循环结束，退出！')
        break
print(a)'''

salarySum=0
salarys = []
for i in range(4):
    s = input('请输入一共4位同事的薪资（按q或Q中途结束）：')
    if s.upper()=='Q':
        print('录入完成，退出')
        break
    if float(s)<0:
        continue
    salarys.append(float(s))
    salarySum += float(s)
else:
    print('您已经全部录入一共4位同事的薪资')
print('录入薪资：',salarys)
print('平均薪资{0}'.format(salarySum/4))