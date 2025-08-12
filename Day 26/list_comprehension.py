numbers = [1, 2, 3]

new_list = [n+1 for n in numbers]
print(new_list)

name = "Asim"
letter_list = [letter for letter in name]
print(letter_list)

number_list = [n*2 for n in range(1,5)]
print(number_list)

number_list = [n for n in range(1,10) if n % 3 ==0]
print(number_list)

names = ['Alex','Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

new_name = [name.upper() for name in names if len(name) > 5]
print(new_name)