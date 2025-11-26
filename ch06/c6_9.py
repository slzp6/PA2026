"""c6_9.py"""

# pylint: disable=consider-using-dict-items
# pylint: disable=consider-iterating-dictionary

fruits = {'apples': 10, 'apricots': 30, 'avocados': 50}

print("--- keys and values")
for key in fruits:
    print(key, fruits[key])

print("--- items")
for key, value in fruits.items():
    print(key, value)

print("--- keys")
for key in fruits.keys():
    print(key)

print("--- values")
for value in fruits.values():
    print(value)
