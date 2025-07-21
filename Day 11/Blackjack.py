import random
from arts import logo
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10] 
length = len(cards)
play = True

def add_card_computer():
     """Adds a new card for computer"""
     computer_cards.append(cards[ random.randint(0,length-1)])

def add_card_user():
     """Adds a new card for user"""
     your_cards.append(cards[ random.randint(0,length-1)])

def display_result():
    """To compare the total sum of user_card and computers_card"""
while(play):
    your_cards = []
    computer_cards = []

    add_card_user()
    add_card_user()
    add_card_computer()

    print(f"Your cards: {your_cards}")
    print(f"Computer's first hand card: {computer_cards[0]}")

    add_card_computer()

    another_card = input("Type 'y' to get another card, type 'n' to pass: ")
    while another_card == 'y' :
        add_card_user()
        another_card = input("Type 'y' to get another card, type 'n' to pass: ")
        total_your = sum(your_cards)
        if total_your < 17 and another_card == 'n':
            print("The sum is less than 17 you must have more card.")
            another_card = 'y'
        
    if total_your > 21:

        print(f"Your final hand: {your_cards}")
        print(f"Computer's final hand: {computer_cards}")
        print("You Lose.")
   
    else:
        total_computer = sum(computer_cards)
        while total_computer < 17 :
            add_card_computer()
            total_computer = sum(computer_cards)
        
        if total_computer < 21:
            random_integer = random.randint(0,5)
            if random_integer == 4:
                add_card_computer()
        else:
                
            print(f"Your final hand: {your_cards}")
            print(f"Computer's final hand: {computer_cards}")
            print(f"You Win")
       
                 
        print(f"Your final hand: {your_cards}")
        print(f"Computer's final hand: {computer_cards}")       
        display_result()
    
    game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    
    if not game == 'y':
        play = False
    