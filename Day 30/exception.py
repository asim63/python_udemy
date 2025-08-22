
try:   
    file  = open("Day 30/a_file.txt")
    a = {"Key": "Value"}
    print(a["Key"])
except FileNotFoundError:
    file = open("Day 30/a_file.txt", mode = 'w')
    file.write("Something")
except KeyError as error:
    print(f"That key {error} does not exit")
else:
    content = file.read()
    print(content)