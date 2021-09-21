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
    "money": 0
}


coins = [
    ["quarters", "dimes", "nickles", "pennies"],
    {
    "quarters" : 0.25,
    "dimes" : 0.10,
    "nickles" : 0.05,
    "pennies" : 0.01,
     }
]

def purchase(drink):
    print("Please insert coins.")
    total_coins = 0
    for coin in coins[0]:
        coin_insert = int(input(f"how many {coin}?: "))
        total_coins += round((coin_insert * coins[1][coin]), 2)
        print(total_coins)
    beverage_cost = MENU[drink]["cost"]
    print(beverage_cost)
    change = total_coins - beverage_cost
    print(change)
    if change >= 0:
        print(f"Here is ${change} in change.\nHere is your {drink} ☕️. Enjoy!")
        change_resources(drink)
    else:
        print("Sorry that's not enough money. Money refunded.")

def calc_report() :
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')
    print(f'Money: ${resources["money"]}')

def change_resources(drink):
    resources["money"] += MENU[drink]["cost"]
    for item in resources:
        if item in MENU[drink]["ingredients"]:
            resources[item] = resources[item] - MENU[drink]["ingredients"][item]

def coffee_machine(drink):
    if drink.lower() == "report":
        calc_report()
    else:
        purchase(drink)


end_purchase = False
while not end_purchase:
    print("Coffee Machine ☕")
    beverage = input(f'What would you like? (espresso ${MENU["espresso"]["cost"]} /latte ${MENU["latte"]["cost"]} / cappuccino ${MENU["cappuccino"]["cost"]}): ')
    if beverage == "off":
        resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
            "money": 0
        }
        end_purchase = True
    else:
        coffee_machine(beverage)
