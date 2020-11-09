
with open('../file/a.jpeg', 'rb') as f:
    with open('../file/abc.jpeg', 'wb') as g:
        for line in f.readlines():
            g.write(line)
print('图片打印完成！')