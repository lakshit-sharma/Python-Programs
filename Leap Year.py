# WAP to check whether the year entered by the user is leap year or not.

n=int(input("Enter Year - "))
if(n/4):
    if(n%4==0): 
        print(str(n)+" is a leap year",)
    else:
        print(str(n)+' is not a leap year')