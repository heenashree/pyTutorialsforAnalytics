
from time import sleep
print("Few operations on Dictionary\n")
print("###Update, Append, Access the Dictionary####\n")

dict_1 = {'Name':'Heenashree', 'Practice': 'CnD', 'Skills':'Python'}
dict_1['Exp'] = 8.5

dict_1.update({"Skills" : "Python and DevOps"})
print(dict_1)
dict_1.update(Skills='test')
dict_1['Name'] = 'Anita'

print(dict_1)

print(dict_1.get('Skills'))
print(dict_1['Skills'])
print(dict_1.get('Certs'))
#print(dict_1['Certs']) #Error


print("Dictionry deletion")
dict_1.pop('Skills') #pop a specific element
print(dict_1)

del dict_1['Name']
print(dict_1)

#del dict_1

print(dict_1.keys())
print(dict_1.values())
