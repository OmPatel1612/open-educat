a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
b=list()

for i in a:
    if i%2==0:
        b.append(i)

b=tuple(b)
print(b)