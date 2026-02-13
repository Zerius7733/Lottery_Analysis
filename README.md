# Lottery Analysis

Collection of Python scripts for exploring Singapore-style lottery odds and simple Monte Carlo simulations (Toto and 4D).

## Files
- `Probability Calculator.py`: menu-driven probability calculator for Toto/4D, plus inverse calculation (target probability -> required draws/years).
- `toto_new_payout.py`: Toto odds utilities (k-number matches, roll odds, expected payout, iToto odds, plan/probability helpers).
- `toto simulator.py`: brute-force simulation that keeps generating draws until one ticket matches exactly.
- `4d simulation.py`: 4D draw simulation focused on time-to-first first-prize hit.
- `4d price.py`: calculator for 4D betting cost (Singapore Pools/private, with roll/permutation handling).
- `fixed vs QP toto simulation.py`: compares fixed ticket vs quick-pick strategy under equal jackpot odds.

## Requirements
- Python 3.10+ recommended.
- Standard library only (no external packages required).

## Run Scripts
From `Lottery/Lottery_Analysis`:

```powershell
python ".\Probability Calculator.py"
python ".\toto_new_payout.py"
python ".\toto simulator.py"
python ".\4d simulation.py"
python ".\4d price.py"
python ".\fixed vs QP toto simulation.py"
```

## Notes
- Scripts are mostly interactive CLI programs and not packaged as a single module.
- Some simulations use very large trial counts and can run for a long time.
- Filenames include spaces, so keep quotes around paths when running commands.
- Outputs are exploratory/statistical and not financial advice.
