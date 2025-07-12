
age = int(input("What's your current age?: "))

days_max = 90*365
weeks_max = 52*90
months_max = 12*90

days_left = days_max - age * 365
weeks_left = weeks_max - age*52
months_left = months_max - age*12

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")
