import pandas as pd
df = pd.read_csv(r"Day 30\NATO_P~1.CSV")

NATO_dict = {row.letter : row.code for (index,row) in df.iterrows()}
error = True
while(error):
    input_word = input("Enter a word:").upper()
    try:
        code_list = [NATO_dict[letter] for letter in input_word]
    except KeyError:
        print("Sorry, only letter in the alphabet please")
    else:
        error = False
        print(code_list)
