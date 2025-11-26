"""c8_4.py"""

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

sorted_fruits = sorted(fruits, key=lambda x: x['qty'])
print(sorted_fruits)
