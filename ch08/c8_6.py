"""c8_6.py"""


def factorial(i):
    """factorial"""
    if i == 0:
        return 1
    return i * factorial(i - 1)


N = 5
fact = factorial(N)
print(f"N={N:2} : {fact}")

N = 20
fact = factorial(N)
print(f"N={N:2} : {fact}")
