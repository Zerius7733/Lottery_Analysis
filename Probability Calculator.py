import math
from toto_priv import num_roll
#create menu - ok
#implement functions - ok 
# add more features
# should implement os file dir function - wrong program notes ? 
global P_toto_miss
global P_4d_miss
P_toto_strike = 1/math.comb(49,6)
P_toto_miss = 1 - P_toto_strike
P_4d_strike = 1/10000
P_4d_miss = 1 - P_4d_strike

def geo_func(p,q,draws):
    odds = 0 
    while draws > 0 :
        odds += pow(q,(draws-1))*p
        draws -=1
    return odds

def years_cal():
    option = input("4d/toto:")
    while option != '4d' and option != 'toto':
        option = input("4d/toto:")
    years = int(input("Number of years:"))
    draws = years*12*4*3 if option == '4d' else years*2*4*12 #before toto 4d choice 12 months * 4 weeks
    return years,draws

def draws_cal():
    option = input("4d/toto/priv:").strip().lower()
    while option != '4d' and option != 'toto'and option != 'priv':
        option = input("4d/toto/priv:")
    draws = int(input("Number of draws:"))
    years = draws /4 /12 /3 if option == '4d' else draws/4/12/2
    return years,draws 

def odds_cal(tuple_parameter):
    years , draws  = tuple_parameter 
    #print(f"Number of years: {years:.2f}")
    #toto = math.factorial(49) / (math.factorial(6)*math.factorial(49-6))
    #global choice 
    P_toto_strike = 1/math.comb(49,6)
    global P_toto_miss
    P_toto_miss = 1 - P_toto_strike
    P_toto_never_winning = pow(P_toto_miss,draws)
    P_toto_at_least_once = 1 - P_toto_never_winning
    toto_accumulator_odds = geo_func(P_toto_strike,P_toto_miss,draws)
    
    P_4d_strike = 1/10000
    P_4d_miss = 1 - P_4d_strike
    P_4d_never_winning = pow(P_4d_miss,draws)
    P_4d_at_least_once = geo_func(P_4d_strike,P_4d_miss,draws) #using gemotric function
    return toto_accumulator_odds,P_toto_never_winning, P_4d_never_winning,P_4d_at_least_once,P_toto_at_least_once,years

def printing(tuple_parameter):
    toto_accumulator_odds,P_toto_never_winning, P_4d_never_winning,P_4d_at_least_once,P_toto_at_least_once,years = tuple_parameter
    print(f'P(never winning for toto) = {P_toto_never_winning:.10f}')
    print(f'Striking toto at least once in {years:.2f} years = {P_toto_at_least_once*100:.5f} %')
    #print(f'{toto_accumulator_odds:.10f} -> Geometric calculation for toto.')
    print()
    print(f'P(never winning for 4D) = {P_4d_never_winning:.10f}')
    print(f'Striking 4d at least once in {years:.2f} years = {P_4d_at_least_once*100:.2f} %')
    #print(f'{P_4d_at_least_once:.10f} -> Geometric calculation for 4D.')

def main():
    while True: 
        print("\nYears --> converting number of years to probability, Draws --> converting draws to probability\
            \n1. Calculate years\
            \n2. Calculate draws\
            \n3. Reverse Calculation (odds -> years & draws)")
        option = int(input("Choice of Calculation:"))
        switch_dict = {
            1: years_cal,
            2: draws_cal,
            3: inverse_cal
        }
        #years , odds = switch_dict.get(choice,0)()
        if option == 1 or option == 2: 
            printing(odds_cal(switch_dict.get(option,0)()))
        else: 
            inverse_printing(switch_dict.get(option,0)())
# Compute binomial probability for exactly 1 win
'''k = 1  # Exactly 1 win
nCr = math.comb(draws, k)  # Binomial coefficient (n choose k)
P_exactly_one_win = nCr * (P_toto_strike ** k) * (P_toto_miss ** (draws - k))

print(f'P(exactly one win in {years} years) = {P_exactly_one_win:.10f}')

come out with an inverse calculation with menu, given P return number of years to hit P'''
def inverse_cal():
    global P_toto_miss
    global P_4d_miss
    global choice
    odds = float(input("Enter the % for at least one win :"))/100
    choice = input("4d/toto/priv:").strip().lower()
    if choice == '4d':
        P_never_winning_4d = P_4d_miss
        draws = math.log10(1-odds) / math.log10(P_never_winning_4d)
        years = draws/12/4/3
    elif choice == 'toto':
        P_never_winning_toto = P_toto_miss
        draws = math.log10(1-odds) / math.log10(P_never_winning_toto)
        years = draws/12/4/2
    else: 
        P_never_winning_priv = 1 - num_roll()/100
        draws = math.log10(1-odds) / math.log10(P_never_winning_priv)
        years = draws/12/4/2
    return years , draws
#convert odds to toto years draws and 4d years draws 
def inverse_printing(inverse_tuple):
    global choice
    years , draws = inverse_tuple
    print(f"Number of years and draws for {choice}: {years:.2f} , {draws:.2f}")
    return

main()