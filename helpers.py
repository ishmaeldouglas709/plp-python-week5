import math

def tables_needed(people, seats):
    # Return people divided by seats, rounded UP
    return math.ceil(people / seats)


def welcome(name):
    # Return a welcome message
    return f"Welcome to PLP, {name}!"


if __name__ == "__main__":
    print(tables_needed(10, 4))
