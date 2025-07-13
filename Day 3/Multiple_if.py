height = int(input("What is your height?: "))

if height >= 120:
    age = int(input("What is your age?: "))
    if age < 12:
        bill = 5
        print("$5 for kids")
    elif age <= 18:
        bill = 7
        print("$7 for teen")
    else:
        bill = 12
        print("$12 for adult")

    wants_photo = input("Do you want a picture as well? Enter Y or N:")
    if(wants_photo == "Y"or"y"):
        bill += 3
    
    print(f"Your final bill is {bill}")

    
else:
    print("Why are you even here go away!!")