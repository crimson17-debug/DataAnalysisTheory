import numpy as np

# shape of array

arr_1d = np.array([1,2.0,3,4])
arr_2d= np.array([[12,3,4,5],[1,2,3,4]])
arr_3d = np.array([[[1,2,3],[1,2,3]],[[1,2,3],[1,2,3]]])

print("the shape of the arrays")
print(arr_1d.shape)
print(arr_2d.shape)
print(arr_3d.shape)

# size of array - total no of elements
print("the size of the arrays")
print(arr_1d.size)
print(arr_2d.size)
print(arr_3d.size)

# ndim -no of dimensions
print("The dimensions of the array")
print(arr_1d.ndim)
print(arr_2d.ndim)
print(arr_3d.ndim)

print(arr_3d) # (no of matrix, rows , columns)

print("the datatype follows heirarchy")
print(arr_3d.dtype)
print(arr_1d.dtype)
print(arr_2d.dtype)




