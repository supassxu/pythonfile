names = ('supassxu','bingbing','zhenzhen','sansheng')
ages = (28,28,26,25)
jobs = ('tester','police','kuaiji','learner')
#c = zip(names,ages,jobs)
for name,age ,job in zip(names,ages,jobs):
	print('{0}--{1}--{2}'.format(name,age,job))
print('*************************************')
for i in range(4):
	print('{0}--{1}--{2}'.format(names[i],ages[i],jobs[i]))
