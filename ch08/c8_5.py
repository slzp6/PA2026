"""c8_5.py"""

fruits = [{
    'name': 'banana',
    'qty': 10
}, {
    'name': 'apple',
    'qty': 30
}, {
    'name': 'cranberry',
    'qty': 20
}]

sorted_fruits = sorted(fruits, key=lambda x: x['name'])
print(sorted_fruits)
