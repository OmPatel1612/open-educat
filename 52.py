a= [{'name': 'John', 'age': 20, 'grades': [85, 90, 88]}, {'name': 'Alice', 'age': 22,
'grades': [78, 85, 92]}]
for i in a:
    temp=(sum(i["grades"])/len(i))
    i.update({"avg_grade":temp})
print(a)