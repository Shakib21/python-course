	#!/usr/bin/env python
# coding: utf-8
def checkprime(n):
    for i in range(2,round(n/2)):
        if n%i == 0:
            return False
    return True

from collections import Counter
def getExponent(n):

    c = Counter(n)
    factors = []

    for i in range(min(n), max(n) + 1):
        if i in n:
            if c[i] != 1:
                factors.append(str(i) + '^' + str(c[i]))
            else:
                factors.append(str(i))

    return factors

n = int(input('Enter a number: '))
factors = []
counter = 2

while True:

    if n == 0 or n == 1:
        break

    for i in range(counter, n + 1):
        if n % i == 0:
            if checkprime(i):
                factors.append(i)
                n //= i
                break

if len(factors) != 0:
        factors = getExponent(factors)
        print(', '.join(factors))
else:
        print(n, 'doesnt have any prime factors.')