import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
hand = [rock,paper,scissors]
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
comp = random.randint(0,2)

if user>2 or user<0:
    print("Invalid . You lose")
else:
    print(f"{hand[user]}")

    print("Computer Chose:")
    print(f"{hand[comp]}")

    if(user == comp):
        print("It's a draw")
    elif(user == 0 and comp == 1):
        print("You lose")
    elif(user == 0 and comp == 2):
        print("You win")
    elif(user == 1 and comp == 0):
        print("You win")
    elif(user == 1 and comp == 2):
        print("You lose")
    elif(user == 2 and comp == 1):
        print("You win")
    else:
        print("You lose")
