#  Write a NumPy program to create an element-wise comparison (greater, greater_equal, less and less_equal) of two given arrays.

import numpy as np 

a=np.array([23,68,15,78,10,13])
b=np.array([98,37,22,11,72,56])

greater = np.greater(a,b)
greater_equal = np.greater_equal(a,b)
lesser = np.less(a,b)
lesser_equal = np.less_equal(a,b)

print("Enter choice --> \n 1 - Check  Greater \n 2 - Check Less \n 3 - Check Greater or Equal \n 4 - Check Less or Equal")
print("Choice - ",input(switcher))


def choice(n):
    switcher={
        1:print(greater),
        2:print(lesser),
        3:print(greater_equal),
        4:print(lesser_equal)
    }
    return switcher.get(n,"Invalid Input")



choice(input())
if switcher==1:
    print(greater)
elif (switcher==2):
    print(lesser)
elif(switcher==3):
    print(greater_equal)
elif(switcher==4):
    print(lesser_equal)