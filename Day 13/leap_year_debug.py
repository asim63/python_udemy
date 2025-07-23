year = int(input("Which year do you want to check?: "))

if year%4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Its a leap year.")
        else:
            print("Its not a leap year.")
    else:
        print("Its a leap year.")
else:
    print("Its not a leap year.")