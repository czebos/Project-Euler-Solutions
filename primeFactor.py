#!/usr/bin/python

#https://projecteuler.net/problem=3
list = []

def primeFactor(n):
    end = True
    number = 2
    while n % number != 0:
        number += 1
        if number == n:
            end = False
            break
    global list
    list.append(number)
    if(end):
        primeFactor(n/number)

primeFactor(600851475143)
print(list)
