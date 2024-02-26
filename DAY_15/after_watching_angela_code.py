MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
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


def if_enough_ingredients(ingredient_volume, volume_left):
    for item in ingredient_volume:
        if ingredient_volume[item] > volume_left[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def insert_money():
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    return (0.25 * quarters) + (0.1 * dimes) + (0.05 * nickles) + (0.01 * pennies)


def enough_money(beverage_cost, payment):
    if beverage_cost > payment:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif beverage_cost <= payment:
        global profit #поменять глобальную переменную не получится по-другому (просто обратится можно и без глобал, но изменить только с глобал)
        profit += beverage_cost
        change = payment - beverage_cost
        print(f'Here is {change} in change.') # забыл, что так можно
        return True


def deduct_ingredients(ingredient_volume, volume_left):
    for item in ingredient_volume:
        volume_left[item] -= ingredient_volume[item] #довольно таки не просто для понимания
    print(f"Here is your beverage {item}. Enjoy!")


profit = 0
is_play = True
while is_play:
    client_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if client_choice == "off":
        is_play = False
    elif client_choice == "report":
        print(f"Water: {ingredients_start['water']}ml\n"
              f"Milk: {ingredients_start['milk']}ml\n"
              f"Coffee: {ingredients_start['coffee']}ml\n"
              f"Money: ${profit}\n")
    else:
        beverage = MENU[client_choice]
        if if_enough_ingredients(beverage['ingredients'], ingredients_start):
            inserted_money = insert_money()
            if enough_money(beverage['cost'], inserted_money):
                deduct_ingredients(beverage['ingredients'], ingredients_start)



