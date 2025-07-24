import random
import os
from art import logo,vs
from game_data import data
game_is_over = False
score = 0
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear' )

def calculate(guess,A,B):
    followers_A = int(A['follower_count'])
    followers_B = int(B['follower_count'])

    if (guess == 'A' and followers_A >= followers_B) or (guess == 'B' and followers_B >= followers_A):
        return 1
    else:
        return 2
    
a = random.choice(data)
while(not game_is_over):
    print(logo)
    if score > 0:
        print(f"You're right! Current Score: {score}")

    b = random.choice(data)

    while(b['follower_count'] == a['follower_count']):
        b = random.choice(data)

    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']} ")
    print(f"A_followers = {a['follower_count']}")
    print(vs)
    
    print(f"Against B: {b['name']}, a {b['description']}, from {b['country']} ")
    print(f"B_followers = {b['follower_count']}")
    choose = input("Who has more followers? Type 'A' or 'B': ")
    clear_screen()

    if calculate(choose,a,b) == 1:
        score += 1
        a = b 
    else:
        game_is_over = True
        print(f"Sorry, you are wrong. Your final score is : {score}.")
    