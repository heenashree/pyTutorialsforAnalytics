dict_1 = {'Name':'Heenashree', 'Practice': 'CnD', 'Skills':'Python'}
id1 = id(dict_1)
print(id(dict_1))
del dict_1

dict_2 = {'Name':'Heenashree', 'Practice': 'CnD', 'Skills':'Python'}
id2 = id(dict_2)
print(id2)
print(id1 == id2)
