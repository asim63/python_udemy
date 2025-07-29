#Step 4

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["ardvark","baboon","camel"]
chosen_word = random.choice(word_list)
print(f"THe word is {chosen_word}")
result = True
display = []
lives = 6
count = 0
for i in chosen_word:
    display.append('_')

while(result):
    guess_letter = input("Guess a letter: ").lower()
    count = 0
    for i in range(0,len(chosen_word)):
        if chosen_word[i] == guess_letter:
            display[i] = guess_letter
        else:
            count += 1

    if count == len(chosen_word):
        lives -= 1
    print(f"{' '.join(display)}")

    
    if lives == 0:
        result = False
        print(stages[0])
        print(f"You lose. The word was {chosen_word}")

    elif '_' in display:
        result = True
        print(stages[lives])

    else:
        result = False
        print("You Win")

