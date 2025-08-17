import numpy as np

arr_1d = np.array([1,2.0,3,4,5,6])
arr_2d= np.array([[12,3,4,5],[1,2,3,4]])
arr_3d = np.array([[[1,2,3],[1,2,3]],[[1,2,3],[1,2,3]]])

# reshape(rows, columns) specifiy new shape
# if dimensions are same only then

reshaped_arr= arr_1d.reshape(2,3)
print(reshaped_arr)

# [[1. 2. 3.]
#  [4. 5. 6.]] 2 rows and 3 columns
#it changes the original value reference cannot directly print





