"""c6_3.py"""

# pylint: disable=duplicate-key

fruits = {'apples': 10, 'apricots': 30, 'avocados': 50, 'apples': 100}

print("---")
print(fruits['apples'])
print(fruits['apricots'])
print(fruits['avocados'])

print("---")
print(fruits.get('apples'))
print(fruits.get('apricots'))
print(fruits.get('avocados'))
