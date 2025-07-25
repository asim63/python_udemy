from menu import MENU,resources

# print(MENU['espresso']['ingredients']['water'])
def calculate_new_resources(user_input,resources):
    for key in MENU[user_input]['ingredients']:
        resources[key] -= MENU[user_input]['ingredients'][key]

print(resources)
calculate_new_resources('espresso',resources)
calculate_new_resources('espresso',resources)
print(resources)

print(MENU['latte']['cost'])