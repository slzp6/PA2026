"""c15_13.py"""

import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

# --- keras 3.X
import keras
from keras import datasets, layers, models

# --- keras 2.X
# keras = tf.keras
# datasets = tf.keras.datasets
# layers = tf.keras.layers
# models = tf.keras.models

print("tensorflow: ", tf.__version__)
print("keras: ", keras.__version__)

DIM = 32

(x_train, _), (x_test, _) = datasets.mnist.load_data()
x_train = x_train / 255.0
x_test = x_test / 255.0
print(x_train.shape)
print(x_test.shape)

x_train = x_train.reshape((len(x_train), np.prod(x_train.shape[1:])))
x_test = x_test.reshape((len(x_test), np.prod(x_test.shape[1:])))
print(x_train.shape)
print(x_test.shape)

input_img = layers.Input(shape=(784, ))
encoded = layers.Dense(128, activation='relu')(input_img)
encoded = layers.Dense(64, activation='relu')(encoded)
encoded = layers.Dense(32, activation='relu')(encoded)

decoded = layers.Dense(64, activation='relu')(encoded)
decoded = layers.Dense(128, activation='relu')(decoded)
decoded = layers.Dense(784, activation='sigmoid')(decoded)

autoencoder = models.Model(input_img, decoded)
autoencoder.compile(optimizer='adam', loss='mse')
# keras.utils.plot_model(autoencoder, show_shapes=True, show_layer_names=True)
autoencoder.summary()
HIST = autoencoder.fit(
    x_train,
    x_train,
    epochs=5,
    # batch_size=256,
    shuffle=True,
    validation_data=(x_test, x_test))

encoder = models.Model(input_img, encoded)
encoded_input = layers.Input(shape=(DIM, ))

decoder_layer = autoencoder.layers[-3](encoded_input)
decoder_layer = autoencoder.layers[-2](decoder_layer)
decoder_layer = autoencoder.layers[-1](decoder_layer)
decoder = models.Model(encoded_input, decoder_layer)

encoded_imgs = encoder.predict(x_test)
decoded_imgs = decoder.predict(encoded_imgs)

N = 5
plt.figure(figsize=(10, 4))
for i in range(N):
    ax = plt.subplot(2, N, i + 1)
    plt.imshow(x_test[i].reshape(28, 28), cmap='gray')
    plt.title("Original")
    plt.xticks([])
    plt.yticks([])

    ax = plt.subplot(2, N, i + N + 1)
    plt.imshow(decoded_imgs[i].reshape(28, 28), cmap='gray')
    plt.title("Reconstructed")
    plt.xticks([])
    plt.yticks([])

# plt.show()
plt.savefig("c15_13.png")
