array =[ 'a', 'ab', '1','2','3','4']
n = [1,2,3,4]
n.append([5,6])
n.extend([7,8])
print("len", len(n))
print('n', n)
for i in array:
    print(i)

print(len(array))
for i in range(len(array)):
    print(i)


for i in range(10):
    print(i)

for i in range(1,10,2):
    print(i)

'''
k = [i for i in array if i.isdigit()]
print(k)
'''