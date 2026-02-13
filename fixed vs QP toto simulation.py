import random
from math import comb

def draw(n, k):
    return tuple(sorted(random.sample(range(1, n+1), k)))

def simulate_equal_chance(n, k, draws, seed=0):
    global draw_num 
    draw_num = draws 
    random.seed(seed)
    fixed = draw(n, k)           # fixed ticket
    fixed_hits = 0
    rand_hits = 0
    for _ in range(draws):
        winning = draw(n, k)
        # fixed strategy
        if fixed == winning:
            fixed_hits += 1
        # random new ticket each draw
        if draw(n, k) == winning:
            rand_hits += 1
    return fixed_hits, rand_hits, fixed

# 1) Real TOTO parameters: n=49, k=6 — show that hits are vanishingly rare
real_fixed, real_rand, fixed_ticket = simulate_equal_chance(49, 6, draws=300_000_000, seed=42)
real_odds = 1/comb(49,6)

# 2) Toy lottery to *see* hits in finite time: n=10, k=3
#toy_fixed, toy_rand, fixed_toy = simulate_equal_chance(10, 3, draws=100_000, seed=42)
#toy_odds = 1/comb(10,3)

print("=== Real TOTO (49 choose 6) ===")
print(f"Trials (draws): {draw_num}")
print(f"Analytical jackpot odds per draw: 1 in {comb(49,6):,} (~{real_odds:.8%})")
print(f"Fixed ticket:  {fixed_ticket}, hits: {real_fixed}")
print(f"Quick picks:   hits: {real_rand}")
print("\nNote: With such tiny odds, it's normal to see zero hits for both strategies.\n")
'''
print("=== Toy Lottery (10 choose 3) ===")
print(f"Trials (draws): 100,000")
print(f"Analytical jackpot odds per draw: 1 in {comb(10,3):,} (~{toy_odds:.4%})")
print(f"Fixed ticket:  {fixed_toy}, hits: {toy_fixed}")
print(f"Quick picks:   hits: {toy_rand}")
print("\nThey should be close, and converge with more trials.")
'''
