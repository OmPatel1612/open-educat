import csv
with open('player copy.csv','r') as f:
    player_data=csv.DictReader(f,delimiter=',')
    i = (str(input("enter country:")))
    j=0
    for rec in player_data:
        if rec['country']==i:
            j+=1
print("Number Of Players:",j)