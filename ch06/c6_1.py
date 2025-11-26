"""c6_1.py"""

# pylint: disable=duplicate-key

fruits = {'apples': 10, 'apricots': 30, 'avocados': 50, 'apples': 100}

print(type(fruits))
print(list(fruits))

print("---")
print(fruits.keys())
print(fruits.values())
print(fruits.items())
