"""q12_2.py"""

import csv

F = "test_2.txt"
fields = ["f1", "f2", "f3"]
rows = [[10, 20, 30], [40, 50, 60]]

with open(F, "w", encoding="utf8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(fields)
    writer.writerows(rows)

db = []
with open(F, "r", encoding="utf8") as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        db.append(row)
print(db)
