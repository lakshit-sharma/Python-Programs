# Write a Python program to print the numbers of a specified list after removing even numbers from it.

list1 = [3,10,45,22,46,86,93,12,100,38,101]

def specified_list(n):
    for i in n:
        if i % 2 == 0:
            list1.remove(i)
    return list1

print(specified_list(list1))
