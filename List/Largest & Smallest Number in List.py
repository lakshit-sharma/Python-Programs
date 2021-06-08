# Write a Python program to get the largest number from a list.

x = [6,18,25,15,13,3,11]
# There are two methods for this problem=
# 1st user defined function


def largest_num(x):
    maximum = x[0]
    for a in x:
        if a > maximum:
            maximum = a
    return maximum

print("The Largest Number in List - ", largest_num(x))



def smallest_num(x):
    minimum = x[0]
    for a in x:
        if a < minimum:
            minimum = a
    return minimum
print("The Smallestt Number in List - ", smallest_num(x))


#2nd in-built function method -  


print("The Largest Number in List - ", max(x))
print("The Smallestt Number in List - ", min(x))
