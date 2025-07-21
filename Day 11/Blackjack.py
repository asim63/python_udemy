import random
from arts import logo
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10] 
length = len(cards)
play = True

while(play):
    your_cards = []
    computer_cards = []
    your_cards.append(cards[ random.randint(0,length-1)])
    your_cards.append(cards[ random.randint(0,length-1)]) 
    computer_cards.append(cards[ random.randint(0,length-1)])
    print(f"Your cards: {your_cards}")
    print(f"Computer's first hand card: {computer_cards[0]}")
    another_card = input("Type 'y' to get another card, type 'n' to pass: ")
    while another_card == 'y' :
        your_cards.append(cards[random.randint(0,length-1)])
        another_card = input("Type 'y' to get another card, type 'n' to pass: ")
    
    print(f"Your final hand: {your_cards}")
    
    total = sum(computer_cards)

    
    
    
    play = False
    