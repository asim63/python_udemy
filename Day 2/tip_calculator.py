print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

bill += ((tip/100)*bill)
pay_each = round(bill/people, 2)
pay_each = "{:.2f}".format(bill/people)
message = f"Each person should pay: ${pay_each}"
print(message)