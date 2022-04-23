import sys

a = float(input('a = '))
c = float(input('c = '))

n = a + 4 * c
m = 2 * c + a
if m == 0:
    print('ERROR: divisor must not be zero')
    sys.exit(-1)

b = (n / m)

print(b)
