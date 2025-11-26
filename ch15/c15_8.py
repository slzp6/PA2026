"""c15_8.py"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

x = 10.0 * np.random.rand(100, 1)
y = 1.2 * x + np.random.rand(100, 1) + 3.0

lin_reg = LinearRegression()
lin_reg.fit(x, y)
print(lin_reg.coef_)
print(lin_reg.intercept_)

plt.scatter(x, y)
plt.axis([0, 15, 0, 25])
plt.xlabel("x")
plt.ylabel("y")
# plt.show()
plt.savefig("c15_8a.png")

print("---")
plt.scatter(x, y)
plt.plot(x, lin_reg.predict(x), color='red')
plt.axis([0, 15, 0, 25])
plt.xlabel("x")
plt.ylabel("y")
# plt.show()
plt.savefig("c15_8b.png")

print("---")
x_ext = np.array([[10], [11], [12], [13], [14]])
y_pred = lin_reg.predict(x_ext)
plt.plot(x, lin_reg.predict(x), color='red')
plt.scatter(x_ext, y_pred)
plt.axis([0, 15, 0, 25])
plt.xlabel("x")
plt.ylabel("y")
# plt.show()
plt.savefig("c15_8c.png")
