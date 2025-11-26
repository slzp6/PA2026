"""c2_15.py"""

# pylint: disable=unnecessary-negation

X = 30
Y = 50
print(X < 40 or Y < 40)
print(X < 40 and Y < 40)
print(not X < 40)  # "X >= 40"
print(not X == Y)  # "X != Y"
