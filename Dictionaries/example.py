import json
with open('example.json','r') as f:
    data=json.load(f)


print(data)
print(data['quiz'])

print(data.keys())
print(data.values())
print("\n")
print(data['quiz']['sport'])
print(data['quiz'].keys())
print("======================")
print(data.get('quiz').get('sport').get('q1', None))
print(data['quiz']['sport']['q1'].keys())
print(data['quiz']['sport']['q1'].values())
print(data.get('quiz').get('sport').get('q2', None))


# To change the keys
data['test']= {}
data['test']['test1'] = [1,2,3]
data['test']['test12'] = 'Hello'
#data['test']['test1']['test2']['test3']= [1,2,3]


print("line 25", data)



print(data['quiz']['sport']['q1']['question'])
data['quiz']['sport']['q1']['question'] = "Any name is good in NBA. Think not?"
print("====>", data)
data['quiz']['sport']['q1'].pop('question')
print(data)

data['quiz']['sport']['q1']['ask'] = "There is that question again?"
print(data)

with open('example1.json','w') as f:
    json.dump(data,f)