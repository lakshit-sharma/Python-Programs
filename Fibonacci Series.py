# Write a program to implement Fibonacci Series.

def fibonacci(n):
    result = []
    n1 = 0
    n2 = 1
    while n2 < n:  # Using while
        result.append(n2)  # add elements in empty list
        n3 = n2 + n1
        n1 = n2
        n2 = n3

    return result

print('The Fibonacci Series - ', fibonacci(100))

def fib(c):
    b=1
    for a in range(c+1):
        d=a+b
        a=b
        b=d
    return d

print(fib(9))