''''
vertical stacking
horizontal stacking

vstack()  rowwise
hstack( )  column wise
'''


import numpy as np

arr1 = np.array([1,2,3,4])
arr2 = np.array([1,2,3,4])

print(np.stack((arr1,arr2)))
print(np.hstack((arr1,arr2)))
