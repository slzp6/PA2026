"""c4_19.py"""

FLAG = False
for i in [10, 20, 30, 40]:
    print(i, end=" ")
    if i == 30:
        FLAG = True
        break

if FLAG is False:
    print("done")
