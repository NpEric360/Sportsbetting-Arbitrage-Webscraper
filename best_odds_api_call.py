import requests
import json


#Fetches all of the odds from the current games
#Key betting in each game:
#home_ml vs. away_ml
#home_spread_odds vs away_spread_odds; spread = __
#over_odds vs under_odds;  'total': 230.0

def betstamps_best_odds():
    url = "https://api.betstamp.app/api/best_available/?game_ids=[121867,121868,121869,121872,121871,121870,121873,121875,121874,121876,121877,121878,121879,121880,121881]&period=FT&"

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
    'If-Modified-Since': 'Sun, 19 Mar 2023 05:26:07 GMT',
    'TE': 'trailers'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    print(response)
    data = response.json()
    games = data.keys() #data is type dict
    return data, games

