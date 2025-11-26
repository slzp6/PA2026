"""c6_12.py"""

dict_fruits = {'kiwi': [30, 'B'], 'grape': [10, 'C'], 'pineapple': [20, 'A']}

print(dict_fruits)

print("---")
for key in sorted(dict_fruits.keys()):
    print(key, dict_fruits[key])

print("---")
for key in sorted(dict_fruits.keys()):
    print(key, dict_fruits[key][0])
