#Write a Python program to sum all the items in a list.
a = [1,3,5,7,8,9,2,4]

def addition(n):
    total = 0
    for i in a:
        total = total+i

    return total

print ('Sum of all the items in list',addition(a))
