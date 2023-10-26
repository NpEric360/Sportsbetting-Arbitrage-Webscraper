def send_user_notification(surebets_list_dict):
    number_bets = len(surebets_list_dict)
    highest_profit = surebets_list_dict[0]['Profit']
    league = surebets_list_dict[0]['League']
    Teams = surebets_list_dict[0]['Teams']
    date = surebets_list_dict[0]['Date']
    odds = surebets_list_dict[0]['Odds']
    books = surebets_list_dict[0]['Books']
    staking_ratio = surebets_list_dict[0]['Staking_Ratio']

    message=("{} surebets were found. The highest profit is {}. The {} game is {} vs. {} at {}. The odds and respective staking ratio is: {}:{}({}) vs. {}:{}({})!".format(number_bets,highest_profit,league, Teams[0], Teams[1],date,books[0],odds[0],staking_ratio[0],books[1],odds[1],staking_ratio[1]))
    return message


from twilio.rest import Client


def send_notif(surebets_list_dict):
    account_sid = 'AC6d892587743c9ac53a1eadec0e7c5c71'
    auth_token = 'c060c16b2cfd8fe829f43e50c9234083'
    client = Client(account_sid, auth_token)

    surebet_message = send_user_notification(surebets_list_dict)

    message = client.messages.create(
    from_='+15077055495',
    body= surebet_message,
    to='+'
    )

    print(message.sid)