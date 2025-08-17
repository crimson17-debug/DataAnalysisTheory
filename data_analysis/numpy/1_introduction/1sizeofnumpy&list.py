import numpy as np
import sys

s = range(1000);
print(sys.getsizeof(s))   #size of each element in bytes
print(sys.getsizeof(s) * len(s))      #size of the list in bytes


d = np.arange(1000)
print(d.itemsize) #size of each element in bytes
print(d.size * d.itemsize)  #size of the array in bytes 
