sentence = "What is the Airspeed Velocity of an Unladen Swaflow?"

word_list = sentence.split()
print(word_list)


dictionary = {word : len(word) for word in word_list}
print(dictionary)