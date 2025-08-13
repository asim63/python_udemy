

import pandas as pd

df = pd.read_csv(r"Day 26\NATO_P~1.CSV")
# print(df)

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
NATO_dict = {row.letter : row.code for (index,row) in df.iterrows()}
# print(NATO_dict)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
input_word = input("Enter a word:").upper()
code_list = [NATO_dict[letter] for letter in input_word]

print(code_list)