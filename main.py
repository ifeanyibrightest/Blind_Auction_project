gavel = r""""
___________
                        \         /
                         )_______(
                         |"""""""|_.-._,.---------.,_.-._
                         |       | | |               | | ''-.
                         |       |_| |_             _| |_..-'
                         |_______| '-' `'---------'` '-'
                         )"""""""(
                        /_________\
                        `'-------'`
"""
print(gavel)

def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        amount = bidding_dictionary[bidder]
        if amount > highest_bid:
            highest_bid = amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")

bids = {}
continue_bidding = True
while continue_bidding:
    usr_name = str(input("what is your name?: "))
    price = int(input("what is your bid?:  $"))
    bidders = str(input("Are there any other bidders? Type 'Yes' or 'NO' "))
    bids[usr_name] = price
    should_continue = input("Are their any other bidders? 'Yes' or 'No'\n").lower()
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 30)


