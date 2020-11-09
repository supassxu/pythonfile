with open('../file/b.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    lines = [line.rstrip() + '#' + str(index + 1) + '\n' for index,line in enumerate(lines)]
with open('../file/c.txt', 'w', encoding='utf-8') as f:
    f.writelines(lines)