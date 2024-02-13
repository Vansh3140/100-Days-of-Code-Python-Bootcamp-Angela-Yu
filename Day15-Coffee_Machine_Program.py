MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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

machine_state = "on"
money = 2.5


def resources_sufficient(coffee_name):
    '''Function to check whether there are ample amount of ingredients'''
    if resources["milk"] < MENU[coffee_name]["ingredients"]["milk"]:
        return "milk"
    elif resources["coffee"] < MENU[coffee_name]["ingredients"]["coffee"]:
        return "coffee"
    elif resources["water"] < MENU[coffee_name]["ingredients"]["water"]:
        return "water"
    else:
        return True


def print_report():
    ''' Function to print the current quantity of ingredients '''
    global money
    print(f"Water is {resources["water"]}ml")
    print(f"Milk is {resources["milk"]}ml")
    print(f"Coffee is {resources["coffee"]}g")
    print(f"Money is ${money}")


def order_drink(coffee_name):
    '''Function to check money and ingredients and further process the coffee'''
    output = resources_sufficient(coffee_name)
    global money
    if output == True:
        penny = float(input("Enter the number of pennies:\n"))
        dime = float(input("Enter the number of dimes:\n"))
        nickel = float(input("Enter the number of nickels:\n"))
        quarter = float(input("Enter the number of quarters:\n"))
        tot_money = penny * 0.01 + dime * 0.1 + nickel * 0.05 + quarter * 0.25
        if tot_money < MENU[coffee_name]["cost"]:
            print("Sorry that's not enough money. Money refunded.\n")
        else:
            print(f"Here is ${round(tot_money - MENU[coffee_name]["cost"], 2)} dollars in change.\n")
            resources["water"] -= MENU[coffee_name]["ingredients"]["water"]
            resources["milk"] -= MENU[coffee_name]["ingredients"]["milk"]
            resources["coffee"] -= MENU[coffee_name]["ingredients"]["coffee"]
            print(f"“Here is your {coffee_name}. Enjoy!")
            money+=MENU[coffee_name]["cost"]
    else:
        print(f"Sorry there is not enough {output}.")


def take_order():
    '''Function to ask user choices and further call other functions'''
    choice_of_user = input("What would you like? Type (espresso/latte/cappuccino) \n")
    global machine_state
    if choice_of_user == "off":
        machine_state = "off"
    elif choice_of_user == "report":
        print_report()
    else:
        order_drink(choice_of_user)
MENU[coffee_name]["cost"]

while machine_state == "on":
    take_order()

print("Thank You!! for giving us your valuable time...")


