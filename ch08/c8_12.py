"""c8_12.py"""


def memoize(f):
    """memoization decorator"""
    hash_tbl = {}

    def g(*arg):
        if arg not in hash_tbl:
            hash_tbl[arg] = f(*arg)
        return hash_tbl[arg]

    return g


@memoize
def fibonacci_me(i):
    """Fibonacci"""
    if i == 0:
        return 0
    if i == 1:
        return 1
    return fibonacci_me(i-1) + \
            fibonacci_me(i-2)


N = 11
print("Fibonacci (memoization decorator):")
for j in range(N):
    fib = fibonacci_me(j)
    print(f"n={j:02} : {fib}")
