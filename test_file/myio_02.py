s = 'Hello ,my name is supassxu!\n welcome to file world!\nI love you,tanvwen!'
with open(r"../file/c.txt", "w", encoding='utf-8') as f1:
    f1.writelines(s)
with open(r"../file/b.txt", "r") as f2:
    print(f2.readlines())
with open(r"../file/b.txt", "r") as f3:
    for a in f3:
        print(a)
#print(f2.read())
#print(f1)