from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_machine_on = True
my_menu = Menu()
my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()

def get_choice():
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    
    return choice
    
while is_machine_on == True:
    choice = get_choice()
    item = my_menu.find_drink(choice)
    
    if choice == "report":
        my_coffee_maker.report()
    elif choice == "money":
        my_money_machine.report()   
    elif item:
        if my_coffee_maker.is_resource_sufficient(item):
            if my_money_machine.make_payment(item.cost):
                my_coffee_maker.make_coffee(item)
    else:
        is_machine_on = False
        print("bye!")
    
    