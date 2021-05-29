# Program that operates a coffee machine

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu() # Object being created from the module above
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True # Variable created for structure control reason on the while loop.

while is_on:
    options = menu.get_items()
    choice = input(str(f"What would you like? ({options}): "))
    if choice == 'off':
        is_on = False
        print('Coffee Machine is being turned off.')
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
