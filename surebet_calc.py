#Surebet calculation

#This function determines if there is a discreprency in the best available odds; will return the profit, odds, and bet staking ratio if there a sure bet exists
def surebet(odds):
    odd1 = odds[0]
    odd2 = odds[1]
    edge = round(1/odd1 + 1/odd2,3)
    
    #A guaranteed profit only exists if there is a mismatch of odds
    if (edge >0.0) and (edge < 1.0):
        
        profit = round(1-(1/odd1+1/odd2),4)
        #calculate stake ratio:
        stakeA = 1
        stakeB = round(stakeA*(odd1/odd2),2)
        stake_ratio = [stakeA,stakeB]
       #print("stake ratio is {}:{} given that Odd1 = {}, and Odd2 = {}".format(stakeA,stakeB,odd1,odd2))
        return profit,odds,stake_ratio
    else:
        return None