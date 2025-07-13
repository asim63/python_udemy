weight = float(input("Enter your weight(in kgs): "))
height = float(input("What is you height(in m): "))

BMI = weight/(height**2)
print(f"Your BMI is {round(BMI,2)}")

if BMI <= 18.5:
    print("You're Underweight.")
elif BMI <= 25:
    print("You have a normal weight")
elif BMI <= 30:
    print("You are overweight")
elif BMI < 35:
    print("You are obese")
else:
    print("You are clinically obese")