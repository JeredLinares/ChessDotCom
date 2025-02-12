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
username = 'shiba_dad'      #TODO change to argv

# Basic Metrics
number_white_games = 0
number_black_games = 0
number_white_wins = 0
number_black_wins = 0
number_draws = 0
peak_rating = 0

# Advanced Metrics


# Internal functions


# Basic Functions

def add_game(game_data):
    if game_data['white']['username']==username:
        add_white_game(game_data['white'])
    else:
        add_black_game(game_data['black'])

def add_white_game(game):
    number_white_games += 1
    game_result = game['result']
    compare_max_rating(game['rating'])
    if game_result=='win':
        number_white_wins += 1
    if game_result=='repetition' or game_result=='timevsinsuficient':
        number_draws += 1

def add_black_game(game):
    number_black_games +=1
    game_result = game['result']
    compare_max_rating(game['rating'])
    if game['result']=='win':
        number_black_wins +=1
    if game_result=='repetition' or game_result=='timevsinsuficient':
        number_draws += 1

def compare_max_rating(new_rating):
    if peak_rating < new_rating:
        peak_rating = new_rating



# Advanced Functions


# Load Data
with open(file_name,'r') as file:
    data_json = json.load(file)

# Run analysis
for element in data_json["games"]:
    add_game(element)

# Output Results
number_games_total = number_white_games + number_black_games
print(f"Number of games: {number_games_total}")
print(f"Games played as white: {number_white_games*1.0/number_games_total}")
print(f"Percent wins: {number_wins*1.0/number_games_total}")
print(f"Peak rating: {peak_rating}")








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


