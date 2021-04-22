from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menuu=Menu()
# menu_item=MenuItem()
coffee_Maker=CoffeeMaker()
money_mach=MoneyMachine()
is_on=True
while is_on:
    user_input=input(f"What would you like? ({menuu.get_items()}): ")
    if user_input=="report":
        print("~Available Resources~")
        coffee_Maker.report()
        money_mach.report()
    elif user_input=="off":
        is_on=False
    else:
        OrderItem=menuu.find_drink(user_input)
        if OrderItem:
            if coffee_Maker.is_resource_sufficient(OrderItem):
                if money_mach.make_payment(OrderItem.cost):
                    coffee_Maker.make_coffee(OrderItem)
                else:
                    print("~ You have entered Insufficient Amount ~")
            else:
                print("~ Resources Insufficient ~")
        else:
            print("~ Please enter correct details ~ ")
