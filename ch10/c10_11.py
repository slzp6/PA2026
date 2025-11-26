"""c10_11.py"""

print("--- 1")
S = "Open+University"
print(S)
print(S.partition("+"))

print("--- 2")
S = "The+Open++University"
print(S)
print(S.partition("++"))

print("--- 3")
S = "The+Open+University"
print(S)
print(S.partition("@"))
