"""c5_19.py"""

fruits = {"apple": 100, "banana": 200, "cherry": 300}
fruits_len = {item: len(item) for item, val in fruits.items()}

print(fruits)
print(fruits_len)
