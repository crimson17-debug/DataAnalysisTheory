import numpy as np
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

# Integer array indexing 
indices = np.array([1, 5, 3])
print ("Integer array indexing:", arr[indices])

# boolean array indexing 
cond = arr > 0
print ("\nElements greater than 0:\n", arr[cond])