def addition(x):
    sum = 0
    for i in range(x + 1):
        sum += i
    return sum

def multiply(x):
    value = 1
    for i in range (1, x + 1):
        value *= i
    return value

x = int(input("Enter Number - "))

print('Addition of all Numbers - ', addition(x))
print('Multiplication of all Numbers - ', multiply(x))