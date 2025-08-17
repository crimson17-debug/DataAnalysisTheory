import numpy as np

''''
np.nan_to_num(array , nan = value) default = 0
'''


arr = np.array([1,2,0,np.nan,4,5,np.nan])
print(np.isnan(arr))

cleaned_array = np.nan_to_num(arr, nan = 100)
print(cleaned_array)
