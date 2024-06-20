dic = [('John', 85), ('Alice', 92), ('Bob', 78)]
dic.sort(key=lambda a: a[1],reverse=True)
print(dic)