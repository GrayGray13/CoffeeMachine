machine_is_on = True

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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0.00
current_transaction = 0.00


def is_enough_resources(menu_item, resources_given):
    missing_ingredients = []
    for ingredient in menu_item["ingredients"]:
        if menu_item['ingredients'][ingredient] > resources_given[ingredient]:
            missing_ingredients.append(ingredient)
    if len(missing_ingredients) > 0:
        print(f"Sorry there is not enough {', or '.join(missing_ingredients)}.")
    return len(missing_ingredients) == 0


def insert_money(money_in_machine):
    print("Please insert coins.")
    quarters = int(input("how many quarters?: ")) * 0.25
    dimes = int(input("how many dimes?: ")) * 0.10
    nickles = int(input("how many nickles?: ")) * 0.05
    pennies = int(input("how many pennies?: ")) * 0.01

    money_in_machine += quarters + dimes + nickles + pennies

    return money_in_machine


while machine_is_on:
    print("Welcome to Coffee Master 3000")
    coffee_type = input("What would you like? (espresso/latte/cappuccino): ")

    if coffee_type == "off":
        machine_is_on = False
        print("Machine powering down")
    elif coffee_type == "espresso" or coffee_type == "latte" or coffee_type == "cappuccino":
        if is_enough_resources(MENU[coffee_type], resources):
            current_transaction = insert_money(current_transaction)
            if current_transaction < MENU[coffee_type]['cost']:
                print("Sorry that's not enough money. Money refunded.")
                current_transaction = 0.00
            elif current_transaction >= MENU[coffee_type]['cost']:
                profit += MENU[coffee_type]['cost']
                current_transaction -= MENU[coffee_type]['cost']
                for coffee_ingredient in MENU[coffee_type]["ingredients"]:
                    resources[coffee_ingredient] -= MENU[coffee_type]["ingredients"][coffee_ingredient]
                if current_transaction > 0:
                    print(f"Here is ${'%.2f' % current_transaction} in change.")
                    current_transaction = 0.00
                print(f"Here is your {coffee_type}. Enjoy!")
    elif coffee_type == "report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\n"
              f"Coffee: {resources['coffee']}g\nMoney: ${'%.2f' % profit}")
    else:
        print("Not a valid entry, please try again")
