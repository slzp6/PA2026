"""c12_18.py"""

import random

import h5py

nums = [random.randint(0, 100) for i in range(8)]
print(nums)

with h5py.File("nums.hdf5", "w") as f:
    # f.create_dataset('nums', data = nums)
    f['nums'] = nums
