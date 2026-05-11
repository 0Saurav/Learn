# Secret Auction: Highest bidder wins, First come first win in event of tie
# Secret Auction

print("Welcome to Secret Auction.")
def maximum_bid(bidders):
    maximum_bid = 0
    for bidder in bidders:
        if bidders[bidder] > maximum_bid:
            maximum_bid = bidders[bidder]    
    return maximum_bid

def who_won(bidders, maximum_bid):
    winner = {}
    for key in bidders:
        if bidders[key] == maximum_bid:
            winner[key] = maximum_bid
    for key, value in winner.items():
        return key, value


bidders = {}


bid_on = True
while bid_on:
    bidder = str(input("What is your name: "))
    bid_amount = float(input("How much you want to bid: $ "))

    bidders[bidder] = bid_amount
    more_bidders = str(input("Is there any more bidder. Type 'yes' or 'no': ")).lower()
    if more_bidders == 'yes':
        bid_on = True
    elif more_bidders == 'no':
        bid_on = False
    else:
        print("Please enter a valid choice")



maximum_bid = maximum_bid(bidders)

winner, amount = who_won(bidders, maximum_bid)

print(f"{winner} won the auction with $ {amount}.")