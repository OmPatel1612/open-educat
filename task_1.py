
import csv
with open('player copy.csv','r') as f:
    player_data=csv.DictReader(f,delimiter=',')
    for rec in player_data:
        if rec['name'].startswith('a') or rec['name'].startswith('o'):
            print(rec)