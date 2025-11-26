"""c5_17.py"""

price_old = {"apple": 100, "banana": 200, "cherry": 300}
price_new = {item: val * 1.20 for (item, val) in price_old.items()}

print(price_old)
print(price_new)
