num = 0
while num < 10:
    print(num, end='\t')
    num += 1
    # time.sleep(0.5)

print('*************************************')
total = i = 0
print('total = ', end='')
while i < 100:
    total += i
    if (i != 99):
        print(str(i), end=' + ')
    else:
        print(str(i), end='')
    i += 1
print(' ={0}'.format(total))
print('*************************************')
for a in (10, 20, 30): print(a * 10)
for b in 'supassxu': print(b)
d = {'name': 'supassxu', 'age': 28, 'job': 'tester'}
for c in d: print(c)
for x in d.values(): print(x)
for x in d.items(): print(x)
