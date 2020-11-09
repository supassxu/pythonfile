
try:
    f = open(r"../file/a.txt", "w")
    f.write('Hello ,my name is supassxu! welcome to file world!\n')
    f.write('你好，徐超超，早上好，欢迎来到python世界！')
except BaseException as e:
    print(e)
finally:
    f.close()
b = open(r"../file/a.txt", "r")
s = b.read()
b.close()
print(s)
