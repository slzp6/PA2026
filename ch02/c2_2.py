"""c2_2.py"""

X = 10
Y = 0
print("X:", X)
print("Y:", Y)

try:
    print("X / Y = ", X / Y)
except ZeroDivisionError as e:
    print(e)
