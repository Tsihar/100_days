from menu import Menu, MenuItem

from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# menu_items = MenuItem()
menu = Menu()
coffee = CoffeeMaker()
machine = MoneyMachine()

is_play = True
while is_play:
    client_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if client_choice == "off":
        is_play = False
    elif client_choice == "report":
        coffee.report()
        machine.report()
    else:
        if coffee.is_resource_sufficient(client_choice):
            machine.make_payment(menu.MenuItem)
