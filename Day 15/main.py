MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk":0
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
is_on=True

def isSufficient(coff):
    coffee = MENU[coff]
    ingred = coffee['ingredients']
    if resources["water"]>=ingred["water"] and resources["milk"]>=ingred["milk"] and resources["coffee"]>=ingred["coffee"]:
        return True
    else:
        return False

def make_coffee(coff):
    coffee = MENU[coff]
    ingred=coffee['ingredients']
    resources["water"]-=ingred["water"]
    resources["coffee"] -= ingred["coffee"]
    resources["milk"] -= ingred["milk"]
    print(f"Here is your {coff} ☕, Enjoy! ")


def charge (coff) :
    chosen_coffee=MENU[coff]
    cost_coffee = chosen_coffee["cost"]
    print("~Enter the denominations~")
    pennies=float(input("Pennies: "))*0.01
    nickles = float(input("Nickles: "))*0.05
    dimes = float(input("Dimes: "))*0.1
    quarters = float(input("Quarters: "))*0.25
    cost_user=round(pennies+nickles+dimes+quarters,2)
    if cost_user>=cost_coffee:
        print("Here is your change: $", round(cost_user-cost_coffee, 2))
        make_coffee(coff) # making the coffee after the money is dispensed
    else:
        print("~ Please enter sufficient Amount, Money Refunded!! ~")


while is_on:
    user_input=input("What would you like? (espresso/latte/cappuccino): ")
    if user_input=="off":
        is_on=False
    elif user_input=="report":
        print("~Current Resources available~")
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
    else:
        if isSufficient(user_input):
            charge(user_input)
        else:
            print("Sorry, Not enough Resource!")