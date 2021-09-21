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

money = 0

coins = [
    ["quarters", "dimes", "nickles", "pennies"],
    {
    "quarters" : 0.25,
    "dimes" : 0.10,
    "nickles" : 0.05,
    "pennies" : 0.01,
     }
]

def process_coins(price):
    print("Please insert coins.")
    total_coins = 0
    for coin in coins[0]:
        coin_insert = int(input(f"how many {coin}?: "))
        total_coins += round((coin_insert * coins[1][coin]), 2)
    change = total_coins - price
    if change < 0:
        print("Sorry that's not enough money. Money refunded.")
        return False
    print(f"Here is ${change} in change.")
    return True

def is_enough_resources(drink):
    for item in resources:
        if resources[item] >= MENU[drink]["ingredients"][item]:
            return True
        else:
            print(f"Sorry there is not enough {item}.")
            return False


def calc_report():
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')
    print(f'Money: ${money}')

def change_resources(drink):
    global money
    money += MENU[drink]["cost"]
    for item in resources:
        if item in MENU[drink]["ingredients"]:
            resources[item] = resources[item] - MENU[drink]["ingredients"][item]


is_on = False
while not is_on:
    print("Coffee Machine ☕")
    choice = input(f'What would you like? (espresso ${MENU["espresso"]["cost"]} /latte ${MENU["latte"]["cost"]} / cappuccino ${MENU["cappuccino"]["cost"]}): ')
    if choice == "off":
        is_on = True
    elif choice == "report":
        calc_report()
    else:
        if is_enough_resources(choice):
            if process_coins(MENU[choice]["cost"]):
                change_resources(choice)
                print(f"Here is your {choice} ☕️.Enjoy!")
        else:
            is_on = True
