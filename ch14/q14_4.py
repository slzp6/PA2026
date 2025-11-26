"""q14_4.py"""

from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

img = np.asarray(Image.open("sample.png"))
print(img.shape)

fig, ax = plt.subplots()
ax.imshow(img)
ax.set_xticks([])
ax.set_yticks([])
# plt.show()
plt.savefig("q14_4.png")
