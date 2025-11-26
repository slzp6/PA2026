"""c8_2.py"""

numbers = [10, 11, 12, 13, 14]
odds = list(filter(lambda x: x % 2 != 0, numbers))
print(odds)
