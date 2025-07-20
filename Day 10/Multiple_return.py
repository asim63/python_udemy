def multiple_return(name,age):
    if name == "" or age < 0:
        return "Invalid"
    return f"Name : {name} and age: {age}"

print(multiple_return(input("What is the name?: "),int(input("What is the age?:"))))