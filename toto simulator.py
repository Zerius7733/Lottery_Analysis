import random
import time

def draw_ticket():
    # 6 unique numbers from 1..49, sorted for easy comparison
    return tuple(sorted(random.sample(range(1, 50), 6)))

def simulate_toto(progress_every=1_000_000, seed=None):
    """
    Keep generating random Toto tickets until one equals the draw.
    Returns (attempts, seconds_elapsed, draw).
    """
    if seed is not None:
        random.seed(seed)

      # the winning draw
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
    print(f"Time: {elapsed:.2f}s (~{attempts/elapsed:,.0f} guesses/sec)")
    return attempts, elapsed, target

if __name__ == "__main__":
    simulate_toto(progress_every=1_000_000)
