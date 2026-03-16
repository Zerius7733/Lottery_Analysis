import math


def roll_cost(roll_size):
    cost = 0
    for k in range(2, min(roll_size, 6) + 1):
        cost += math.comb(roll_size, k)
    return cost


def debug_roll_cost(roll_size):
    max_match = min(roll_size, 6)
    cost = 0
    print(f"Breakdown for roll {roll_size} num:")
    for k in range(2, max_match + 1):
        combinations = math.comb(roll_size, k)
        cost += combinations
        print(f"{roll_size}C{k} = {combinations}")
    print(f"Total cost = {cost}")
    return cost

if __name__ == "__main__":
    while True:
        k = int(input("Roll how many numbers: "))
        print(f"The expected price to pay for roll {k} num is: ${roll_cost(k)}.")
        debug = input("Show breakdown? (y/n): ").strip().lower()
        if debug == "y":
            debug_roll_cost(k)
