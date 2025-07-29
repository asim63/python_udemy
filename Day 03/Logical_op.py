height = int(input("What is your height?: "))

if height >= 120:
    age = int(input("What is your age?: "))
    if age < 12:
        print("Sorry mate you cant go in.")
    elif age <= 18:
        print("$7 for you")
    elif age > 45 and age < 55:
        print("No tickets for you . Have fun!!")
    else:
        print("$12 for you")
else:
    print("Why are you even here go away!!")