dic = {'apple': 2.5, 'banana': 1.75, 'orange': 3.0, 'mango': 12.5, 'grapes': 8.0}
ans = {}
for key, value in dic.items():
    if value>5:
        ans.update({key:value})
print(ans)
