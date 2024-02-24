from data import coffees_resources
from coffees import espresso, latte, cappuccino


def insert_coin_espresso():
    espresso_cost = coffees_resources["espresso"]["money"]
    coins = int(input(f"Insert {coffees_resources['espresso']['money']} coins"))
    if coins < espresso_cost:
        rest = espresso_cost - coins
        coins += input(f"You must put {rest} coins more ")
        if coins == espresso_cost:
            espresso()
        elif coins > espresso_cost:
            rest_for_user = coins - espresso_cost
            print(f"Your rest is {rest_for_user} coins")
            espresso()
    elif coins > espresso_cost:
        rest_for_user = coins - espresso_cost
        print(f"Your rest is {rest_for_user} coins")
        espresso()
    else:
        espresso()


def insert_coin_latte():
    latte_cost = coffees_resources["latte"]["money"]
    coins = int(input(f"Insert {coffees_resources['latte']['money']} coins"))
    if coins < latte_cost:
        rest = latte_cost - coins
        coins += input(f"You must put {rest} coins more ")
        if coins == latte_cost:
            latte()
        elif coins > latte_cost:
            rest_for_user = coins - latte_cost
            print(f"Your rest is {rest_for_user} coins")
            latte()
    elif coins > latte_cost:
        rest_for_user = coins - latte_cost
        print(f"Your rest is {rest_for_user} coins")
        latte()
    else:
        latte()


def insert_coin_cappuccino():
    cappuccino_cost = coffees_resources["cappuccino"]["money"]
    coins = int(input(f"Insert {coffees_resources['cappuccino']['money']} coins"))
    if coins < cappuccino_cost:
        rest = cappuccino_cost - coins
        coins += input(f"You must put {rest} coins more ")
        if coins == cappuccino_cost:
            cappuccino()
        elif coins > cappuccino_cost:
            rest_for_user = coins - cappuccino_cost
            print(f"Your rest is {rest_for_user} coins")
            cappuccino()
    elif coins > cappuccino_cost:
        rest_for_user = coins - cappuccino_cost
        print(f"Your rest is {rest_for_user} coins")
        cappuccino()
    else:
        cappuccino()
