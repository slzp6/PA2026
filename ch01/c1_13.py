"""c1_13.py"""

x = {"apple", "banana", "cherry"}
y = frozenset({"apple", "banana", "cherry"})
print(y)
print(type(y))

print("---")
print(set(dir(x)) - set(dir(y)))
