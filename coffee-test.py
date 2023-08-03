from menu import Menu

my_menu = Menu()

is_machine_on = True
while is_machine_on == True:
    choice = input("What would you like?").lower()

    if my_menu.find_drink(choice):
        print("yes")
    else:
        print("no")