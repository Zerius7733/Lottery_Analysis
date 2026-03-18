import math

TOTAL_COMB = math.comb(49, 6)
DEFAULT_PAYOUTS = {2: 62, 3: 620, 4: 6200}


def roll_cost(roll_size):
    cost = 0
    for k in range(2, min(roll_size, 4) + 1): #max payout is 4
        cost += math.comb(roll_size, k)
    return cost


def debug_roll_cost(roll_size):
    max_match = min(roll_size, 4)
    cost = 0
    print(f"Breakdown for roll {roll_size} num:")
    for k in range(2, max_match + 1):
        combinations = math.comb(roll_size, k)
        cost += combinations
        print(f"{roll_size}C{k} = {combinations}")
    print(f"Total cost = {cost}")
    return cost


def num_k(k):
    winning_combinations = math.comb(49 - k, 6 - k)
    odds = winning_combinations / TOTAL_COMB
    return odds * 100


def expected_value(roll_size, payouts=None):
    if payouts is None:
        payouts = DEFAULT_PAYOUTS

    value = 0
    for k in range(2, min(roll_size, 4) + 1):
        value += math.comb(roll_size, k) * num_k(k) * payouts[k] / 100
    return value


def debug_expected_value(roll_size, payouts=None):
    if payouts is None:
        payouts = DEFAULT_PAYOUTS

    value = 0
    cost = roll_cost(roll_size)
    print(f"Expected value breakdown for roll {roll_size} num:")
    for k in range(2, min(roll_size, 4) + 1):
        combinations = math.comb(roll_size, k)
        odds_percent = num_k(k)
        contribution = combinations * odds_percent * payouts[k] / 100
        value += contribution
        print(
            f"{roll_size}C{k} x {odds_percent:.5f}% x ${payouts[k]} = ${contribution:.5f}"
        )
    payout_percentage = (value / cost * 100) if cost else 0
    print(f"Expected payout = ${value:.5f} ({payout_percentage:.2f}% of price paid)")
    print(f"Net expected value = ${value - cost:.5f}")
    return value

if __name__ == "__main__":
    while True:
        k = int(input("Roll how many numbers: "))
        cost = roll_cost(k)
        expected_payout_value = expected_value(k)
        payout_percentage = (expected_payout_value / cost * 100) if cost else 0
        print(f"The expected price to pay for roll {k} num is: ${cost}.")
        print(
            f"The expected payout for roll {k} num is: ${expected_payout_value:.5f} "
            f"({payout_percentage:.2f}% of price paid)."
        )
        debug = input("Show breakdown? (y/n): ").strip().lower()
        if debug == "y":
            debug_roll_cost(k)
            debug_expected_value(k)
