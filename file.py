with open('player copy.csv','r') as f:
    data=f.read()
columns=data.split("\n")[0].split(",")
print(columns)
dict_player={}
for column in columns:
    dict_player[column]=[]
    for row in data.split("\n")[1:-1]:
        elements = row.split(",")
        count = 0
        for e in elements:
            dict_player[columns[count]].append(e)
            count += 1
            print(dict_player)