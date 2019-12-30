import yaml
with open('templates\yamldata.yml','r') as f:
    list_data = yaml.load(f, Loader=yaml.FullLoader)
print(list_data)

for k, v in list_data.items():
    print("key", k, "and value", v)


# write into the file
dict_file = [{'sports' : ['soccer', 'football', 'basketball', 'cricket', 'hockey', 'table tennis']},
{'countries' : ['Pakistan', 'USA', 'India', 'China', 'Germany', 'France', 'Spain']}]

with open('templates\yamldata1.yml', 'a') as f:
    yaml.dump(dict_file, f)


## remove the file
import os
if os.path.exists("templates\demofile.txt"):
  os.remove("templates\demofile.txt")
else:
  print("The file does not exist")
