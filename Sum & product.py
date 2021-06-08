'''Accept two int values from the user and return their product.
If the product is greater than 1000, then return their sum.'''

x=int(input("Enter 1st Number - "))
y=int(input("Enter 2nd Number - "))
z=x*y
if(z>1000):
    z=x+y
    print('The product is greater than 1000, So the SUM is '+str(z))
else:
    print("The product is  - "+str(z))