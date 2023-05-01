# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import status


# Press the green button in the gutter to run the script.
def print_report():
    money = status.profit
    water = status.resources["water"]
    milk = status.resources["milk"]
    coffee = status.resources["coffee"]
    print(f"""Water: {water}ml
Milk: {milk}ml
Coffee: {coffee}g
Money: ${money}
    """)


def has_enough_resources(product):
    ingredients = product["ingredients"]
    machine_resources = status.resources

    for ing in ingredients:
        if ingredients[ing] > machine_resources[ing]:
            print(f"Sorry there is not enough {ing}.")
            return False
    return True


def update_machine_status(product):
    status.profit += product["cost"]
    for ing in product["ingredients"]:
        status.resources[ing] -= product["ingredients"][ing]


def deliver_product(command, product, inserted_cash):
    change = round(inserted_cash - product["cost"], 2)
    if change > 0:
        print(f"Here is ${change} in change.")
    print(f"Here is your {command} ☕. Enjoy!");
    update_machine_status(product)


def refund_cash():
    print("Sorry that's not enough money. Money refunded.")


def take_cash():
    print("Please insert coins.")
    accepted_coins = status.accepted_coins_value
    inserted_cash = 0
    for coin in accepted_coins:
        inserted_coins = int(input(f"how many {coin}?: "))
        inserted_cash += (inserted_coins * accepted_coins[coin])
    return inserted_cash


def process_order(command):
    menu = status.MENU
    chosen_product = menu[command]
    if has_enough_resources(chosen_product):
        inserted_cash = take_cash()
        if inserted_cash >= chosen_product["cost"]:
            deliver_product(command, chosen_product, inserted_cash)
        else:
            refund_cash()


def start_coffee_machine():
    while True:
        command = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if command == 'report':
            print_report()
        elif command in ["espresso", "latte", "cappuccino"]:
            process_order(command)
        else:
            print("Sorry, command not available")
            break


if __name__ == '__main__':
    start_coffee_machine()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
