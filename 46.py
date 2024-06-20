a = [[1, 2, [3, 4]], [5, [6, 7]], 8, [9]]
ans=[]
for i in a:
    if type(i)==list:
        for j in i:
            if type(j)==list:
                for s in j:
                    ans.append(s)
            else:
                ans.append(j)
    else:
        ans.append(i)
print(ans)

