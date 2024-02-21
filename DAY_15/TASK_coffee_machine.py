# TODO 1. предложить выбрать "What would you like? (espresso/latte/cappuccino):" + вывод "Please, insert coins"
# TODO 2. после ввода напитка проверка на достаточность ингридиентов на его приготовление
# TODO 2.1 если хватает просим внести монеты и предложить внести по очереди: quarters, dimes, nickles, pennies
# TODO 2.2 вернуть сдачу, если клиент дал лишних денег "Here is {change} in change" + вывести "Here is your {beverage}. Enjoy!"
# TODO 2.3 если денег не хватило сказать, что не хватило "Sorry that's not enough money. Money refunded." и предложить выбрать напиток заново
# TODO 2.4 если не хватает ингридиентов вывод: "Sorry there is not enough {beverage}"
# TODO 3 при вводе "report" показываем сколько осталось ресурсов(water, milk, coffee, money загружено в автомате на данный момент)
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

print(MENU['espresso']['ingredients']['water'])

client_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

ingredients_start = {
    'water': 300,
    'milk': 200,
    'coffee': 100,
    'money': 0
}


def enough_ingredients(choice):
    water = ingredients_start['water'] - MENU[choice]['ingredients']['water']
    milk = ingredients_start['milk'] - MENU[choice]['ingredients']['milk']
    coffee = ingredients_start['coffee'] - MENU[choice]['ingredients']['coffee']

    if water >= 0 and milk >= 0 and coffee >= 0:
        return True
    elif water < 0:
        return print("Sorry there is not enough water.")
    elif milk < 0:
        return print("Sorry there is not enough milk.")
    elif coffee < 0:
        return print("Sorry there is not enough coffee.")



print("Please insert coins.")

quarters = input("how many quarters?: ")
dimes = input("how many dimes?: ")
nickles = input("how many nickles?: ")
pennies = input("how many pennies?: ")
print(f"Here is ${change} in change.")
