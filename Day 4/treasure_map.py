row1 = [" "," "," "]
row2 = [" "," "," "]
row3 = [" "," "," "]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = int(input("Where do you want to put your treasure?(specify two digit (row-column))"))
first_digit = int((position/10))
last_digit = int((position%10))

#for row-column operation
# row = map[first_digit-1]
# row[last_digit-1] = "X"
# print(f"{row1}\n{row2}\n{row3}")

#for column-row operation
row = map[last_digit-1]
row[first_digit-1] = "X"
print(f"{row1}\n{row2}\n{row3}")
