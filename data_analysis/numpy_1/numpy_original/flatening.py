import numpy as np

""""
if we have to convert
multidimensional arrays into 1d array
we use rival an flatten

.ravel() - view original
.flatten() - copy
"""

arr_1d = np.array([1,2.0,3,4,5,6])
arr_2d= np.array([[12,3,4,5],[1,2,3,4]])
arr_3d = np.array([[[1,2,3],[1,2,3]],[[1,2,3],[1,2,3]]])

print(arr_2d.ravel())
print(arr_2d.flatten())