"""c12_9.py"""

import csv

db = []
with open("fruits.csv", "r", encoding="utf8", newline="") as f:
    csv_reader = csv.reader(f)
    # print(type(csv_reader))
    for row in csv_reader:
        db.append(row)

print(db)
print("---")
for item in db:
    print(item)
