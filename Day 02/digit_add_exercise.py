number = input("Input a 2 digit number:")

new_number = str(number)
first_digit = new_number[0]
second_digit = new_number[-1]

print(int(first_digit) + int(second_digit))