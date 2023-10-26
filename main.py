#Sportsbook Arbitrage:
from best_odds_api_call import betstamps_best_odds
from formatting import moneyline_surebet_formatting, spread_surebet_formatting, total_surebet_formatting
from surebet_calc import surebet
from game_data_api_call import game_ID_api, find_game_data
from send_user_notification import send_notif
#data contains the Odds data, games is the keys for the dictionary
data,games = betstamps_best_odds()


#Sure bets will be structured as:
#[[profit,game_id,bet_type,[books],[odds],[stakes]],]

list_surebets = []
#iterate through every game/key, and search through non-None odds, and will appends to list_surebets if there is a surebet
for i in games:
    x = 0
    #MONEYLINE
    if data[i]['home_ml'] != None or data[i]['away_ml'] != None:
        #call function to compare odds
        moneyline_odds = [data[i]['home_ml'],data[i]['away_ml']]
        #print(moneyline_odds)
        x = surebet(moneyline_odds)
        if x is not None:
            winning_entry = moneyline_surebet_formatting(i,x)
            list_surebets.append(winning_entry)

    #SPREADS
    if data[i]['home_spread_odds'] != None or data[i]['away_spread_odds'] != None:
        spread_odds = [data[i]['home_spread_odds'],data[i]['away_spread_odds']]

        x = surebet(spread_odds)
        if x is not None:
            winning_entry = spread_surebet_formatting(i,x)
            list_surebets.append(winning_entry)
    
    #GAME TOTALS
    if data[i]['over_odds'] != None or data[i]['under_odds'] != None:
        spread_odds = [data[i]['over_odds'],data[i]['under_odds']]
        x = surebet(spread_odds)
        if x is not None:
            winning_entry = total_surebet_formatting(i,x)
            list_surebets.append(winning_entry)


#Sort surebets by max profits
sorted_surebets = sorted(list_surebets, key=lambda x: x[0], reverse=True)

for i in range(len(sorted_surebets)):
    print("{}: ".format(i))
    print(list_surebets[i])



game_data = game_ID_api()

#Convert surebets nested lists to list of dictionaries
surebets_list_dict= [] #list of dictionaries
for i in (sorted_surebets):    
    dict1 = {"Profit": i[0],
            "Game_ID":str(i[1]),
            "Bet_Type":i[2],
            "Books":i[3],
            "Odds":i[4],
            "Staking_Ratio":i[5]}
    surebets_list_dict.append(dict1) 
    
#Retrieve the gameID's from surebets_list_dict for easier searching
surebets_gameID = []
for i in surebets_list_dict:
    surebets_gameID.append(int(i["Game_ID"]))


#Since the game data and the best odds are not found in the same API call, we must do this
#Loop through the game ID's, and search for the correspondign ID's in surebets list; then append the corresponding game data to surebets
#We want: league, team

for i in range(len(game_data)):
    gameID = game_data[i]['id']
    #iterate through the game ID's in the surebets 
    for j in range(len(surebets_gameID)):
        if gameID == surebets_gameID[j]: #Mathced the game data of the selected gameID in surebets

            #Find date,teams of current game selected from api call 2
            date, league, teams = find_game_data(i,game_data) #date, [home_team,away_team]
            #append game data to original surebets_list_dict
            surebets_list_dict[j]['Teams']=teams
            surebets_list_dict[j]['League']=league
            surebets_list_dict[j]['Date']=date
            
#Final message sent to user:
surebets_list_dict[0]

#send the user notification
send_notif(surebets_list_dict)