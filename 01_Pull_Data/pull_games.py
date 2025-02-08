'''
Pull Games from Chess.com
JD Linares
2025 02 07
'''

import readline
import requests
import json

year = "2025"
month = "02"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
url="https://api.chess.com/pub/player/Shiba_dad/games/2025/01"
data = requests.get(url,headers=headers)
data_j = data.json()

filename = "JD_Games_"+year+"_"+month+".json"


with open(filename,'w') as json_file:
    json.dump(data_j,json_file,indent=4)

print("File Written")





'''
data = requests.get("https://api.chess.com/pub/player/Shiba_dad")
data = requests.get("https://api.chess.com/pub/player/Shiba_dad",headers=headers)
'''


