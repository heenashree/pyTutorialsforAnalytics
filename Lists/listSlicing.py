k=[]
list_=[]
mlist = [1,[2,3], 4, [5,6,[7,11]]]
with open('stats') as f:
    data = f.read()


for j, i in enumerate(data.split('\n')):
    print (j,i)
    k = i.split()
    print("k is", k)

for i in data.split('\n'):
    list_.append(i)
print("our compiled list", list_)
print(list_[7])
print(list_[1:3])
print(list_[1:8:2])
print(list_[::-1]) #reverse
print(list_[-3])
print(list_[-8:-1:2]) #list slicing from 8th to last element with step 2
print(list_[:-6])# list slicing till 6th element from last

print(mlist)
print(mlist[1])
print(mlist[1][1])
print(mlist[3][2][1])







