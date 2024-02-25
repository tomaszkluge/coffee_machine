from source.data import coffees_resources
from source.coins import insert_coin_espresso, insert_coin_latte, insert_coin_cappuccino


def check_resources_espresso():
    espresso_resources = coffees_resources["espresso"]

    for resource, amount in espresso_resources.items():
        if resource != "money":
            if coffees_resources["resources"][resource] < amount:
                print(f"Not enough {resource} to make espresso")
                return False
    return insert_coin_espresso()


def check_resources_latte():
    latte_resources = coffees_resources["latte"]

    for resource, amount in latte_resources.items():
        if resource != "money":
            if coffees_resources["resources"][resource] < amount:
                print(f"Not enough {resource} to make latte")
                return False
    return insert_coin_latte()


def check_resources_cappuccino():
    cappuccino_resources = coffees_resources["cappuccino"]

    for resource, amount in cappuccino_resources.items():
        if resource != "money":
            if coffees_resources["resources"][resource] < amount:
                print(f"Not enough {resource} to make cappuccino")
                return False
    return insert_coin_cappuccino()



