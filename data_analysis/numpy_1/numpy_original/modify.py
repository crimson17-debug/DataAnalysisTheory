import numpy as np

""""
np.insert(array , index ,value , axis=None)
axis - 0 , acording to row wise
axis - 1 , acording to column wise
"""

arr = np.array([1,2,3,4,5,6,6,7])
new_arr = np.insert(arr , 2, 34) #adds aditional element doesnt replace the element

print(arr)
print(new_arr)

arr_1d = np.array([1,2.0,3,4,5,6])
arr_2d= np.array([[12,3,4,5],[1,2,3,4]])
arr_3d = np.array([[[1,2,3],[1,2,3]],[[1,2,3],[1,2,3]]])

new_arr_2d = np.insert(arr_2d , 1, [6,7] , axis = 0) # adds another array in the 1index and moves the aray in 1index to second in row
new_arr2_2d = np.insert(arr_2d , 1, [6,7] , axis = 1) # adds another array in the 1index and moves the aray in 1index to second in column

print(new_arr_2d)
print(new_arr2_2d)

new_arr3_2d = np.insert(arr_2d , 1, [6,7] , axis = None)
print(new_arr3_2d) # flattened array

