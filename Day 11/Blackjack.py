import random
from arts import logo
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10] 
length = len(cards)
play = True

def add_card_computer():
     """Adds a new card for computer"""
     computer_cards.append(random.choice(cards))

def add_card_user():
     """Adds a new card for user"""
     your_cards.append(random.choice(cards))

def display_result():
    """To compare the total sum of user_card and computers_card"""
    if total_your > total_computer or total_computer > 21 :
        print("You Win")
    elif total_your == total_computer:
        print("Its a draw")
    else:
        print("You lose")

def check_valid(total_your, another_card):
    """checks if the sum of cards is less than 17"""
    if total_your < 17 and another_card == 'n':
        print("The sum is less than 17 you must have more card.")
        return 'y'
    elif another_card == 'y':
        return 'y'
    else:
        return 'n'

def check_ace(total_your,your_cards):
    """Checks if the ace should be 11 or 1"""
    if 11 in your_cards and total_your > 21:
        your_cards.remove(11)
        your_cards.append(1)
        total_your = sum(your_cards)

def is_game_over(total_your,your_cards):
    """Check for BlackJack"""
    if total_your == 21 and len(your_cards) ==2:
        return True

game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if not game == 'y':
        play = False 

while(play):
    print(logo)
    your_cards = []
    computer_cards = []

    for i in range(2):
        add_card_user()
        add_card_computer()
        
    total_your = sum(your_cards)
    total_computer = sum(computer_cards)
    check_ace(total_your,your_cards)
    print(f"Your cards: {your_cards}, current score: {total_your}")
    print(f"Computer's first hand card: {computer_cards[0]}")
    
    
    if (is_game_over(total_your,your_cards)):
        print("Woahhh!! BlackJack . You win the game.")
        
    else:
        another_card = input("\nType 'y' to get another card, type 'n' to pass: ")
        another_card = check_valid(total_your, another_card)
        while another_card == 'y' :
            add_card_user()
            total_your = sum(your_cards)
            check_ace(total_your,your_cards)
            print(f"Your cards: {your_cards}, current score: {total_your}")

            another_card = input("\nType 'y' to get another card, type 'n' to pass: ")
            total_your = sum(your_cards)
            another_card = check_valid(total_your, another_card)
            
        if total_your > 21:

            print(f"Your final hand: {your_cards}, final score: {total_your}")
            print(f"Computer's final hand: {computer_cards}, final score: {total_computer} ")
            print("Oops!! Greater than 21. You Lose.\n")
    
        else:
            total_computer = sum(computer_cards)
            while total_computer < 17 :
                add_card_computer()
                total_computer = sum(computer_cards)
            
            if total_computer < 21:
                random_integer = random.randint(0,5)
                if random_integer == 4:
                    add_card_computer()
                    total_computer = sum(computer_cards)
                    
            print(f"Your final hand: {your_cards}, final score: {total_your}")
            print(f"Computer's final hand: {computer_cards}, final score: {total_computer}")       

            display_result()

    game = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': \n")
    
    if not game == 'y':
        play = False
    