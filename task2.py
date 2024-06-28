import csv
with open('player copy.csv','r') as f:
    player_data=csv.DictReader(f,delimiter=',')
    i = (int(input("enter runs:")))
    for rec in player_data:
        if int(rec['total runs'])>i:
            print(rec)