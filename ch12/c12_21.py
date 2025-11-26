"""c12_21.py"""

import h5py

with h5py.File("nums.hdf5", "r") as f:
    nums_a_np = f['nums_a'][:]
    nums_b_np = f['nums_b'][:]
    nums_c_np = f['nums_c'][:]

print(type(nums_a_np))
print(nums_a_np)
print(nums_b_np)
print(nums_c_np)
