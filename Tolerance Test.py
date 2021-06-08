# Write a NumPy program to test whether two arrays are element-wise equal within a tolerance.


import numpy as np

print(np.allclose([1e10,1e-7], [1.00001e10,1e-8]))
print(np.allclose([1e10,1e-8], [1.00001e10,1e-9]))
print(np.allclose([0.0000000000001,0.000000000000000000000010], [0.000000000000000000001,0.0000000000000000003]))