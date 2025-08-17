import numpy as np

arr = np.array([1,2,3,4])
new_arr = np.append(arr , [2,3,4])
print(new_arr)

arr1 = np.array([1,2,3,4])
arr2 = np.array([1,2,3,4])

# concatination

# np.concatenate((arr1 , arr2), axis = 0) verticl stacking
# np.concatenate((arr1 , arr2), axis = 1) horizontal stacking

new_arr1 = np.concatenate((arr1 , arr2), axis = 0)

print(new_arr1)
