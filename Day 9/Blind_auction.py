import os
from art import logo

print(logo) 
bidder_info ={}
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def add_info(name,bid_amount):
    bidder_info[name] = bid_amount 

other_user = True
while(other_user):
    name = input("Enter your name: ")
    bid = int(input("What is your bid? :$"))
    add_info(name , bid)

    ask_user = input("Are there more bidders? (Yes or No):")
    if ask_user == 'Yes':
        other_user = True
        clear_screen()
    else:
        other_user = False
list = []
highest_bidder = ''
for key in bidder_info:
    list.append(bidder_info[key])
highest_bid = max(list)
for key in bidder_info:
    if bidder_info[key] == highest_bid:
        highest_bidder = key

print(bidder_info)
print(f"The highest bidder is {highest_bidder}, with ${highest_bid} as the bid.")



