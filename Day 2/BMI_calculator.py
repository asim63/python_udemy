weight = int(input("What's your weight in kgs?: "))
height = float(input("What's your height in meters?: "))

# print(type(weight))
# print(type(height))

BMI = weight / (height**2)
BMI = int(BMI)
print(BMI)