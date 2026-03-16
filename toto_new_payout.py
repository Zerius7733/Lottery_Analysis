import math 
from roll_cost import roll_cost
total_comb = math.comb(49,6)
def main():
    while True:
        print(' \n1. Calculate odds\
                \n2. Test Plan\
                \n3. Probability to strike in N draws\
                \nEnter(0 to exit):', end='')
        choice = int(input()) 
        if choice == 1: 
            odds() 
        elif choice == 2: 
            total , cost = test()
            print(f"Total cost: {total} , unit price to buy : {cost}")
        elif choice == 3: 
            prob()
        else:
            break 
    return

def test():
    base_payout = int(input('Payout in int for 2 num:'))
    accumulator = 1
    n = int(input("Nth draw: "))
    j = 1 
    while n > 0: 
        payout = j*base_payout
        if (accumulator+j*11) >= payout:
            j+=1
            continue
        else: 
            accumulator+= j*11 
        n-=1 
    return accumulator , j

def prob():
    n = int(input("Number of draws: "))
    roll_size = int(input("Roll how many numbers: "))
    print(f"Number of weeks in {n} draws is {float(n/2)}")
    odds_at_least_2 = num_roll(roll_size, 2) / 100
    failure_at_least_2 = math.pow(1-odds_at_least_2,n)
    print(f"The odds of at least 1 success for at least 2 matches in a {roll_size} num roll: {(1-failure_at_least_2)*100:.3f}%")
    odds_at_least_3 = num_roll(roll_size, 3) / 100
    failure_at_least_3 = math.pow(1-odds_at_least_3,n)
    print(f"The odds of at least 1 success for at least 3 matches in a {roll_size} num roll: {(1-failure_at_least_3)*100:.3f}%")
    odds_at_least_4 = num_roll(roll_size, 4) / 100
    failure_at_least_4 = math.pow(1-odds_at_least_4,n)
    print(f"The odds of at least 1 success for at least 4 matches in a {roll_size} num roll: {(1-failure_at_least_4)*100:.3f}%")
    odds_3num = num_k(3)/100
    failure_3num = math.pow(1-odds_3num,n)
    print(f"The odds of at least 1 success for 3 num only: {(1-failure_3num)*100:.3f}%")
    odds_4num = num_k(4)/100 
    failure_4num = math.pow(1-odds_4num,n)
    print(f"The odds of at least 1 success for 4 num only: {(1-failure_4num)*100:.3f}%")
    return None

        
def odds() : 
    while True: 
        print(' \n1. Additional Num\
                \n2. 2 num\
                \n3. 3 num\
                \n4. 4 num\
                \n5. roll k num\
                \n6. Expected Payout\
                \n7. iToto odds\
                \nEnter(0 to exit):', end='')
        choice = int(input())
        if choice == 1: 
            print(f'The odds of striking additional number:{num_k(choice):.5f}%.')
        elif choice in [2,3,4]:
            print(f'The odds of striking {choice} number:{num_k(choice):.5f}%.')
        elif choice == 5: 
            roll_size = int(input("Roll how many numbers: "))
            print(f'The odds of striking at least 2 number with {roll_size} numbers:{num_roll(roll_size, 2):.5f}%.')
            print(f'The odds of striking at least 3 number with {roll_size} numbers:{num_roll(roll_size, 3):.5f}%.')
            print(f'The odds of striking at least 4 number with {roll_size} numbers:{num_roll(roll_size, 4):.5f}%.')
            print(f'The expected price to pay for roll {roll_size} num is: ${roll_cost(roll_size)}.')
        elif choice == 6:
            print(f'{expected_payout():.2f}')
        elif choice == 7:
            print(f'The odds of striking iToto:{itoto_odds():.5f}%.')
        else:
            break 
    return None

def payout():
    while True: 
        print('1.Expected payout')
        break
    return None

def expected_payout(): 
    payout = 0
    for k in range(2,5):
        payout += math.comb(4,k)*num_k(k)*{2:62,3:620,4:6200}[k]/100
    return payout

def num_k(k):
    num_k = math.comb(49-k,6-k)
    odds = num_k/total_comb
    return odds*100

def num_roll(roll_size, min_match=2):
    num_roll = 0
    for k in range(min_match, min(roll_size, 6) + 1):
        num_roll += math.comb(roll_size,k)*num_k(k)
        
    return num_roll

def itoto_odds(): 
    global total_comb
    k = 3
    odds = 0
    for k in range(3,7):
        k_odds = (math.comb(12,k)*math.comb(37,6-k))/total_comb
        odds += k_odds
        print (f"Odds of {k} num: {k_odds*100:.5f}%")
    return odds*100

#print(math.comb(47,4)*math.comb(4,2))
if __name__ == "__main__":
    main() 
