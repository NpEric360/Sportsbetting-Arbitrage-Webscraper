# Sportsbetting-Arbitrage

Sportsbetting arbitrage occurs when two different sportsbooks post differing odds for the same game. A discrepancy in the odds between these two books can be taken
advantage of to give you a guaranteed profit regardless of the outcome of the game.

An example of this occurring:

Sportsbook 1:
Outcome 1 Odds = 1.26
Outcome 2 Odds = 4.95

Sportsbook 2:
Outcome 1 Odds = 1.23
Outcome 2 Odds = 5.00

There is a discrepancy in odds between these two sportsbooks such that if you:
BET $1 on Sportsbook1 on Outcome 1 @ 1.26
BET $0.25 on Sportsbook2 on Outcome 2 @ 5.00

You will net 0.8% regardless of the outcome. The profit margins on this strategy is extremely low, so I am just doing this as a fun way to practice API calling, 
data structure manipulation, and twillio SMS notifications. I am not advocating for gambling. I always wanted to learn about arbitrage and found this to be much easier
than crypto/stock arbitrage.

Discrepancies occur when the sum of (1/Odd1) and (1/Odd2) is less than 1 (or 100%) meaning that the combined odds do not add up to 100%!
Stakes are calculated by:
1. Set stake on outcome A to be reference; i.e. $1
2. Stake B = StakeA * (Odds of Outcome 1/Odds of Outcome 2)
Profit = Winnings/Total amount staked.
