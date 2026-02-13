#!/usr/bin/env python3
"""
Simplified Singapore 4D simulation for ROI and Time-to-First-Prize.
Removed CLI to ensure it runs directly without arguments.
"""
import dataclasses as dc
import random
from collections import Counter
from typing import Dict, List, Tuple

ORDINARY_BIG = {"first": 2000.0, "second": 1000.0, "third": 490.0, "starter": 250.0, "consolation": 60.0}
ORDINARY_SMALL = {"first": 3000.0, "second": 2000.0, "third": 800.0}

DRAW_CATS = ("first", "second", "third", "starter", "consolation")

@dc.dataclass(frozen=True)
class Bet:
    number: str
    stake: float = 1.0
    entry_type: str = "ordinary"
    big: bool = True
    small: bool = False

    def __post_init__(self):
        if not (isinstance(self.number, str) and len(self.number) == 4 and self.number.isdigit()):
            raise ValueError("number must be 4-digit string")
        if not (self.big or self.small):
            raise ValueError("must bet on big or small")

    @property
    def pattern(self) -> str:
        counts = sorted(Counter(self.number).values(), reverse=True)
        if counts == [4] or counts == [3, 1]:
            return "3same"
        if counts == [2, 2]:
            return "2pairs"
        if counts == [2, 1, 1]:
            return "2same"
        return "4diff"

def generate_draw(rng: random.Random) -> Dict[str, List[str]]:
    pool = rng.sample(range(10_000), 23)
    fmt = lambda n: f"{n:04d}"
    return {
        "first": [fmt(pool[0])],
        "second": [fmt(pool[1])],
        "third": [fmt(pool[2])],
        "starter": list(map(fmt, pool[3:13])),
        "consolation": list(map(fmt, pool[13:23])),
    }

def _win_category(num: str, draw: Dict[str, List[str]]) -> Tuple[str | None, str | None]:
    for cat in DRAW_CATS:
        if num in draw[cat]:
            return cat, num
    return None, None

def _permutations_set(num: str) -> set[str]:
    if len(set(num)) == 1:
        return {num}
    from itertools import permutations
    return {"".join(p) for p in set(permutations(num, 4))}

def _win_category_any_perm(num: str, draw: Dict[str, List[str]]) -> Tuple[str | None, str | None]:
    perms = _permutations_set(num)
    for cat in DRAW_CATS:
        if any(cand in draw[cat] for cand in perms):
            return cat, num
    return None, None

def trials_to_first_first(bets: List[Bet], seed: int | None = None, max_draws: int = 50_000_000) -> int | None:
    rng = random.Random(seed)
    for d in range(1, max_draws + 1):
        draw = generate_draw(rng)
        first_num = draw["first"][0]
        for b in bets:
            if b.entry_type == "ordinary" and b.number == first_num:
                return d
            elif b.entry_type != "ordinary" and first_num in _permutations_set(b.number):
                return d
    return None

if __name__ == "__main__":
    # Example: runs directly
    sample_size = 100 # Number of samples first prize draws 
    loop_counter = sample_size
    draws_accumulated = 0 
    while loop_counter > 0: 
        bets = [Bet("1234"), Bet("5551", entry_type="ordinary")]
        draws_needed = trials_to_first_first(bets)
        print(f"Draws until first 1st Prize: {draws_needed}")
        draws_accumulated += draws_needed if draws_needed is not None else 0 
        loop_counter -= 1
    print(f"Average draws to first 1st Prize: {draws_accumulated / sample_size if draws_accumulated > 0 else 0}")
    print(f"Expected number of years: {draws_accumulated / (12*4*3) /sample_size if draws_accumulated > 0 else 0}")
    print("Simulation complete.")
    
        
