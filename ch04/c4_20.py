"""c4_20.py"""

for n in range(2, 15):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} equals {x} * {n//x}")
            break
    else:
        print(n, "is a prime number")
