from source.data import coffees_resources
from source.check_resources import check_resources_espresso, check_resources_latte, check_resources_cappuccino


def what_coffee():
    should_continue = True
    while should_continue:
        ask = input("What would you like to drink? (espresso, latte or cappuccino): ").lower()
        if ask == "report":
            print(coffees_resources["resources"])
        elif ask == "off":
            print("Good Bye!")
            should_continue = False
        elif ask == "espresso":
            check_resources_espresso()
        elif ask == "latte":
            check_resources_latte()
        elif ask == "cappuccino":
            check_resources_cappuccino()

        print(f"Rest of resources in the machine: {coffees_resources['resources']}")


what_coffee()
