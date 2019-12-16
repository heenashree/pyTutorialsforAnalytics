l = ['A','B','C','D','E']
j = [1,2,3,4,5]
print (zip(l,j))

for k, v in zip(l,j):
    print (k,v)

test = {k:v for k,v in zip(j,l)}
print(test)


test2 = {i:i*i*i for i in [1,2,3,4,5,6,7,8]}
print(test2)

#Make another dictionary from existing
test3 = {i:j for i,j in test2.items() if j%2==0}
print(test3)

