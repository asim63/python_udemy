import random
word_list = ["ardvark","baboon","camel"]
chosen_word = random.choice(word_list)

guess_letter = input("Guess a letter: ").lower()

for i in chosen_word:
    if( guess_letter == i):
        print("Right")
    else:
        print("Wrong")
    
