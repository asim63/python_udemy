def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mult(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2

operations = {
    "+": add,
    "-": sub,
    "*": mult,
    "/":div

}
num1 = int(input("Whats the first number: "))
print("Here are the operations:")
for i in operations:
    print(i)

symbol = input("Pick an operation from the line above: ")
num2 = int(input("Whats the second number: "))
answer = operations[symbol](num1,num2)

print(f"{num1} {symbol} {num2} = {answer}")