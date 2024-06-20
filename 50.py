a = ['hello', 'level', 'world', 'radar', 'python']
b=[]
for i in a:
    if i!=i[::-1]:
        b.append(i)
print(b)