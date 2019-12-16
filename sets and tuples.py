
list1 = [1,1,2,1,3,1,5,6,7,4,5]
list2 = set(list1)
print(list2)
list3 = tuple(list1)
print(list3)
print(type(list3))  # --> tuple
print(type(list2))  # --> set

print(list3[0])
#list3[0] = 10
list1[0]= 10
print(list1)
#list3[0] = 10 # because list3 is a tuple --> this will not work
list3 = list(list3)
print(type(list3))
list3[0] = 10
print(list3)
list3 = tuple(list3)
print(type(list3))
k = ([1,2,34], 4,5,6,'hello')
print(k)
k[0][0]=1111
print(k)


print(id(k))
print(id(list3))
