#!/usr/bin/python

#https://projecteuler.net/problem=2

d = {}
number = 0

def fib(n):
    global number
    if n == 0:
        d[0] = 0
        return 0
    if n == 1:
        d[1] = 1
        return 1
    if n-1 in d:
        fib1 = d[n-1]
    else:
        fib1 = fib(n-1)
        d[n-1] = fib1
        if fib1 % 2 == 0:
            number = number + fib1
    if n-2 in d:
        fib2 = d[n-2]
    else:
        fib2 = fib(n-2)
        d[n-2] = fib2
        if fib1 % 2 == 0:
            number = number + fib1
    return fib1 + fib2

print(fib(34))
print(number)
