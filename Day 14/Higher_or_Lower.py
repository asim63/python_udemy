import random
import os
from art import logo,vs
from game_data import data
game_is_over = False

yes = True
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear' )

def calculate(guess,A,B):
    followers_A = int(A['follower_count'])
    followers_B = int(B['follower_count'])

    if (guess =='a' and followers_A >= followers_B) or (guess =='b' and followers_B >= followers_A):
        return 1
    else:
        return 2
while(yes):
    score = 0
    print(logo)  
    a = random.choice(data)
    while(not game_is_over):

        if score > 0:
            print(f"You're right! Current Score: {score}")

        b = random.choice(data)

        while(b == a):
            b = random.choice(data)

        print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']} ")
        # print(f"A_followers = {a['follower_count']}")
        print(vs)
        
        print(f"Against B: {b['name']}, a {b['description']}, from {b['country']} ")
        # print(f"B_followers = {b['follower_count']}")
        choose = input("Who has more followers? Type 'A' or 'B': ").lower()
        clear_screen()
        print(logo)
        if calculate(choose,a,b) == 1:
            score += 1
            a = b 
        else:
            game_is_over = True
            print(f"Sorry, that's wrong. Final Score : {score}.")

    game_is_over = False
    again = input("Do you want to play the game once again? Type 'y' or 'n': ").lower()
    if not again == 'y':
        yes = False
    clear_screen()
