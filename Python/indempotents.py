#!/usr/bin/python

#https://projecteuler.net/problem=407
sum = 0
import time

def calculateLargest(upperBound):
    if upperBound == 0:
        return 0
    for i in range(upperBound):
        check = upperBound - i - 1
        if check**2 % upperBound == check % upperBound:
            return check
        if check < upperBound/2:
           return 1

for i in range(1000000):
    largestA = int(calculateLargest(i))
    sum += largestA
    #print ("Largest:" + str(largestA) + " " + "i:" + str(i))
    if i %100 == 0:
        print(i)

print(sum)
