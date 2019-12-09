# Declare list
list1 = []
list2 = [1,2,3,4,5,6,7,8,9]
print(list2[0])
print(list2[5])

print(list2[2:])

print(list2[1:2])
print("even numbers", list2[1:4:2])

print(list2[-1])

print("reverse the string,", list2[::-1])

list3 = ['heena', 12, 13.4] # a list can have different data types
print(type(list3[0]))
print(type(list3))
print(type(list3[2]))
list4 = [list2, list3]

print(list4)
print(list4[0])
list3.append('khandewal')  #append at the end of the list
print(list3)
list3.insert(3, 'hello') #insert(index, object)
print(list3)

list3.remove(13.4) #deletes object
print(list3)

list3.pop(1) #this will take index to delete the object

print(list3)

list3.pop()  #without index removes the last element
print(list3)

del list2[2:]  #delete multiple values at the same time
print(list2)

list2.extend([3,4,5]) #to add multiple values
print(list2)
print(min(list2))
print(sum(list2))

list2.extend([10,50,20])
print(list2)

list2.sort()  #this has sorted the list
print(list2)

list2.sort(reverse=True)
print(list2)