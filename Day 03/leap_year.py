print("Welcome to leap year checker!!\n")
year = int(input("Enter the year: "))
# if(year % 4 == 0 and year % 100 != 0) or (year % 4 == 0 and year % 400 == 0 ):
#     print("The year is a leap year.")
# else:
#     print("The year aint leap year mate.")


if year % 4 ==0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("It is a leap year.")
        else:
            print("It is not a leap year.")
    else:
        print("It is a leap year.")
else:
    print("Not a leap year.")