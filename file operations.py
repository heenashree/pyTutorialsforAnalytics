testdict = 'hello 2020\n'

## Create files in python
f = open('templates\dummy1.json', 'w') #'w' will create a new file if it doesnt exist
f.write(testdict)
f.write('Hello there\n')
f.close()


testyaml = 'Hello there\nHow is it going'
with open('templates\dummy2.yml', 'w') as file:
    file.write(testyaml)

    
'''
'r'	Open a file for reading. (default)
'w'	Open a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
'x'	Open a file for exclusive creation. If the file already exists, the operation fails.
'a'	Open for appending at the end of the file without truncating it. Creates a new file if it does not exist.
't'	Open in text mode. (default)
'b'	Open in binary mode.
'+'	Open a file for updating (reading and writing) 
'''


with open('templates\dummy2.yml', 'r') as file:
    k = file.read(30)
    print(k)
    file.seek(10)

    print(file.readline())
    print(file.readline())
    file.seek(0)

    print(file.readlines())


#https://www.programiz.com/python-programming/file-operation



