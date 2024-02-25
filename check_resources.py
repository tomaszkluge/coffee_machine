from data import coffees_resources


def check_resources_espresso():
    espresso_resources = coffees_resources["espresso"]

    for resource, amount in espresso_resources.item():
        if resource != "money":
            if coffees_resources["resources"][resource] < amount:
                print(f"Not enough {resource} to make espresso")
                return False

    return True
