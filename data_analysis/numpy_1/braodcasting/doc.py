''''
matching dimensions
expanding values
incompatible size

broadcasting smaller to larger expanding
faster than loops
1d 2d broadcasting

vecotrization --matrix operation
'''

import numpy as np

arr_1d = np.array([1,2.0,3,4])
arr_2d= np.array([[12,3,4,5],[1,2,3,4]])
arr_3d = np.array([[[1,2,3],[1,2,3]],[[1,2,3],[1,2,3]]])


matrix =np.array([[12,3,4,5],[1,2,3,4]])
vector = np.array([10, 20, 30 ,40])     #1d array

new_array = matrix + vector

print(new_array)

