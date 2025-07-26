from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
on = True
coffee_machine = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()




while(on):
    options = menu.get_items()
    choice = input(f"What would you like ? ({options}): ")
    if choice == 'off':
        on = False
    elif choice == 'report':
        coffee_machine.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if(coffee_machine.is_resource_sufficient(drink)):
            if(money_machine.make_payment(drink.cost) ):
                coffee_machine.make_coffee(drink)