import numpy as np

''''
np.isnf(array) 10 ^1000
boolean return
'''

arr = np.array([1,2,3,np.inf, 5, np.inf])

print(np.isinf(arr))

cleaned_arr = np.nan_to_num(arr , posinf=100, neginf=-100)
print(cleaned_arr)

