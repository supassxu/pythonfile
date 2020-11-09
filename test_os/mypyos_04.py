#coding=utf-8
#测试shutil模块的用法：复制、压缩

import shutil
import zipfile

#shutil.copyfile('a.csv','abc.txt')
#shutil.copytree('file/a','b')
#shutil.copytree('file','cfile',ignore=shutil.ignore_patterns('*.csv'))

#shutil.make_archive('b/abc','zip','file/a')
#z1 = zipfile.ZipFile('file.zip','w')
#z1.write('a.csv')
#z1.write('abc.txt')
#z1.close()

z2 = zipfile.ZipFile('file.zip','r')
z2.extractall('e:/dfile')
z2.close()