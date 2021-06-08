# Write a NumPy program to test whether none of the elements of a given array is zero or non zero.
import numpy as np

a = np.array([1, 2, 4])
b = np.array([1, 0, 3])
c = np.array([0, 0, 1, 0])
d = np.array([0, 0, 0, 0])
print('Array has zero element - ', 0 in a)
print('Array has zero element - ', 0 in b)
print('Array as non zero element - ', np.any(c))
print('Array as non zer element - ', np.any(d))
