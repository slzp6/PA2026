"""c6_25.py"""

set_a = {10, 20, 30, 40}
set_b = {30, 40, 50, 60}

print("---")
print(set_a | set_b)
print(set_a & set_b)
print(set_a - set_b)
print(set_a ^ set_b)

print("---")
print(set_a.union(set_b))
print(set_a.intersection(set_b))
print(set_a.difference(set_b))
print(set_a.symmetric_difference(set_b))
