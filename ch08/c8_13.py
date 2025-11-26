"""c8_13.py"""

from functools import lru_cache


@lru_cache(None)
def fibonacci_cache(i):
    """Fibonacci"""
    if i == 0:
        return 0
    if i == 1:
        return 1
    return fibonacci_cache(i-1) + \
            fibonacci_cache(i-2)


N = 11
print("Fibonacci (functools):")
for j in range(N):
    fib = fibonacci_cache(j)
    print(f"n={j:02} : {fib}")

print(fibonacci_cache.cache_info())
