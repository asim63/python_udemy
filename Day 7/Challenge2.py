import random
word_list = ["ardvark","baboon","camel"]
chosen_word = random.choice(word_list)
print(f"THe word is {chosen_word}")
guess_letter = input("Guess a letter: ").lower()


display = []
for i in chosen_word:
    display.append('_')

for i in range(0,len(chosen_word)):
    if chosen_word[i] == guess_letter:
        display[i] = guess_letter

print(display)