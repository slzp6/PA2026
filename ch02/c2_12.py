"""c2_12.py"""

X = 12
Y = 1
print("X: ", X, bin(X))
print("Y: ", Y, bin(Y))
print("---")
Z = ~X
print("~X: ", Z, bin(Z))
print("---")
Z = X << Y
print("X << Y:", Z, bin(Z))
Z = X >> Y
print("X >> Y: ", Z, bin(Z))
