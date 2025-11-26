"""c5_2.py"""

A = 10
B = 20

# ---
MAX_VAL = A if A > B else B
print(MAX_VAL)

# ---
if A > B:
    MAX_VAL = A
    print(MAX_VAL)
else:
    MAX_VAL = B
    print(MAX_VAL)
