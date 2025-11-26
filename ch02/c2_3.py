"""c2_3.py"""

X = 10
Y = 0
print("X:", X)
print("Y:", Y)

try:
    Z = X / Y
except ZeroDivisionError as e:
    print(e)
else:
    print("No error")
    print("X / Y = ", X / Y)
finally:
    print("done!")
