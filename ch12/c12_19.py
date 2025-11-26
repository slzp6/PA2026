"""c12_19.py"""

import h5py

with h5py.File("nums.hdf5", "r") as f:
    dataset = f['nums']
    print(type(dataset))
    print(dataset)
    nums_np = dataset[:]

print("---")
print(type(nums_np))
print(nums_np)

print("---")
nums = list(nums_np)
print(type(nums))
print(nums)
