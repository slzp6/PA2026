"""c14_2.py"""

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("$y = x^2$")
# plt.show()
plt.savefig("c14_2.png")
