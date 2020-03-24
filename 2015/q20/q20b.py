""" Finds factors that when multiplied by 50 are >= the original number,
multiplies those factors by 11 and adds them, and if that sum is >=
NUM_TO_MEET, halts """



NUM_TO_MEET = 36000000


def sum_factors(factor_list):
    total = 0
    for factor in factor_list:
        total += factor * 11
    return total

def get_factors(x):
    factors = []
    i = 1
    while i*i <= x:
        if x % i == 0:
            if i * 50 >= x:
                factors.append(i)
            if x // i != i:
                if (x // i)*50 >= x:
                    factors.append(x // i)
        i += 1

    return factors

def main():
    for i in range(831600, NUM_TO_MEET*10):
        if sum_factors(get_factors(i)) >= NUM_TO_MEET:
            print(i)
            return

if __name__ == '__main__':
    main()
