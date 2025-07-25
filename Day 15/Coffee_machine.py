from menu import MENU,resources
from art import logo
import os

print(logo)
money = 0
def print_resources(amount):
    """Prints the status of the resources that are available."""
    amount = round(amount,2)
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money :${amount}")

def calculate_new_resources(user_input,resources):
    """Calculates the new value of the availabe resources."""
    for key in MENU[user_input]['ingredients']:
        resources[key] -= MENU[user_input]['ingredients'][key]

def check_if_enough(user_input,resources):
     """ Checks if the available resource is enough to make the product."""
     for key in MENU[user_input]['ingredients']:
        if not resources[key] >= MENU[user_input]['ingredients'][key]:            
            print(f"Sorry there is not enough {key}.")
            return 1


def calculate_money():
    """Calculates the money given by user."""
    total = int(input("How many quarters?: "))*0.25
    total += int(input("How many dimes?: "))*0.1
    total += int(input("How many nickles?: "))*0.05  
    total += int(input("How many pennies?: "))*0.01
    return total

def clear_screen():
    """clears the screen"""
    os.system('cls' if os.name == 'nt' else 'clear')
validity = True
off = True
while(off):
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    
    if user_input == 'report':
        print_resources(money)
    elif user_input == 'off':
        off = False
    else:
        is_enough = check_if_enough(user_input,resources)
        if not is_enough == 1:
            print("Please insert Coins.")
            user_money = calculate_money()
            money += user_money
            if user_money >= MENU[user_input]['cost']:
                change = user_money - MENU[user_input]['cost']
                change = round(change,2)
                print(f"Here is ${change} change.")
                money -= change
            else:
                print("Sorry that's not enough money. Money refuded.")
                money -= user_money
                validity = False
            if(validity):
                calculate_new_resources(user_input,resources)
                print(f"Here is your {user_input}. Enjoy!")
    
    if off == False:
        print("CLosing the machine.....")
        clear_screen()
        
