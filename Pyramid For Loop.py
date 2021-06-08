n = int(input('Enter Height of Pyramid - '))


def pyramid(n) :
    for i in range(0, n):
        for j in range(0, i + 1):
            print('$ ', end='')
        print("\r")


pyramid(n)
