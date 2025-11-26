"""c12_10.py"""

import csv

fields = ['name', 'quantity', 'price']
rows = [['apple', 10, 1.1], ['banana', 20, 1.2], \
        ['cherry', 30, 1.3], ['durian', 40, 1.4], \
        ['elderberry', 50, 1.5]]

with open("fruits_with_header.csv", "w", \
          encoding="utf8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(fields)
    writer.writerows(rows)
