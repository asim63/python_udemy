import random
import os
from arts import logo
play = True
def check(guess):
        if guess == goal:
            print(f"You got it! The answer was {guess}")
            return False
        elif guess>goal:
            print("Too high.")
        elif guess<goal:
            print("Too low.")
        return True
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
while(play):
    clear_screen()
    print(logo)
    print("Welcome to the Number Guessing Game!!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    attempts = 5
    if difficulty == 'easy':
        attempts = 10

    game_not_over = True
    goal = random.randint(2,99)

    while(attempts != 0 and game_not_over):
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        attempts -= 1
        game_not_over = check(guess)
        
    if attempts == 0 and game_not_over == True:
        print("You've run out of guesses, you lose.")
        print(f"The number was {goal}")

    play = input("Do you wanna play the game again? Type 'y' or 'n': ")
    if play == 'n':
        print("\nThank you for playing the game. Goodbye. \n\n")
        play = False
