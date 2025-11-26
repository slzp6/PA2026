"""c4_18.py"""

# pylint: disable=no-else-break

for i in [10, 20, 30, 40]:
    print(i, end=" ")
    if i == 30:
        break
    else:
        print("done")
