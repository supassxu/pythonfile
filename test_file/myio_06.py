import pickle

a1 = 'supassxu'
a2 = 110911043
a3 = [10, 20, 50]
with open(r'e:\data.dat','wb') as f:

    pickle.dump(a1,f)
    pickle.dump(a2,f)
    pickle.dump(a3,f)

with open(r'e:\data.dat','rb') as f:
    b1 = pickle.load(f)
    b2 = pickle.load(f)
    b3 = pickle.load(f)
    print(b1)
    print(b2)
    print(b3)

print(id(a1))
print(id(b1))