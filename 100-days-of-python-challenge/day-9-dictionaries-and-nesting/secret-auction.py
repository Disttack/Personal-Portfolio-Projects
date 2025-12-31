print('Welcome to the secret auction!')

name = input("What is your name?: ")
bid = int(input("What is your bid?: $"))
bids = {}
bids[name] = bid

should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

while should_continue == 'yes':
    print('\n' * 50)  # Clear the screen by printing new lines
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bids[name] = bid
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

    if should_continue == 'no':
        print('\n' * 50)  # Clear the screen by printing new lines
        highest_bid = 0
        for name in bids:
            bid_amount = bids[name]
            if bid_amount > highest_bid:
                highest_bid = bid_amount
                winner = name

    else:
        print("Invalid input. Please type 'yes' or 'no'.")

    print(f"The winner is {winner} with a bid of ${highest_bid}.")