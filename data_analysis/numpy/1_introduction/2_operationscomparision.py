import numpy as np
import sys

ls = [1,2,3,4,5]

arr = np.array(ls)


try:
    result = ls + 4
    print("List addition:", result)

except Exception as e:
    print("list addition failed:", e)


try:
    result = arr + 4
    print("Array addition:", result)    

except Exception as e:
    print("Array addition failed:", e)
