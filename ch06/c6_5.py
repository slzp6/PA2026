"""c6_5.py"""

fruits = {'apples': 400, 'apricots': 500, 'avocados': 600}

print(fruits)
del fruits['apricots']
print(fruits)

fruits.pop('apples')
print(fruits)
