import json
import yaml

testdict = 'hello 2020'

## Create files in python
f = open('templates\dummy1.json', 'a') #'w' will create a new file if it doesnt exist
f.write(testdict)
f.close()

testyaml = 'Hello there'
with open('templates\dummy2.yml', 'w') as file:
    file.write(testyaml)
'''
“ r “, for reading.
“ w “, for writing.
“ a “, for appending.
“ r+ “, for both reading and writing
'''




