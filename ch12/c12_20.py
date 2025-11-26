"""c12_20.py"""

import random

import h5py

nums_a = [random.randint(0, 100) for i in range(8)]
nums_b = [random.randint(0, 100) for i in range(8)]
nums_c = [random.randint(0, 100) for i in range(8)]
print(nums_a)
print(nums_b)
print(nums_c)

with h5py.File("nums.hdf5", "w") as f:
    f['nums_a'] = nums_a
    f['nums_b'] = nums_b
    f['nums_c'] = nums_c
