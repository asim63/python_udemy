row1 = [" "," "," "]
row2 = [" "," "," "]
row3 = [" "," "," "]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = int(input("Where do you want to put your treasure?(specify two digit (row-column))"))

#for row-column operation
first_digit = int((position/10 -1))
last_digit = int((position%10 -1))

# row = map[first_digit]
# row[last_digit] = "X"


# print(f"{row1}\n{row2}\n{row3}")

#for column-row operation
row = map[last_digit]
row[first_digit] = "X"
print(f"{row1}\n{row2}\n{row3}")
