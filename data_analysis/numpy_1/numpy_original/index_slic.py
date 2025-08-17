import numpy as np

arr = np.array([1,3,4,5,5,6])
arr_1d = np.array([1,2.0,3,4])
arr_2d= np.array([[12,3,4,5],[1,2,3,4]])
arr_3d = np.array([[[1,2,3],[1,2,3]],[[1,2,3],[1,2,3]]])

print(arr[0])
print(arr[-1])

# indexing from zero
print(arr_2d[1, 3]) # 1 row and 3 coloumn

print(arr_3d[1,1,2]) #1 matrix 1 row 2 column


# //////////////slicing///////////////////////#
print(arr[1:3]) #arr[1] to arr[2] elements
print(arr[:4]) # arr[0] to arr[3] elements 
print(arr[2:]) # arr[2] till end of all elements including last
print(arr[::-1]) #reverse of elements
print(arr[::2]) #every two elements will be printed



# ///////////fancy indexing//////////////////////////# selecting multiple elements at once

# takes a copy of the elements so chnges wont reflect in original array

# arr[[index1, idex2, index5]] --syntax

print(arr[[0,2,1]])




# /////////////////fiter idexing////////////////////////////
# boolean masking

print(arr[arr>3])


