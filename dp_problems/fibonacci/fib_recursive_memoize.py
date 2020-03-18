""" recursively solves fibonacci via memoizing results """

n = int(input('input your number '))
memo = [0]*(n+1)
memo[1] = 1
memo[2] = 1

def fib(n):
    if memo[n] > 0:
        return memo[n]
    else:
        memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

print(fib(n))
