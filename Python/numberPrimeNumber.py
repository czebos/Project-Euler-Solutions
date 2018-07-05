#!/usr/bin/python

#https://projecteuler.net/problem=7
def primeNumber(n):
    number = 2
    n1 = 1
    while n != 0:
        n1 = n1 + 1
        number = 2
        while n1 % number != 0:
            number += 1
            if n1 == number:
                n = n-1
                break
    return n1

print (primeNumber(10000))
