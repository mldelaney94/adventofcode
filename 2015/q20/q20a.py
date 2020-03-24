""" This software finds the lowest number, the factors of which, when
multiplied by 10 and added together, is >= 36000000 """

NUM_TO_MEET = 36000000

def sum_factors(factor_list):
    total = 0
    for factor in factor_list:
        total += factor * 10
    return total

def get_factors(x):
    factors = []
    i = 1
    while i*i <= x:
        if x % i == 0:
            factors.append(i)
            if x // i != i:
                factors.append(x // i)
        i += 1

    return factors

def main():
    for i in range(831600, NUM_TO_MEET+1):
        if sum_factors(get_factors(i)) >= NUM_TO_MEET:
            print(i)
            return

if __name__ == '__main__':
    main()
