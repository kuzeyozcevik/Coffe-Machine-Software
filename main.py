from car import *
isContinue = True
money = 0
def report():
    print(f"Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}ml\nMoney :{"{:.2f}".format(money)}")


def ingrediants(y):
    if not y == "espresso":
        resources["water"] -= MENU[y]["ingredients"]["water"]
        resources["milk"] -= MENU[y]["ingredients"]["milk"]
        resources["coffee"] -= MENU[y]["ingredients"]["coffee"]
    else:
        resources["water"] -= MENU[y]["ingredients"]["water"]
        resources["coffee"] -= MENU[y]["ingredients"]["coffee"]


def coin(x):
    global money
    input_money = 0
    quarters = int(input("Quarters : "))
    dimes = int(input("Dimes : "))
    nickles = int(input("Nickles : "))
    pennies = int(input("Pennies : "))
    input_money += ((quarters*0.25) + (dimes*0.1) + (nickles*0.05) + (pennies * 0.01))
    money += ((quarters*0.25) + (dimes*0.1) + (nickles*0.05) + (pennies * 0.01))
    if input_money == MENU[x]["cost"]:
        print("Money is enough.")
        ingrediants(x)
        print(f"Here is your {x} enjoy!")
    elif input_money > MENU[x]["cost"]:
        money -= input_money - MENU[x]["cost"]
        refund_money = "{:.2f}".format(input_money - MENU[x]["cost"])
        print(f"Your money is too much we will refund you {refund_money}")
        ingrediants(x)
        print(f"Here is your {x} enjoy!")
    else:
        print("Sorry that's not enough money. Money refunded.")


def check(x):
    if not x == "espresso":
        if resources["water"] < MENU[x]["ingredients"]["water"]:
            print("Sorry there is not enough water.")
        if resources["milk"] < MENU[x]["ingredients"]["milk"]:
            print("Sorry there is not enough milk.")
        if resources["coffee"] < MENU[x]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.")
        else:
            coin(x)
    else:
        if resources["water"] < MENU[x]["ingredients"]["water"]:
            print("Sorry there is not enough water.")
        if resources["coffee"] < MENU[x]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.")
        else:
            coin(x)


def cofee():
    global isContinue
    kahve = input("What would you like? (espresso/latte/cappuccino):")
    if kahve == "espresso":
        check("espresso")
    elif kahve == "latte":
        check("latte")
    elif kahve == "cappuccino":
        check("cappuccino")
    elif kahve == "report":
        report()
    elif kahve == "off":
        isContinue = False
    else:
        print("Geçersiz Seçenek")


if __name__ == '__main__':
    while isContinue:
        cofee()