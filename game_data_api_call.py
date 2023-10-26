#API CALL 2
#Fetching game ID's: league, games
#Convert surebet's game ID's to see game, below can call to see the home and away teams, nba/nhl etc
import requests
import json


def game_ID_api():
    url = "https://api.betstamp.app/api/games/refresh/?game_ids=[121867,121868,121869,121872,121871,121870,121873,121875,121874,121876,121877,121878,121879,121880,121881]&"

    payload={}
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0',
    'Accept': '*/*',
    'Accept-Language': 'en-GB,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'PLATFORM': 'web',
    'Content-Type': 'application/json',
    'Authorization': 'Token 278c8cc04effb9ebb8dcdb47b4029f5d8657b75075039278ab4429518f572adb',
    'Origin': 'https://betstamp.app',
    'Connection': 'keep-alive',
    'Referer': 'https://betstamp.app/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'If-Modified-Since': 'Sun, 19 Mar 2023 06:23:17 GMT',
    'TE': 'trailers'
    }

    game_type_ID_status = requests.request("GET", url, headers=headers, data=payload)

    game_data = game_type_ID_status.json()
    return game_data


#This function finds the date and team names of a given game in game_data
def find_game_data(current_index,game_data):
    game=current_index
    game_data[game]
    
    #Retrieve date, team names
    date = game_data[game]['date']
    league = game_data[game]['league']
    home_team = game_data[game]['home_team']['full_name']
    away_team = game_data[game]['away_team']['full_name']
    
    print(home_team,away_team)
    return date, league, [home_team,away_team]