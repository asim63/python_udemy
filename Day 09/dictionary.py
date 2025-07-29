dictionary = {
    "Bug": "An error in a programt that prevents program from running as expected.",
    "sky": "Blue thing up above"
}

print(dictionary['sky'])

dictionary["loop"] = "Doing something again and again"

print(dictionary)

#Create an empty dictionary
empty_dictionary = {}

#wipe an existing dictionary
# dictionary = {}

#edit and existing dictionary
dictionary["Bug"] = "a moth in computer."
print(dictionary)

#loop
for i in dictionary:
    print(i)
    print(dictionary[i])