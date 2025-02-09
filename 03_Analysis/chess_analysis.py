'''
Analysis of a set of chess games 
Assumes data is downloaded from Chess.com
Prameters: python chess_analysis.py <username> <json file>

JD Linares
2025 02 09
'''


import json
import sys

file_name = sys.argv[1]
data_json = None

with open(file_name,'r') as file:
    data_json = json.load(file)
'''
# Inspect data elements
print(json.dumps(data_json['games'][0],indent=2))
print()
print()

print(json.dumps(data_json['games'][0]['white'],indent=2))
print(json.dumps(data_json['games'][0]['white']['username'],indent=2))
print()
print(json.dumps(data_json['games'][0]['black'],indent=2))
print(json.dumps(data_json['games'][0]['white']['username'],indent=2))
'''

number_games = 0
number_wins = 0

for element in data_json["games"]:
    number_games += 1
    if element['white']['username']=='shiba_dad':
        if element['white']['result']=='win':
            number_wins += 1
    else:
        if element['black']['result']=='win':
            number_wins += 1
            
print(f"Number of games: {number_games}")
print(f"Percent wins: {number_wins*1.0/number_games}")



