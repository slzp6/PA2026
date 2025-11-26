"""c15_12.py"""

# pylint: disable=unsubscriptable-object

import matplotlib.pyplot as plt

# --- keras 3.X
from keras import datasets

# --- keras 2.X
# import tensorflow as tf
# datasets = tf.keras.datasets

(x_train, y_train), (x_test, y_test) = datasets.mnist.load_data()

W = 8
H = 4
FC = 10
FR = 4
fig = plt.figure(figsize=(W, H))
for i in range(0, FC * FR):
    img = x_train[i].reshape(28, 28)
    fig.add_subplot(FR, FC, i + 1)
    plt.imshow(img, cmap='gray')
    plt.xticks([])
    plt.yticks([])
    plt.xlabel(y_train[i])
    plt.tight_layout()
# plt.show()
plt.savefig("c15_12.png")
