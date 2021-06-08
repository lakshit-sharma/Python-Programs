# Write a NumPy program to create an array of all the even integers from 30 to 70.

import numpy as np

# 1st method
x = np.arange(30, 71, 2)
print('Even Integers - ', x)

# 2nd method
y = np.arange(1, 11)
for i in y:
    if i % 2 == 0:
        print('Even Integers - ', i)
