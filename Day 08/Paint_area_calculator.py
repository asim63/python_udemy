import math
def no_of_cans(height,width,coverage):
    surface_area = height * width
    return surface_area/coverage

height = int(input("Enter the height of the wall: "))
width = int(input("Enter the width of the wall: "))
coverage = 5

cans = math.ceil(no_of_cans(height,width,coverage))
print(f"You'll need {cans} cans of paint.")