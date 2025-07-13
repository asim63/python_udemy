print("Welcome to Pizza's Hub")
size = input("What size of Pizza would you like to have sir? Small, Medium, or Large ( Input S, M or L): ")
pep = input("Would you like to ad Pepperoni as well sir? (Enter Y or N): ")
cheese = input("And How about some extra cheese? (Enter Y or N ): ")
bill = 0
if(size == "S"):
    bill += 15
elif size == "M":
    bill += 20
elif size =="L":
    bill += 25
else:
    print("Invalid input.")

if(pep == "Y"):
    if size == "S":
        bill += 2
    else:
        bill += 3
if(cheese == "Y"):
    bill += 1
print(f"Your final bill is: ${bill}.")