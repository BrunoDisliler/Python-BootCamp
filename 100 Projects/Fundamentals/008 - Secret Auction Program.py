from Modules import Hammer

print(Hammer.logo)
bids = {}
bidding_finished = False


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ''
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f'The winner is {winner} with a bid of ${highest_bid}.')


while not bidding_finished:
    name = str(input('What´s your name?: '))
    price = int(input('What´s your bid?: $'))
    bids[name] = price
    should_continue = str(input('Are there any other bidders: Type "yes" or "no": ').lower())
    if should_continue == 'no':
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == 'yes':
        print('\n' * 50)
