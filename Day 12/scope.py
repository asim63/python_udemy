a = 5
b = 8
def change():
    a = 6
    print(a)  #excesses only the 'a' inside the function
    print(f"b = {b}")
change()
b = 8
print(a) 
print(b)