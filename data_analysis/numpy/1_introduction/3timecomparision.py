import numpy as np
import time

n = 1000000;


list1 = range(n)
list2 = range(n)

intial_time = time.time()


result = [(a*b) for a,b in zip(list1, list2)]

print(time.time()- intial_time)


array1 = np.arange(n)
array2 = np.arange(n)


intial_time = time.time()


result = array1 * array2

print(time.time()- intial_time)