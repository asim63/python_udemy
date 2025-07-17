import random
from hangman_arts import logo, stages 
from hangman_words import word_list

chosen_word = random.choice(word_list)
print(logo)
print(f"Psssts. The word is {chosen_word}")
result = True
display = []
lives = 6
count = 0
for i in chosen_word:
    display.append('_')

while(result):

    guess_letter = input("Guess a letter: ").lower()
    count = 0 
    if guess_letter in display:
        print(f"{guess_letter}?. You have already guessed this word.")
        print(f"{' '.join(display)}")
    else:    
        for i in range(0,len(chosen_word)):
            if chosen_word[i] == guess_letter:
                    display[i] = guess_letter
            else:
                    count += 1 
        else:
            if count == len(chosen_word):
                print(f"{guess_letter} is not in the word. ")
                lives -= 1
        
            print(f"{' '.join(display)}")

        
        if lives == 0:
            result = False
            print(f"You lose. The word was {chosen_word}")

        if '_' not in display:
            result = False
            print("You Win")

    print(stages[lives])