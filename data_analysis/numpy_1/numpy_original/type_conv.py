import numpy as np

arr = np.array([1.2 ,2.2,5.3,4.8])
print(arr.dtype)
print(arr.shape)
print(arr.ndim)
print(arr.size)

print("now the typeconversion")
# astype(type of conversion)
# array_name.astype(int)
integer_arr = arr.astype(int)
print(integer_arr.dtype)

