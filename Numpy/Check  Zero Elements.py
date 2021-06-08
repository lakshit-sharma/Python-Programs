# Write a NumPy program to test whether none of the elements of a given array is zero.

import numpy as np

x= np.array([1,2,3],[5,6,7])
y=np.array([1,0,2],[2,4,5])

print(0 in x)
print(0 in y)