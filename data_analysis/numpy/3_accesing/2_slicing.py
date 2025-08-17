import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
# #elements from index 1 to 3
# print("Range of Elements:",arr[0:2, 0:2])

# #arr[row_index_start: row_index_end, column_index_start: column_index_end]

# #all rows, second column
# print("Multidimensional Slicing:", arr[:, 1])

print(arr[: , 2])
