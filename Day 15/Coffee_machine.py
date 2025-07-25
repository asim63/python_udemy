from menu import MENU,resources
money = 0
def print_resources(amount):
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money :${amount}")


print_resources(money)
