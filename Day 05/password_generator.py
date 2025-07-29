import random
letters = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z',
    'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = [
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
    ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~'
]

print("Welcome to the PyPassword Generator")
l = int(input("How many letters would you like in your password?: "))
s = int(input("How many symbols would you like?: "))
n = int(input("How many numbers would you like?: "))
result= ""
# for i in range(0,l):
#         result += random.choice(letters)
# for i in range(0,n):
#         result += random.choice(numbers)
# for i in range(0,s):
#         result += random.choice(numbers)

# print(result)


password_list = []
for i in range(0,l):
        password_list.append(random.choice(letters))
for i in range(0,n):
       password_list.append(random.choice(numbers))
for i in range(0,s):
        password_list.append(random.choice(symbols))

random_number = 0
password = ""
length = len(password_list)
random.shuffle(password_list)
for i in password_list:
        password += i
print(f"Here is your password: {password}")