# Write a function `fib(n)` that takes in a number as an argument.
# The function should return the n-th number of the Fibonacci sequence.

# The 0th number of the sequence is 0.
# The 1st number of the sequence is 1.

# To generate the next number of the sequence, we sum the previous two.

# n:      0, 1, 2, 3, 4, 5, 6, 7,  8,  9
# fib(n): 0, 1, 1, 2, 3, 5, 8, 13, 21, 34


def fib(n):
    tab = [0 for _ in range(n + 1)]
    tab[1] = 1
    i = 0
    while i < n:
        tab[i + 1] += tab[i]
        if i + 2 <= n:
            tab[i + 2] += tab[i]
        i += 1

    return tab[-1]


print(fib(6))
print(fib(7))
print(fib(8))
print(fib(50))
print(fib(100000))
