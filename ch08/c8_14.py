"""c8_14.py"""


def factorial_stack(n):
    """factorial stack"""
    stack = []
    while n > 0:
        stack.append(n)
        n -= 1
    result = 1

    while len(stack) > 0:
        result *= stack.pop()

    return result


N = 11
for j in range(N):
    fib = factorial_stack(j)
    print(f"n={j:02} : {fib}")
