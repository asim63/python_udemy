import os
def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mult(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
operations = {
    "+": add,
    "-": sub,
    "*": mult,
    "/":div

}
def calculation():
    num1 = int(input("Whats the first number: "))
    y = True

    print("Here are the operations:")
    for i in operations:
        print(i)
    while(y):
        symbol = input("Pick an operation from the line above: ")
        num2 = int(input("Whats the next number: "))
        calculation_function = operations[symbol]
        answer = calculation_function(num1,num2)

        print(f"{num1} {symbol} {num2} = {answer}")
        action = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start new calculation: ")

        if(action == 'y'):
            num1 = answer
        else:
            y = False
            clear_screen()
            calculation()

calculation()