#function formats the winning entry that will be appended to surebets
def moneyline_surebet_formatting(data,gameID,surebet_return):
    x = surebet_return
    book1 = (data[gameID]['home_ml_book']['name'])
    book2 = (data[gameID]['away_ml_book']['name'])
    winning_entry = [x[0],gameID,"Moneyline",[book1,book2],x[1],x[2]]
    return winning_entry


def spread_surebet_formatting(data,gameID, surebet_return):
    x = surebet_return
    book1 = (data[gameID]['home_spread_book']['name'])
    book2 = (data[gameID]['away_spread_book']['name'])
    winning_entry = [x[0],gameID,"Spread",[book1,book2],x[1],x[2]]
    return winning_entry

def total_surebet_formatting(data, gameID, surebet_return):
    x = surebet_return
    book1 = (data[gameID]['over_book']['name'])
    book2 = (data[gameID]['under_book']['name'])
    winning_entry = [x[0],gameID,"Total",[book1,book2],x[1],x[2]]
    return winning_entry