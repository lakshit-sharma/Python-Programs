#Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.
n=int(input("Enter Number - "))
x=n-17
if(n>17):
    print(x*2)
else:
    print(x)