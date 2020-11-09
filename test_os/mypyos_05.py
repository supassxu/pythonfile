#coding=utf-8
#递归遍历打印所有的目录和文件

import os

allfiles = []
def getAllFiles(path,level):
    childFiles = os.listdir(path)
    for file in childFiles:
        filepath = os.path.join(path,file)
        if os.path.isdir(filepath):
            getAllFiles(filepath,level+1)
        #print('\t'*level + filepath)
        allfiles.append('\t'*level + filepath)
getAllFiles('', 0)

for f in allfiles:
    print(f)