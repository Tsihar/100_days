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

ingredients_start = {
    'water': 300,
    'milk': 200,
    'coffee': 100,
    'money': 0
}

client_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

def enough_ingredients(choice):
    water = ingredients_start['water'] - MENU[choice]['ingredients']['water']
    milk = ingredients_start['milk'] - MENU[choice]['ingredients']['milk']
    coffee = ingredients_start['coffee'] - MENU[choice]['ingredients']['coffee']

    if water >= 0 and milk >= 0 and coffee >= 0:
        return True
    elif water < 0:
        return False  # print("Sorry there is not enough water.")
    elif milk < 0:
        return False  # print("Sorry there is not enough milk.")
    elif coffee < 0:
        return False  # print("Sorry there is not enough coffee.")


def refund_money(quarter, dime, nickle, penny, beverage_cost):
    inserted_money = (0.25 * quarter) + (0.1 * dime) + (0.05 * nickle) + (0.01 * penny)
    result = inserted_money - beverage_cost
    return result


is_enough_ingredients = enough_ingredients(client_choice)

profit = 0
while is_enough_ingredients:
    print("Please insert coins.")

    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))

    change = refund_money(quarters, dimes, nickles, pennies, MENU[client_choice]['cost'])

    if change >= 0:
        profit += MENU[client_choice]['cost']
        print(f'Here is {change} in change.\nHere is your {client_choice}. Enjoy!')
    else:
        print("Sorry that's not enough money. Money refunded.")

# print(f"Here is ${change} in change.")
