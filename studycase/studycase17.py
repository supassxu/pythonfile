#Python 练习实例17:输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

s = input("请输入一行字符串，我们将分别统计出其中英文字母、空格、数字和其它字符的个数：")
a = b = c = d = 0
for i in range(len(s)):
    if(s[i].isalpha()):
        a += 1
    elif(s[i].isspace()):
        b += 1
    elif(s[i].isalnum()):
        c += 1
    else:
        d += 1
print('英文字母数为：%d，空格数为：%d，数字数为：%d，其他字符数为：%d' % (a,b,c,d))