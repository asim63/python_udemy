

# with open("Day 24/my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# with open("Day 24/my_file.txt",mode = 'w') as file:
#     file.write("i gotta do homeworks.")
    
# with open("Day 24/my_file.txt",mode = 'a') as file:
#     file.write("\nAppending")

#creates a new file by itself
with open(r"Day 24\new_file.txt", mode = 'a') as file:
    file.write("HEY")


#when the file is in desktop
with open(r"..\..\new_file.txt", mode = 'r') as file:
    contents = file.read()
    print(contents)