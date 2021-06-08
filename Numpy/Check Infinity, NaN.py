# Write a NumPy program to test a given array element-wise for finiteness (not infinity or not a Number).
import numpy as np

a = np.array([1, 0, np.nan, np.inf])

print('Original Array - ', a)
print('Finite Elements - ', np.isfinite(a))

# Write a NumPy program to test element-wise for positive or negative infinity.

print('Infinite Positive or NegativeElements - ', np.isinf(a))

# Write a NumPy program to test element-wise for NaN of a given array.
print('Check Nan Value - ', np.isnan(a))
