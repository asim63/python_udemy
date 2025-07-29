print("Welcome to Love Calculator!!")
name1 = input("What is your name?: ")
name2 = input("What is their name?: ")

lower_case_name1 = name1.lower()
lower_case_name2 = name2.lower()

l = lower_case_name1.count("l") + lower_case_name2.count("l")
o = lower_case_name1.count("o") + lower_case_name2.count("o")
v = lower_case_name1.count("v") + lower_case_name2.count("v")
e = lower_case_name1.count("e") + lower_case_name2.count("e")
t = lower_case_name1.count("t") + lower_case_name2.count("t")
r = lower_case_name1.count("r") + lower_case_name2.count("r")
u = lower_case_name1.count("u") + lower_case_name2.count("u")

f_digit = str(t+r+u+e)
l_digit = str(l+o+v+e)
# print(l)
# print(o)
# print(v)
# print(e)
# print(f_digit)
# print(l_digit)
result = f_digit + l_digit
result = int(result)
if result < 10 or result > 90:
    print(f"Your score is {result}, you go together like coke and mentos.")
elif result > 40 and result < 50:
    print(f"Your score is {result}, you are alright together.")
else:
    print(f"Your score is {result}.")