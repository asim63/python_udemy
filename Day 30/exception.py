
# try:   
#     file  = open("Day 30/a_file.txt")
#     a = {"Key": "Value"}
#     print(a["Key"])
# except FileNotFoundError:
#     file = open("Day 30/a_file.txt", mode = 'w')
#     file.write("Something")
# except KeyError as error:
#     print(f"That key {error} does not exit")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("This is an error that i made up...")
   
 
height = float(input("HEight: "))
weight = int(input("weight = "))

if height > 3 :
    raise ValueError("Height cant be that long.")
if weight > 140:
    raise ValueError("Weight that big?? ")
bmi = weight /height **2
print(bmi)
