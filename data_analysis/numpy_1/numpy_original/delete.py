import numpy as np

''''
np.delete(arr, index , axis = None) - copy
axis - none flatttened array
'''

arr = np.array([10,20,30,40,50,60,70])

new_arr= np.delete(arr, 1, axis = None)

print(new_arr)

arr_1d = np.array([1,2.0,3,4,5,6])
arr_2d= np.array([[12,3,4,5],[1,2,3,4]])
arr_3d = np.array([[[1,2,3],[1,2,3]],[[1,2,3],[1,2,3]]])


new_arr1 = np.delete(arr_2d , 1 , axis = 0) #removing wholefirst row since axis is 0
print(new_arr1)
new_arr1 = np.delete(arr_2d , 1 , axis = 1) #removing wholefirst column since axis is 1
print(new_arr1)