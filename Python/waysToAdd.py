#!/usr/bin/python

#https://projecteuler.net/problem=71

def findLessThanFrac(numToFind, denToFind, n):
    bestNumber = 0
    bestNum = 0
    num = 0
    den = 1
    while den < n:
        den += 1
        while (num/den) < (numToFind/denToFind):
            if (num + 1)/den < (numToFind/denToFind):
                num = num + 1
                if (num/den) > bestNumber:
                    bestNumber = num/den
                    bestNum = num
            else:
                break
    return bestNum

print(findLessThanFrac(3,7, 1000000))
