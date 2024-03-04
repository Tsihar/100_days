from menu import Menu, MenuItem

from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee = CoffeeMaker()
machine = MoneyMachine()

is_play = True
while is_play:
    client_choice = input(f"What would you like? ({menu.get_items()}): ").lower()
    if client_choice == "off":
        is_play = False
    elif client_choice == "report":
        coffee.report()
        machine.report()
    else:
        beverage = menu.find_drink(client_choice)
        if coffee.is_resource_sufficient(beverage) and machine.make_payment(beverage.cost):
            coffee.make_coffee(beverage)
