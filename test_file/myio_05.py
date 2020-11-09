with open('../file/b.txt', 'r', encoding='utf-8') as f:
    print('文件名是：{0}'.format(f.name))
    print(f.tell())
    print('读取的内容是：{0}'.format(f.readline()))
    f.seek(10)
    print(f.tell())
    print('读取的内容是：{0}'.format(f.readline()))
    print(f.tell())
    #lines = f.readlines()
    #lines = [line.rstrip() + '#' + str(index + 1) + '\n' for index,line in enumerate(lines)]