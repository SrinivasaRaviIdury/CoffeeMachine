def coffee_machine():
    MENU = {'espresso': {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    }, 'latte': {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    }, 'cappuccino': {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }}

    resources = {
        "water": 3000,
        "milk": 3000,
        "coffee": 1000,
    }

    def current_resources_report():
        print(f'Water: {resources["water"]} ml')
        print(f'Milk: {resources["milk"]} ml')
        print(f'Coffee: {resources["coffee"]} g ')
        print(f'Money: ${MONEY}')

    def check_resources(curr_resources):
        if resources['water'] >= curr_resources['water'] \
                and resources['milk'] >= curr_resources['milk'] \
                and resources['coffee'] >= curr_resources['coffee']:
            return 1
        else:
            return 0

    def process_coins(price):
        global MONEY
        print("Please insert coins:")
        quarters = float(input("Insert quarters:")) * 0.25
        dimes = float(input("Insert dimes:")) * 0.10
        nickles = float(input("Insert nickles:")) * 0.05
        pennies = float(input("Insert pennies:")) * 0.01
        tot = round(quarters + dimes + nickles + pennies, 2)
        if tot == price:
            print(f"Thanks For Buying! Have a Nice Day")
            MONEY += price
        elif tot > price:
            print(f"Please Take remaining change : ${round(tot - price, 2)}")
            MONEY += price
        else:
            print("please insert sufficient coins")

    def make_coffee(req):
        resources['water'] -= req['water']
        resources['milk'] -= req['milk']
        resources['coffee'] -= req['coffee']
        print(f"Here is your {user_choice}. Enjoy!.")

    # TODO 1.Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    flag = 1
    while flag:
        user_choice = input("What would you like (espresso/latte/cappuccino):").lower()
        if user_choice in MENU:
            ingredients_of_choice = MENU[user_choice]['ingredients']
            # todo 4.Check resources sufficient?
            if check_resources(ingredients_of_choice):
                cost_of_choice = MENU[user_choice]['cost']
                process_coins(cost_of_choice)
                # todo 7.Make Coffee
                make_coffee(ingredients_of_choice)
            else:
                print("Sorry there is not enough resources")
        # todo 2.Turn off the Coffee Machine by entering “​off​” to the prompt.
        elif user_choice == 'off':
            flag = 0
        # todo 3.Print report.
        elif user_choice == 'report':
            current_resources_report()
        else:
            print('Enter Valid input')


MONEY = 0.0
coffee_machine()
