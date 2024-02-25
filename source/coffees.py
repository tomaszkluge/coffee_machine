from source.data import coffees_resources


def espresso():
    espresso_resources = coffees_resources["espresso"]
    for resource, amount in espresso_resources.items():
        if resource == "money":
            coffees_resources["resources"][resource] += amount
        else:
            coffees_resources["resources"][resource] -= amount
    print("Level up your power with our espresso. Enjoy!")


def latte():
    espresso_resources = coffees_resources["latte"]
    for resource, amount in espresso_resources.items():
        if resource == "money":
            coffees_resources["resources"][resource] += amount
        else:
            coffees_resources["resources"][resource] -= amount
    print("Level up your power with our latte. Enjoy!")


def cappuccino():
    espresso_resources = coffees_resources["cappuccino"]
    for resource, amount in espresso_resources.items():
        if resource == "money":
            coffees_resources["resources"][resource] += amount
        else:
            coffees_resources["resources"][resource] -= amount
    print("Level up your power with our cappuccino. Enjoy!")
