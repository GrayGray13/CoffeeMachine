from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
options = menu.get_items()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
is_on = True


while is_on:
    user_input = input(f"What would you like? ({options}): ")
    if user_input == "off":
        is_on = False
        print("Machine is shutting down")
    elif user_input == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        menu_item = menu.find_drink(user_input)
        if coffee_maker.is_resource_sufficient(menu_item) and money_machine.make_payment(menu_item.cost):
            coffee_maker.make_coffee(menu_item)