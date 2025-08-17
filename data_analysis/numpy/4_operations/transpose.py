import numpy as np
import sys


s = range(1000)
print(sys.getsizeof(s)) # size of the item in the list
print(sys.etsizeof(s)*len(s))  # total size of the list



d = np.arange(1000)
print(d.itemsize)
print(d.size * d.itemsize)

print(d.nbytes)




print()