"""c5_18.py"""

fruits = {"apple": 100, "banana": 200, "cherry": 300}
fruits_new = {item.upper(): val * 2.0 for item, val in fruits.items()}

print(fruits)
print(fruits_new)
