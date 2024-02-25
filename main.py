from data import coffees_resources
from coins import insert_coin_espresso, insert_coin_latte, insert_coin_cappuccino


def what_coffee():
    should_continue = True
    while should_continue:
        ask = input("What would you like to drink? (espresso, latte or cappuccino): ")
        if ask == "report":
            print(coffees_resources["resources"])
        elif ask == "off":
            print("Good Bye!")
            should_continue = False
        elif ask == "espresso":
            insert_coin_espresso()
        elif ask == "latte":
            insert_coin_latte()
        elif ask == "cappuccino":
            insert_coin_cappuccino()

        print(f"Rest of resources in the machine: {coffees_resources['resources']}")


what_coffee()
