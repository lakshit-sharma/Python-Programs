#Write a Python program to test whether a number is within 100 of 1000 or 2000.
n=int(input("Enter Number - "))
if(n<100):
    print("Number "+str(n)+" is smaller than 100")
elif(100<n<1000):
    print("Number "+str(n) +" is b/w 100 and 1000")
elif(1000<n<2000):
    print("Number "+str(n)+" is b/w 1000 and 2000")
else:
    print("Number "+str(n)+" is greater than 2000")