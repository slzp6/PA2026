"""c15_11.py"""

# pylint: disable=unsubscriptable-object

import matplotlib.pyplot as plt

# --- keras 3.X
from keras import datasets

# --- keras 2.X
# import tensorflow as tf
# datasets = tf.keras.datasets

(x_train, y_train), (x_test, y_test) = datasets.mnist.load_data()

fig, ax = plt.subplots()
img = ax.imshow(x_train[0].reshape(28, 28), cmap='gray')
fig.colorbar(img)
# plt.show()
plt.savefig("c15_11.png")
