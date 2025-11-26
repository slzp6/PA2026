"""c5_6.py"""

import itertools

a = ['x', 'y', 'z']
b = [10, 20, 30]

for i, j in itertools.product(a, b):
    print(f"{i}_{j}", end=" ")
print("")
