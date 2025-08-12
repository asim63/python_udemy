with open(r"Day 26\file1.txt") as file1:
    file1_list = file1.readlines()

with open(r"Day 26/file2.txt") as file2:
    file2_list = file2.readlines()

file1_list = [int(n.strip()) for n in file1_list]
file2_list = [int(n.strip()) for n in file2_list]

file1_list.sort()
file2_list.sort()

result = [n for n in file1_list if n in file2_list]
print(result)