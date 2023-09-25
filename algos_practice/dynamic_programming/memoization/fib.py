# Write a function `fib(n)` that takes in anumber as an argument.
# The function should return the n-th number of the Fibonacci sequence.

# The 1st and 2nd number of the sequence is 1.
# To generate the nexxt number of the sequence, we sum the previous two.

# memoization
# dict keys = arg, value = return value

def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

print(fib(6))
print(fib(7))
print(fib(8))
print(fib(50))
