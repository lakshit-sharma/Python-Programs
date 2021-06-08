x=int(input('Enter number - '))

def prime(x):
    for i in range(2,x):
        if x%i==0:
            return False
    return True

if (prime(x)):
    print('This is a Prime Number.')
else:
    print('This is not a Prime Number.')
