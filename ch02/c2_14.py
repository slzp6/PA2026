"""c2_14.py"""

a = [100, 3.14, "ouj"]
b = [100, 3.14, "ouj"]
c = a

print(a is c)
print(a is b)
print(a == b)
print(id(a), id(b), id(c))
