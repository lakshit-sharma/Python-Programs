#Write a Python program to multiplies all the items in a list.

def multiply(n):
    total = 1
    for i in n:
        total = total*i

    return total
print('The Total of Multiplied Numbers - ' , multiply([1,2,3,4,5]))
