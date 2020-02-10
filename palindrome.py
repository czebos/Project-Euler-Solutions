#!/usr/bin/python

#https://projecteuler.net/problem=4
cap = 0
max = 0

def testPalindrome(inte):
    list1 = list(str(inte))
    list2 = []
    for num in list1:
        list2.append(num)
    list2.reverse()
    if list1 == list2:
        return True
    else:
        return False

def palindrome(n):
    n1 = n
    global cap
    while n > cap:
        while n1 > cap:
            if(testPalindrome(n*n1)):
                global max
                if(n*n1> max):
                    max = n*n1
                    cap = n1
            n1 = n1 - 1
        n = n - 1
        n1 = n

palindrome(999)
print (max)
print(cap)
