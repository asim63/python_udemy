height = int(input("What is your height?: "))

if height >= 120:
    age = int(input("What is your age?: "))
    if age < 12:
        print("Sorry mate you cant go in.")
    elif age >=12 and age <= 18:
        print("$7 for you")
    else:
        print("$12 for you")
else:
    print("Why are you even here go away!!")