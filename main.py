from data import coffees_resources
from coins import insert_coin_espresso, insert_coin_latte, insert_coin_cappuccino
from coffees import espresso, latte, cappuccino


def welcome():
    ask = input("What would you like to drink? (espresso, latte or cappuccino): ")
    return ask


def what_coffee():
    ask = welcome()
    should_continue = True
    while should_continue:
        if ask == "report":
            print(coffees_resources["resources"])
            welcome()
        elif ask == "off":
            should_continue = False
        elif ask == "espresso":
            # check resources function <- to make
            insert_coin_espresso()
            espresso()
            should_continue = False


what_coffee()
