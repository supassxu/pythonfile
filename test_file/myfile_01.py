# -*- coding:utf-8 -*-
import csv

with open('../file/a.csv', 'r') as f:
    a_csv = csv.reader(f)
    #print(list(a_csv))
    for row in a_csv:
        print(row)

with open('../file/ab.csv', 'w', encoding='utf-8') as f1:
    ab_csv = csv.writer(f1)
    c = [['ID', '姓名', '职业', '年龄'],['1001', '徐超超', '测试', '28']]
    ab_csv.writerows(c)
