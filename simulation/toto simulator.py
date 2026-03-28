import random
import time


def draw_ticket():
    # 6 unique numbers from 1..49, sorted for easy comparison
    return tuple(sorted(random.sample(range(1, 50), 6)))


def format_draw_span(draws):
    weeks = draws / 2
    total_months = int(round(weeks * 12 / 52))
    years, months = divmod(total_months, 12)
    return years, months, weeks


def get_user_ticket():
    """
    Read user-picked numbers from 1..49.
    Supports normal 6-number entry or larger rolls.
    """
    while True:
        raw = input("Enter your numbers from 1 to 49, separated by spaces: ").strip()
        try:
            numbers = tuple(sorted(int(value) for value in raw.replace(",", " ").split()))
        except ValueError:
            print("Invalid input. Please enter integers only.")
            continue
        if 50 in numbers:
            numbers = [1,2,3,4,5,6,7,8,9,10]
            return numbers


        if len(numbers) < 2:
            print("Please enter at least 2 numbers.")
            continue
        if len(set(numbers)) != len(numbers):
            print("Numbers must be unique.")
            continue
        if any(number < 1 or number > 49 for number in numbers):
            print("All numbers must be between 1 and 49.")
            continue
        return numbers


def simulate_toto(progress_every=1_000_000, seed=None):
    """
    Keep generating random Toto tickets until one equals the draw.
    Returns (attempts, seconds_elapsed, draw).
    """
    if seed is not None:
        random.seed(seed)

    attempts = 0
    t0 = time.time()
    guess = draw_ticket()
    while True:
        attempts += 1
        target = draw_ticket()
        if guess == target:
            break
        if progress_every and attempts % progress_every == 0:
            elapsed = time.time() - t0
            print(f"Progress: {attempts:,} guesses in {elapsed:.1f}s")

    elapsed = time.time() - t0
    print(f"\nHIT! Winning draw: {target}")
    print(f"Attempts: {attempts:,}")
    print(f"Time: {elapsed:.2f}s (~{attempts / elapsed:,.0f} guesses/sec)")
    return attempts, elapsed, target


def simulate_user_ticket(draws=100, ticket=None, seed=None, progress_every=None, show_hits=True):
    """
    Simulate `draws` Toto draws for a fixed user ticket.
    Returns (ticket, hit_counts) where hit_counts maps matches 2..6 to frequency.
    """
    if seed is not None:
        random.seed(seed)

    if ticket is None:
        ticket = get_user_ticket()

    if draws <= 0:
        raise ValueError("draws must be more than 0")

    if progress_every is None:
        progress_every = max(1, draws // 10)

    max_match_to_report = min(6, len(ticket))
    hit_counts = {matches: 0 for matches in range(2, max_match_to_report + 1)}
    ticket_set = set(ticket)
    t0 = time.time()

    print(f"\nYour numbers: {ticket}")
    print(f"Starting simulation for {draws:,} draw(s)...")

    for draw_index in range(1, draws + 1):
        drawn_ticket = draw_ticket()
        matches = len(ticket_set & set(drawn_ticket))

        if matches >= 2:
            tracked_matches = min(matches, max_match_to_report)
            hit_counts[tracked_matches] += 1
            if show_hits:
                print(
                    f"Draw {draw_index:,}: hit {matches} number(s) | "
                    f"Drawn: {drawn_ticket}"
                )

        if progress_every and (draw_index % progress_every == 0 or draw_index == draws):
            elapsed = time.time() - t0
            print(
                f"Progress: {draw_index:,}/{draws:,} draws completed "
                f"in {elapsed:.1f}s"
            )

    elapsed = time.time() - t0
    print("\nSummary")
    print(f"Your numbers: {ticket}")
    print(f"Simulated draws: {draws:,}")
    for matches in range(2, max_match_to_report + 1):
        count = hit_counts[matches]
        percentage = (count / draws) * 100
        print(f"Hit {matches} numbers: {count:,} time(s) ({percentage:.5f}%)")
    years, months, weeks = format_draw_span(draws)
    print(
        f"Equivalent draw period: {years} year(s) and {months} month(s) "
        f"(about {weeks:,.1f} week(s) at 2 draws per week)"
    )
    print(f"Time: {elapsed:.2f}s")
    return ticket, hit_counts


def main():
    while True:
        print(
            "\n1. Simulate until jackpot hit"
            "\n2. Simulate my own numbers"
            "\nEnter(0 to exit): ",
            end=""
        )
        choice = input().strip()

        if choice == "1":
            simulate_toto(progress_every=1_000_000)
        elif choice == "2":
            draws = int(input("How many draws to simulate: "))
            simulate_user_ticket(draws)
        elif choice == "0":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
