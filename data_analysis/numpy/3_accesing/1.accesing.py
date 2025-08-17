import numpy as np

# Create a 1D array
arr1d = np.array([10, 20, 30, 40, 50])

# Single element access
print("Single element access:", arr1d[2])  

# Negative indexing
print("Negative indexing:", arr1d[-1])  

# Create a 2D array
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Multidimensional array access
print("Multidimensional array access:", arr2d[1, 0])

arr3d = np.array([[[1,2],[1,2]], [[1,2], [1,2]]])

print("3D array access:", arr3d[0, 0,1])  # Accessing the first 2D array, second row, first column